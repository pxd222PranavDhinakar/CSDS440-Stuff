import random
from typing import Tuple, Iterable

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


def entropy():
    # Implement this on your own!
    raise NotImplementedError


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


    return (X, y, X, y),


def accuracy(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Another example of a helper method. Implement the rest yourself!

    Args:
        y: True labels.
        y_hat: Predicted labels.

    Returns: Accuracy
    """

    if y.size != y_hat.size:
        raise ValueError('y and y_hat must be the same shape/size!')

    n = y.size

    return (y == y_hat).sum() / n


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
    
    # Iterate over all unique thresholds in descending order
    for threshold in np.unique(p_y_hat)[::-1]:
        # Count true positive and false positive for the current threshold
        tp = np.sum((y == 1) & (p_y_hat >= threshold))
        fp = np.sum((y == 0) & (p_y_hat >= threshold))

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
        # Calculate the width (difference in FPR) and the average height (average of TPR) of each trapezoid
        width = roc_pairs[i][0] - roc_pairs[i - 1][0]
        height = (roc_pairs[i][1] + roc_pairs[i - 1][1]) / 2
        auc_value += width * height

    return auc_value
