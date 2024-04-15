class TreeNode:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, value=None):
        """
        This is the class we used to construct the nodes in the DecisionTree
        """
        self.feature_index = feature_index  # feature index on which the node splits
        self.threshold = threshold  # threshold value if the feature is continuous
        self.left = left  # TreeNode for left subtree
        self.right = right  # TreeNode for right subtree
        self.value = value  # Value of the leaf node (pure node/class label) 

import sys
sys.path.append('D:\\MachineLearning')

import argparse
import os.path
import warnings
import util
import numpy as np

from typing import Optional, List
from numpy import ndarray
from sting.classifier import Classifier
from sting.data import Feature, FeatureType, parse_c45

# In Python, the convention for class names is CamelCase, just like Java! However, the convention for method and
# variable names is lowercase_separated_by_underscores, unlike Java.
class DecisionTree(Classifier):
    
    def __init__(self, schema: List[Feature]):
        """
        This is the class where you will implement your decision tree. At the moment, we have provided some dummy code
        where this is simply a majority classifier in order to give you an idea of how the interface works. Don't forget
        to use all the good programming skills you learned in 132 and utilize numpy optimizations wherever possible.
        Good luck!
        """

        self._schema = schema  # For some models (like a decision tree) it makes sense to keep track of the data schema
        self._majority_label = 0  # Protected attributes in Python have an underscore prefix
        
        self.use_information_gain = True
        self.root = None
        self.max_depth = None
        
