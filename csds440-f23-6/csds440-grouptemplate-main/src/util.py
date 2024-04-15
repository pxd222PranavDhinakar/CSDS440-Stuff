import random
import warnings
from typing import Tuple, Iterable
from sting.data import FeatureType

import numpy as np

"""
This is where you will implement helper functions and utility code which you will reuse from project to project.
Feel free to edit the parameters if necessary or if it makes it more convenient.
Make sure you read the instruction clearly to know whether you have to implement a function for a specific assignment.
"""


def count_label_occurrences(y: np.ndarray) -> Tuple[int, int]:
    """
    This is a simple example of a helpful helper method you may decide to implement. Simply takes an array of labels and
    counts the number of positive and negative labels.

    HINT: Maybe a method like this is useful for calculating more complicated things like entropy!

    Args:
        y: Array of binary labels.

    Returns: A tuple containing the number of negative occurrences, and number of positive occurences, respectively.

    """
    n_ones = (y == 1).sum()  # How does this work? What does (y == 1) return?
    n_zeros = y.size - n_ones
    return n_zeros, n_ones



def calculate_column_entropy(schema, X, y, split_criterion):
    entropies = []
    
    # Iterate through each column
    for i in range(X.shape[1]):
        column = X[:, i]
        # Check if the column is continuous or discrete
        if schema[i].ftype == FeatureType.CONTINUOUS:
            entropy = entropy_continuous(column, y, split_criterion[i])
            entropies.append(entropy)
            
        else:
            # If the column is discrete, calculate the entropy of the column
            entropy = entropy_discrete(column, y, split_criterion[i])
            entropies.append(entropy)

    return entropies
            
def entropy_continuous(column, labels, tests):    
    entropies = []
    
    #print('Tests: ', tests)
    for test in tests:
        #print(test)
        
        # Split column data based on the test
        left_indices = column <= test
        right_indices = column > test
    
        
        
        # Calculate the left and right entropies
        #left_entropy = 0 if calculate_entropy(labels[left_indices]) == 1.0 else calculate_entropy(labels[left_indices])
        left_entropy = calculate_entropy(labels[left_indices])

        
        #right_entropy = 0 if calculate_entropy(labels[right_indices]) == 1.0 else calculate_entropy(labels[right_indices])
        right_entropy = calculate_entropy(labels[right_indices])
        
        #probability of left test
        prob_left = len(labels[left_indices]) / len(labels)
        #probability of right test
        prob_right = len(labels[right_indices]) / len(labels)
        
        # Calculate the total entropy
        #total_entropy += prob_left * left_entropy + prob_right * right_entropy
        
        # Calculate the weighted entropy for this test value
        weighted_entropy = prob_left * left_entropy + prob_right * right_entropy
        entropies.append(weighted_entropy)
        
        
    #print('Entropies:', entropies)
    return min(entropies) 


def entropy_discrete(column, labels, tests):    
    total_entropy = 0.0
    
    for test in tests:
        # Split column data based on the test
        test_indeces = column == test
        
        # Calculate the test entropy
        test_entropy = calculate_entropy(labels[test_indeces])
        
        #probability of test
        prob_test = len(labels[test_indeces]) / len(labels)
        
        # Calculate the total entropy
        total_entropy += prob_test * test_entropy
        
    return total_entropy      
    
          
def calculate_entropy(labels):
    unique_values, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    entropy_value = -np.sum(probabilities * np.log2(probabilities))
    return entropy_value

def majority_label(labels):
    unique_values, counts = np.unique(labels, return_counts=True)
    return unique_values[np.argmax(counts)]

def minority_label(labels):
    unique_values, counts = np.unique(labels, return_counts=True)
    return unique_values[np.argmax(counts)]

def infogain(schema, data, labels, split_criterion):
    # Get the entropy of the labels w.r.t themself
    entropy_labels = calculate_entropy(labels)
    
    # Get the entropy of the labels w.r.t the data
    entropy_labels_data = calculate_column_entropy(schema, data, labels, split_criterion)
    
    # Calculate the information gain
    information_gains = entropy_labels - entropy_labels_data
    
    return information_gains


