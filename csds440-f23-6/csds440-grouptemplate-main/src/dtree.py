import argparse
import os.path
import warnings

from typing import Optional, List

import numpy as np
from sting.classifier import Classifier
from sting.data import Feature, parse_c45
from sting.data import FeatureType
from decimal import Decimal


import util

import warnings
from numba.core.errors import NumbaPendingDeprecationWarning

# Suppress specific Numba deprecation warnings
warnings.filterwarnings("ignore", category=NumbaPendingDeprecationWarning)

class Node():
    def __init__(self, schema = None, tests = None, class_label = None):
        self.schema = schema
        self.tests = tests
        self.children = {} # Empty dictionary, Every child key will be a test and the value will be a node
        self.class_label = class_label
        
        if class_label is not None:
            self.is_leaf = True
        else:
            self.is_leaf = False
        
    # Adds a child node to the current node given a certain test
    # all children will have an associated test, from the parent node
    def add_child(self, test, node, condition=None):
        if condition is not None:  # This is for continuous attributes
            self.children[(test, condition)] = node
        else:  # This is for discrete attributes
            self.children[test] = node
        
    # Returns the children of the node
    def get_children(self):
        return self.children
    
    # Returns the schema of the node
    def get_schema(self):
        return self.schema
    
    # Returns the list of tests for the node
    def get_tests(self):
        return self.tests
    
    # Returns the child node associated with the test
    def get_child(self, test, condition=None):
        if condition is not None:            
            return self.children[(test, condition)]
        else:
            return self.children[test]
    
    # Method to set a node as a leaf with a particular class label
    def set_as_leaf(self, class_label):
        self.class_label = class_label
        self.tests = []
        self.children = {}
        self.is_leaf = True
    
    # Method to get the class label of the leaf node
    def get_class_label(self):
        return self.class_label