# In Python, instead of getters and setters we have properties: docs.python.org/3/library/functions.html#property
    @property
    def schema(self):
        """
        Returns: The dataset schema
        """
        return self._schema
        
    def _entropy(self, y: np.ndarray) :
        """
        Calculate the entropy of the given labels.
        A helper method used to calculate the information gain.
        """
        
        pos_prob = y.sum() / len(y)
        neg_prob = (len(y) - y.sum()) / len(y)
    
        pos_entropy = - pos_prob * np.log2(pos_prob) if pos_prob > 0 else 0
        neg_entropy = - neg_prob * np.log2(neg_prob) if neg_prob > 0 else 0
            
        entropy = pos_entropy + neg_entropy
        return entropy

    def _fit_tree(self, X, y, current_depth: int, remaining_features: List[int]) -> TreeNode:
        
        #Case1 : All samples have the same label(pure nodes)
        unique_labels = np.unique(y)
        if len(unique_labels) == 1:
            return TreeNode(value = unique_labels[0])
            
        #Case2 : Reached max depth or All attributes are exhausted
        if not remaining_features or (self.max_depth is not None and current_depth >= self.max_depth):
            majority_label = 1 if np.sum(y) > len(y) / 2 else 0
            return TreeNode(value = majority_label)
    
        best_split_feature, best_threshold = self._determine_split_criterion(X, y, remaining_features)
        
        #Case3: No good split found
        if best_split_feature is None:
            majority_label = 1 if np.sum(y) > len(y) / 2 else 0
            return TreeNode(value=majority_label)
            
        #Split the dataset
        if self._schema[best_split_feature].ftype == FeatureType.NOMINAL:
            # For nominal attributes, simply split using equality
            left_indices = X[:, best_split_feature] == best_threshold
            right_indices = X[:, best_split_feature] != best_threshold
        else:
            # For continuous attributes, split using a threshold
            left_indices = X[:, best_split_feature] <= best_threshold
            right_indices = X[:, best_split_feature] > best_threshold

        # Check if one of the splits is empty
        if sum(left_indices) == 0 or sum(right_indices) == 0:
            majority_label = 1 if np.sum(y) > len(y) / 2 else 0
            return TreeNode(value=majority_label)
            
       #Remove the attributes that are already tested
        next_remaining_features = remaining_features.copy()
        next_remaining_features.remove(best_split_feature)
    
        left_subtree = self._fit_tree(X[left_indices], y[left_indices], current_depth + 1, next_remaining_features)
        right_subtree = self._fit_tree(X[right_indices], y[right_indices], current_depth + 1,next_remaining_features)
        
        return TreeNode(feature_index=best_split_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)


    def fit(self, X: np.ndarray, y: np.ndarray, weights: Optional[np.ndarray] = None) -> None:
        """
        This is the method where the training algorithm will run.
    
        Args:
            X: The dataset. The shape is (n_examples, n_features).
            y: The labels. The shape is (n_examples,)
            weights: Weights for each example. Will become relevant later in the course, ignore for now.
        """
    
        initial_remaining_features = list(range(X.shape[1]))
    
        # Begin tree construction starting from the root
        self.root = self._fit_tree(X, y, current_depth=0, remaining_features= initial_remaining_features)
    
        n_zero, n_one = util.count_label_occurrences(y)
    
        if n_one > n_zero:
            self._majority_label = 1
        else:
            self._majority_label = 0

    def _traverse_tree(self, x: ndarray, node: TreeNode):
        """
        This is the method we predict the label of new example coming in our tree
    
        Args:
            x: The specific example in dataset. The shape is (, n_features).
            node: The attributes with threshold we used to classify the example. The shape is (n_examples,)
            weights: Weights for each example. Will become relevant later in the course, ignore for now.
        """      
        
        if node.left is None and node.right is None: #base case: node is a leaf node (meaning that it is labeled)
            return node.value
            
        feature_val = x[node.feature_index]
        
        if self._schema[node.feature_index].ftype == FeatureType.NOMINAL:
            if feature_val == node.threshold:
                return self._traverse_tree(x, node.left)
            return self._traverse_tree(x, node.right)
        else:
            if feature_val <= node.threshold:
                return self._traverse_tree(x, node.left)
            return self._traverse_tree(x, node.right)
            

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        This is the method where the decision tree is evaluated.
    
        Args:
            X: The testing data of shape (n_examples, n_features).
    
        Returns: Predictions of shape (n_examples,), either 0 or 1
        """
        y_pred = [self._traverse_tree(x, self.root) for x in X]
        return np.array(y_pred)


    def _information_gain(self, X: np.ndarray, y: np.ndarray, feature_index: int) :
        """
        Calculate the information gain after partitioning the dataset by attribute X
    
        :param feature_index: the index of attribute X used to partition the dataset.
        """
        if self.schema[feature_index].name == 'image_id':
            return -float('inf'), None
    
        entropy_before = self._entropy(y)      
        
        if(self.schema[feature_index].ftype == FeatureType.NOMINAL):
            
            conditional_entropy_1 = 0
            column_values = X[:,feature_index]
            best_split_point = 0
            gain_nominal = 0
            
            for value in np.unique(column_values):
                subset_indices = np.where(column_values == value)
                subset = y[subset_indices]
    
                weight = len(subset) / len(y)
                entropy = self._entropy(subset)
                
                conditional_entropy_1 += weight * entropy
                gain = entropy_before - conditional_entropy_1
                
                if gain > gain_nominal:
                    best_split_point = value
                    gain_nominal = gain
                    
            return gain_nominal, best_split_point
    
        elif (self.schema[feature_index].ftype == FeatureType.CONTINUOUS):
            
            conditional_entropy_2 = 0
            best_split_point = 0
            gain_continuous = 0
            split_points = self._split_continuous_feature(X, y, feature_index)
    
            for midpoint, left_indices, right_indices in split_points:
                
                    left_subset = y[left_indices]
                    right_subset = y[right_indices]
                
                    # Skip this midpoint if one of the subsets is empty
                    if len(left_subset) == 0 or len(right_subset) == 0:
                        continue
                        
                    left_weight = len(left_subset) / len(y)
                    right_weight = len(right_subset) / len(y)
    
                    conditional_entropy_2 = left_weight * self._entropy(left_subset) + right_weight * self._entropy(right_subset)
                    gain_midpoint = entropy_before - conditional_entropy_2
    
                    if gain_midpoint > gain_continuous:
                        best_split_point = midpoint
                        gain_continuous = gain_midpoint
            
            return gain_continuous, best_split_point

    def _feature_information(self, X:np.array, y:np.array, feature_index: int):
        
        if self.schema[feature_index].ftype == FeatureType.NOMINAL:           
            values, counts = np.unique(X[:, feature_index], return_counts=True)
            probs = counts / len(X)
            feature_info = -np.sum(probs * np.log2(probs))
    
            return feature_info
            
        elif self.schema[feature_index].ftype == FeatureType.CONTINUOUS:
            split_points = self._split_continuous_feature(X, y, feature_index)
            feature_info_values = []
            
            for midpoint, left_indices, right_indices in split_points:
                
                left_subset = X[left_indices]
                right_subset = X[right_indices]
    
                left_probs = len(left_subset) / len(X)
                right_probs = len(right_subset) / len(X)
    
                feature_info = 0
                feature_info += - left_probs * np.log2(left_probs) if left_probs > 0 else 0
                feature_info += - right_probs * np.log2(right_probs) if right_probs > 0 else 0
    
                feature_info_values.append(feature_info)
            return np.mean(feature_info_values)

    def _gain_ratio(self, X:np.array, y:np.array, feature_index: int):
    
        info_gain = self._information_gain(X, y, feature_index)[0]
        feature_info = self._feature_information(X, y, feature_index)
        gain_ratio = info_gain / feature_info if feature_info != 0 else 0
        
        return gain_ratio


    def _split_continuous_feature(self, X: np.ndarray, y: np.ndarray, feature_index: int):
    
        sorted_indices = np.argsort(X[:, feature_index])
        X_sorted = X[sorted_indices]
        y_sorted = y[sorted_indices]
        last_midpoint = None
        split_points = []
    
        for i in range(len(y_sorted) - 1):
            if y_sorted[i] != y_sorted[i+1]:
                midpoint = ((X_sorted[i,feature_index]) + (X_sorted[i+1,feature_index])) / 2
                if midpoint != last_midpoint: 
                    last_midpoint = midpoint
                    left_indices = np.where(X[:, feature_index] <= midpoint)
                    right_indices = np.where(X[:, feature_index] > midpoint) 
                    split_points.append((midpoint, left_indices, right_indices))
                
        return split_points

    # It is standard practice to prepend helper methods with an underscore "_" to mark them as protected.
    def _determine_split_criterion(self, X: np.ndarray, y: np.ndarray, remaining_features: List[int]):
        """
        Determine decision tree split criterion. This is just an example to encourage you to use helper methods.
        Implement this however you like!
        """
        max_criterion_value = -float('inf')
        best_feature_index = None
        split_point = None
    
        #Iterate over all features
        for feature_index in remaining_features:
            if self.use_information_gain:
                criterion_value, best_split_point = self._information_gain(X, y, feature_index)
            else:
                criterion_value, best_split_point = self._gain_ratio(X, y, feature_index)
                
            if criterion_value > max_criterion_value:
                max_criterion_value = criterion_value 
                best_feature_index = feature_index
                split_point = best_split_point
        
        return best_feature_index, split_point

def evaluate_and_print_metrics(dtree: DecisionTree, X: np.ndarray, y: np.ndarray):
    """
    You will implement this method.
    Given a trained decision tree and labelled dataset, Evaluate the tree and print metrics.
    """
    def tree_size(node):
        if node == None:
            return 0
        return 1 + tree_size(node.left) + tree_size(node.right)

    def tree_depth(node):
        if node == None:
            return 0
        left_depth = tree_depth(node.left) if node.left is not None else 0
        right_depth = tree_depth(node.right) if node.right is not None else 0
        
        return 1 + max(left_depth, right_depth)

    y_hat = dtree.predict(X)
    acc = util.accuracy(y, y_hat)
    
    return acc, tree_size(dtree.root), tree_depth(dtree.root) - 1

def dtree(data_path: str, tree_depth_limit: int, use_cross_validation: bool = True, information_gain: bool = True):
    """
    It is highly recommended that you make a function like this to run your program so that you are able to run it
    easily from a Jupyter notebook. This function has been PARTIALLY implemented for you, but not completely!

    :param data_path: The path to the data.
    :param tree_depth_limit: Depth limit of the decision tree
    :param use_cross_validation: If True, use cross validation. Otherwise, run on the full dataset.
    :param information_gain: If true, use information gain as the split criterion. Otherwise use gain ratio.
    :return:
    """

    # last entry in the data_path is the file base (name of the dataset)
    path = os.path.expanduser(data_path).split(os.sep)
    file_base = path[-1]  # -1 accesses the last entry of an iterable in Python
    root_dir = os.sep.join(path[:-1])
    schema, X, y = parse_c45(file_base, root_dir)

    if use_cross_validation:
        datasets = util.cv_split(X, y, folds=5, stratified=True)
    else:
        datasets = (X, y, X, y)
        
    total_accuracy = 0
    total_size = 0
    total_depth = 0
    
    for X_train, y_train, X_test, y_test in datasets:
        decision_tree = DecisionTree(schema)
        decision_tree.use_information_gain = information_gain
        decision_tree.max_depth = tree_depth_limit
        decision_tree.fit(X_train, y_train)
        acc, size, depth = evaluate_and_print_metrics(decision_tree, X_test, y_test)

        total_accuracy += acc
        total_size += size
        total_depth += depth

    num_datasets = len(datasets)
    avg_accuracy = total_accuracy / num_datasets
    avg_size = total_size / num_datasets
    avg_depth = total_depth / num_datasets
    
    print(f'Average Accuracy: {avg_accuracy:.2f}')
    print(f'Average Size: {avg_size:.0f}')
    print(f'Average Maximum Depth: {avg_depth:.0f}')
    print('First Feature:', schema[0])

if __name__ == '__main__':
    """
    THIS IS YOUR MAIN FUNCTION. You will implement the evaluation of the program here. We have provided argparse code
    for you for this assignment, but in the future you may be responsible for doing this yourself.
    """

    # Set up argparse arguments
    parser = argparse.ArgumentParser(description='Run a decision tree algorithm.')
    parser.add_argument('path', metavar='PATH', type=str, help='The path to the data.')
    parser.add_argument('depth_limit', metavar='DEPTH', type=int,
                        help='Depth limit of the tree. Must be a non-negative integer. A value of 0 sets no limit.')
    parser.add_argument('--no-cv', dest='cv', action='store_false',
                        help='Disables cross validation and trains on the full dataset.')
    parser.add_argument('--use-gain-ratio', dest='gain_ratio', action='store_true',
                        help='Use gain ratio as tree split criterion instead of information gain.')
    parser.set_defaults(cv=True, gain_ratio=False)
    args = parser.parse_args()

    # If the depth limit is negative throw an exception
    if args.depth_limit < 0:
        raise argparse.ArgumentTypeError('Tree depth limit must be non-negative.')

    # You can access args with the dot operator like so:
    data_path = os.path.expanduser(args.path)
    tree_depth_limit = args.depth_limit
    use_cross_validation = args.cv
    use_information_gain = not args.gain_ratio

    dtree(data_path, tree_depth_limit, use_cross_validation, use_information_gain)