def cv_split(
        X: np.ndarray, y: np.ndarray, folds: int, stratified: bool = False
    ) -> Tuple[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray], ...]:
    """
    Conducts a cross-validation split on the given data.

    Args:
        X: Data of shape (n_examples, n_features)
        y: Labels of shape (n_examples,)
        folds: Number of CV folds
        stratified:

    Returns: A tuple containing the training data, training labels, testing data, and testing labels, respectively
    for each fold.

    For example, 5 fold cross validation would return the following:
    (
        (X_train_1, y_train_1, X_test_1, y_test_1),
        (X_train_2, y_train_2, X_test_2, y_test_2),
        (X_train_3, y_train_3, X_test_3, y_test_3),
        (X_train_4, y_train_4, X_test_4, y_test_4),
        (X_train_5, y_train_5, X_test_5, y_test_5)
    )

    """

    # Set the RNG seed to 12345 to ensure repeatability
    np.random.seed(12345)
    random.seed(12345)

    # HINT!
    if stratified:
        n_zeros, n_ones = count_label_occurrences(y)

    #warnings.warn('cv_split is not yet implemented. Simply returning the entire dataset as a single fold...')

    return (X, y, X, y),


def accuracy(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Another example of a helper method. Implement the rest yourself!

    Args:
        y: True labels.
        y_hat: Predicted labels.

    Returns: Accuracy
    """
    
    correct_predictions = np.sum(y == y_hat)
    total_predictions = len(y)
    
    return correct_predictions / total_predictions


def precision(y: np.ndarray, y_hat: np.ndarray) -> float:
    # True positives are cases when the actual label and the predicted label are both 1.
    true_positives = np.sum((y == 1) & (y_hat == 1))
    # Predicted positives are cases when the predicted label is 1.
    predicted_positives = np.sum(y_hat == 1)
    return true_positives / predicted_positives if predicted_positives > 0 else 0.0
    

def recall(y: np.ndarray, y_hat: np.ndarray) -> float:
    # True positives are cases when the actual label and the predicted label are both 1.
    true_positives = np.sum((y == 1) & (y_hat == 1))
    # Actual positives are cases when the actual label is 1.
    actual_positives = np.sum(y == 1)
    return true_positives / actual_positives if actual_positives > 0 else 0.0
    

def roc_curve_pairs(y: np.ndarray, p_y_hat: np.ndarray) -> Iterable[Tuple[float, float]]:
    # Sort the predicted probabilities and corresponding true labels in descending order.
    desc_score_indices = np.argsort(p_y_hat)[::-1]
    p_y_hat = p_y_hat[desc_score_indices]
    y = y[desc_score_indices]

    # Initialize variables
    fpr_values = [0]
    tpr_values = [0]
    n_pos = np.sum(y)
    n_neg = len(y) - n_pos
    tp = 0
    fp = 0

    # Iterate over all unique thresholds in descending order
    for threshold in np.unique(p_y_hat)[::-1]:
        # Update counts of true positive and false positive
        for i in range(len(p_y_hat)):
            if p_y_hat[i] > threshold:
                if y[i] == 1:
                    tp += 1
                else:
                    fp += 1
            else:
                break  # since the arrays are sorted, no need to continue the loop after crossing the threshold

        # Calculate false positive rate and true positive rate
        fpr = fp / n_neg if n_neg != 0 else 0
        tpr = tp / n_pos if n_pos != 0 else 0

        # Append to the lists
        fpr_values.append(fpr)
        tpr_values.append(tpr)

    return list(zip(fpr_values, tpr_values))
    
    

def auc(y: np.ndarray, p_y_hat: np.ndarray) -> float:
    roc_pairs = roc_curve_pairs(y, p_y_hat)
        
    # Initialize area under curve
    auc_value = 0.0
    
    # Calculate AUC using the Trapezoidal rule
    for i in range(1, len(roc_pairs)):
        auc_value += (roc_pairs[i][0] - roc_pairs[i - 1][0]) * (roc_pairs[i][1] + roc_pairs[i - 1][1])
    auc_value *= 0.5  # since we're applying the trapezoidal rule
    
    return auc_value