# In Python, the convention for class names is CamelCase, just like in Java! However, the convention for method and
# variable names is lowercase_separated_by_underscores, unlike Java.
class DecisionTree(Classifier):
    def __init__(self, schema: List[Feature], tree_depth_limit: int, information_gain: bool):
        """
        This is the class where you will implement your decision tree. At the moment, we have provided some dummy code
        where this is simply a majority classifier in order to give you an idea of how the interface works. Don't forget
        to use all the good programming skills you learned in 132 and test_utilize numpy optimizations wherever possible.
        Good luck!
        """
        
        self._schema = schema  # For some models (like a decision tree) it makes sense to keep track of the data schema
        self._majority_label = 0  # Protected attributes in Python have an underscore prefix
        
        self.root = None
        
        self.masked_indices = []
        
        self.tree_depth_limit = tree_depth_limit
        
        self.information_gain = information_gain
        

    def fit(self, X: np.ndarray, y: np.ndarray, weights: Optional[np.ndarray] = None, current_depth: int = 0) -> None:
        #print('+------------------------+')
        """
        This is the method where the training algorithm will run.

        Args:
            X: The dataset. The shape is (n_examples, n_features).
            y: The labels. The shape is (n_examples,)
            weights: Weights for each example. Will become relevant later in the course, ignore for now.
        """
        
            # 1. Check if the current depth has reached the tree depth limit
        if current_depth >= self.tree_depth_limit:
            majority_label = util.majority_label(y)
            # Return leaf nodes
            return Node(schema=None, tests=None, class_label=majority_label)
        
        
        
        # Implement Split Criterion for Decision Tree
        try:
            split_criterion = self._determine_split_criterion(X, y, self._schema)
        except NotImplementedError:
            warnings.warn('This is for demonstration purposes only.')
                
         
        infogains = util.infogain(self._schema, X, y, split_criterion)
        
        # Masked infogains is the list of infogains that have not been used in the tree
        masked_infogains = [(i, gain) for i, gain in enumerate(infogains) if i not in self.masked_indices]
        
        # Find the tuple with the maximum gain in the masked list
        max_gain_tuple = max(masked_infogains, key=lambda x: x[1])
        
        # Masked ig index is the index of the feature with the highest infogain that has not been used in the tree
        # The first element of this tuple is the index in the original list
        max_ig_index = max_gain_tuple[0]
        
        
        if infogains[max_ig_index] == 0:
            #print("LEAF ACTIVATED")
            majority_label = util.majority_label(y)
            # returns leaf node
            return Node(schema = self._schema[max_ig_index], tests=None, class_label=majority_label)
        
        # if all labels are positive or negative, then create a leaf node
        if len(np.unique(y)) == 1:
            #print("LEAF ACTIVATED")
            #print("Leaf Name:", self._schema[max_ig_index].name)
            majority_label = util.majority_label(y)
            # returns leafe node
            return Node(schema = self._schema[max_ig_index], tests=None, class_label=majority_label)
        
        # Create root node
        #root = Node(self._schema[max_ig_index], split_criterion[max_ig_index]) # Passing the schema of the root feature only, not general schema
        root = Node(schema = self._schema[max_ig_index], tests = split_criterion[max_ig_index], class_label = None) # Passing the schema of the root feature only, not general schema
        
        # If the main root of the tree has yet been initialized, set it to the current root
        if self.root is None:
            self.root = root
        
        # if there are no more attributes to test, return the single node tree root, with label = most common value of the target attribute in the examples
        if len(self.masked_indices) == len(self._schema):
            #print("LEAF ACTIVATED")
            #print("Leaf Name:", self._schema[max_ig_index].name)
            majority_label = util.majority_label(y)
            # returns leafe node
            return Node(schema = self._schema[max_ig_index], tests=None, class_label=majority_label)        
                
        
        # Constructing children of root node
        
        for test in root.get_tests():
            
            # Create masked data and labels for the current test only have rows in which the root feature is equal to the test
                    
            # If the root feature is continuous 
            if self._schema[max_ig_index].ftype == FeatureType.CONTINUOUS:
                
                # For continuous attributes, split based on threshold
                mask1 = X[:, max_ig_index] <= test
                mask2 = X[:, max_ig_index] > test

                # Data for lesser than or equal test
                mask_X1 = X[mask1]
                mask_y1 = y[mask1]
                
                # Data for greater test
                mask_X2 = X[mask2]
                mask_y2 = y[mask2]
                    
                
                if len(self.masked_indices) == len(self._schema): # no more attributes to test
                    child1 = Node(schema = None, tests = None, class_label = util.majority_label(mask_y1))
                    child2 = Node(schema = None, tests = None, class_label = util.majority_label(mask_y2))

                    root.add_child(test, child1, '<=')
                    root.add_child(test, child2, '>')
                
                else:                    
                    
                    # If all label values are the same under the threshold, then create a leaf node
                    if len(np.unique(mask_y1)) == 1:
                        # Create a leaf node
                        child = Node(schema = None, tests = None, class_label = util.majority_label(mask_y1))
                        
                        root.add_child(test, child, '<=')
                    
                    # Recursive Call
                    else:             
                        child = self.fit(mask_X1, mask_y1, current_depth=current_depth + 1)
                        
                        root.add_child(test, child, '<=')
                        
                    # If all label values are the same above the threshold, then create a leaf node
                    if len(np.unique(mask_y2)) == 1:
                        child = Node(schema = None, tests = None, class_label = util.majority_label(mask_y2))
                        
                        root.add_child(test, child, '>')
                        
                    # Recursive Call
                    else:         
                        child = self.fit(mask_X2, mask_y2, current_depth=current_depth + 1)
                        
                        root.add_child(test, child, '>')        
        
           
            # If the feature is discrete
            else:
                # For discrete attributes, split based on equality
                mask = X[:, max_ig_index] == test
            
                mask_X = X[mask]
                mask_y = y[mask]
                
                if len(self.masked_indices) == len(self._schema): # no more attributes to test
                    #print("LEAF ACTIVATED")
                    child = Node(schema = None, tests = None, class_label = util.majority_label(mask_y))
                    root.add_child(test, child)
                        
                # if all label values are the same, then create a leaf node
                elif len(np.unique(mask_y)) == 1:
                    #print("LEAF ACTIVATED")
                    # Create a leaf node
                    child = Node(schema = None, tests = None, class_label = util.majority_label(mask_y))
                    root.add_child(test, child)

                # recursive call to fit covered by else case
                else:
                    #print("RECURSIVE CALL")
                    child = self.fit(mask_X, mask_y, current_depth=current_depth + 1)
                    root.add_child(test, child)
                    
        
        if max_ig_index not in self.masked_indices:
            self.masked_indices.append(max_ig_index)
                
            
        return root
        
        
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts class labels for a set of input examples using the trained decision tree.
    
        Args:
            X: The testing data with shape (n_examples, n_features).
    
        Returns:
            Predicted class labels as a NumPy array of shape (n_examples,).
        """
        n_examples = X.shape[0]
        # Initializing a NumPy array to store the predicted class labels for each example.
        predictions = np.empty(n_examples, dtype=int)
        
        
        for i in range (n_examples):
            current_node = self.root
            while not current_node.is_leaf:
                # get the value of the feature specified by the current node's schema
                feature_value = X[i, self._schema.index(current_node.get_schema())]
                
                if current_node.get_schema().ftype == FeatureType.NOMINAL:
                    # if the feature is discrete
                    if feature_value in current_node.get_children():
                        current_node = current_node.get_child(feature_value)
                    else:
                        # handle the case where the feature value is not in any child node
                        # (e.g., return the majority class label or backtrack)
                        predictions[i] = self._majority_label # Currently returning majority label as default
                        break
                    
                elif current_node.get_schema().ftype == FeatureType.CONTINUOUS: # assuming it's a continuous feature                    
                    found = False
                    for threshold in current_node.get_tests():
                        # Our feature value satisfies the threshold on one of the child node tests
                        if feature_value <= threshold:
                            # Update the current node                            
                            current_node = current_node.get_child(threshold, '<=')                            
                            found = True
                            break
                        else:
                            # Update the current node
                            current_node = current_node.get_child(threshold, '>')
                            found = True
                            break
                            
                        
                    if not found:
                        # handle the case where the feature value exceeds all thresholds
                        predictions[i] = self._majority_label # Currently returning majority label as default
                        break
            
            if current_node.is_leaf:
                predictions[i] = current_node.get_class_label()
                        
        return predictions 
    
    
    def get_max_depth(self, node=None, current_depth=0):
        """
        Compute the maximum depth of the tree.

        Args:
            node: the current node being inspected. Starts with the root node.
            current_depth: the depth of the current node.

        Returns:
            The maximum depth of the tree.
        """
        if node is None:
            node = self.root  # Start with the root node if no node is provided

        # If this is a leaf node (i.e., it has no children), then we've reached the bottom of this path.
        if node.is_leaf:
            return current_depth

        # Recursive case: this node is not a leaf, so get the depth of each subtree.
        children = node.get_children()
        max_depth = current_depth
        for child_key in children:
            child_node = children[child_key]  # Access the actual Node instance
            # Recur on each child subtree
            child_depth = self.get_max_depth(child_node, current_depth + 1)
            max_depth = max(max_depth, child_depth)

        return max_depth
        



    # In Python, instead of getters and setters we have properties: docs.python.org/3/library/functions.html#property
    @property
    def schema(self):
        """
        Returns: The dataset schema
        """
        return self._schema

    def _determine_split_criterion(self, X: np.ndarray, y: np.ndarray, schema: List[Feature]):
        """
        Determine decision tree split criterion. This is just an example to encourage you to use helper methods.
        Implement this however you like!
        """
        # Dictionary that associates each feature with a list of tests
        test_dic = {}
        # Loop through each column of data and calculate the tests for each feature
        for i in range(X.shape[1]):
            
            tests = []  # List to store test values for the current feature          
            datatype = schema[i] # Get the datatype of the current feature of the dataset
            
            # Sort the current column and labels based on the column values
            sorted_indices = np.argsort(X[:, i])
            sorted_column = X[:, i][sorted_indices]
            sorted_labels = y[sorted_indices]
                        
            
            # If the feature is continuous
            if datatype.ftype == FeatureType.CONTINUOUS:
                lastValChange = 0

                # Loop through the sorted data
                for index in range(1, len(sorted_column)):
                    current_value = sorted_column[index]
                    prev_value = sorted_column[index - 1]

                    current_label = sorted_labels[index]
                    prev_label = sorted_labels[index - 1]

                    if prev_value != current_value:
                        lastValChange = index-1

                    if prev_label != current_label:
                        newTest = (current_value + sorted_column[lastValChange]) / 2.0
                        tests.append(newTest)
                
                test_dic[i] = tests
            
            # If the feature is discrete
            #elif datatype.ftype == FeatureType.DISCRETE:
            else:
                # Calculate the unique values and their counts in the data
                unique_values= np.unique(X[:, i])
                for value in unique_values:
                    tests.append(value)
                
                test_dic[i] = tests
                
                    
        return test_dic 




def print_tree(node, depth=0):
    """
    Recursive function to print the structure of the decision tree.
    
    Args:
        node: The current node to print.
        depth: Current depth of the tree (used for indentation).
    """
    # Base case: If the node is a leaf
    if node.is_leaf:
        print("  " * depth + f"Leaf: Class label = {node.get_class_label()}")
        return
    
    # If the node is not a leaf
    print("  " * depth + f"Node: Schema = {node.get_schema().name}, Tests = {node.get_tests()}")
    
    # Recursively print children
    for key, child_node in node.get_children().items():
        # Check if the key is a tuple (for continuous attributes)
        if isinstance(key, tuple):
            test, condition = key
            print("  " * (depth + 1) + f"Test = {test}, Condition = {condition}")
        else:
            print("  " * (depth + 1) + f"Test = {key}")
        
        if isinstance(child_node, Node):
            print_tree(child_node, depth + 2)

                            

def evaluate_and_print_metrics(dtree: DecisionTree, X: np.ndarray, y: np.ndarray):
    """
    You will implement this method.
    Given a trained decision tree and labelled dataset, Evaluate the tree and print metrics.
    """

    y_hat = dtree.predict(X)
    acc = util.accuracy(y, y_hat)
    print(f'Accuracy: {acc:.2f}')
    
    precision = util.precision(y, y_hat)
    print(f'Precision: {precision:.2f}')
    
    recall = util.recall(y, y_hat)
    print(f'Recall: {recall:.2f}')
        
    #print('Size:', 0)
    #print('Maximum Depth:', 0)
    
    print('First Feature:', dtree.root.get_schema().name)

    #raise NotImplementedError()


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
        datasets = ((X, y, X, y),)

    for X_train, y_train, X_test, y_test in datasets:
        decision_tree = DecisionTree(schema, tree_depth_limit, information_gain)        
        decision_tree.fit(X_train, y_train)
        
    return decision_tree


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
