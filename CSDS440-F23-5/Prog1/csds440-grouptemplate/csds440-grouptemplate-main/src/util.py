import random
import warnings
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
        X: np.ndarray, y: np.ndarray, folds: int, stratified: bool = True
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

    if stratified: 

        pos_indices = np.where(y == 1)[0]
        neg_indices = np.where(y == 0)[0]

        np.random.shuffle(pos_indices)
        np.random.shuffle(neg_indices)

        pos_fold_sizes = [len(pos_indices) // folds] * folds
        neg_fold_sizes = [len(neg_indices) // folds] * folds

        for i in range(len(pos_indices) % folds):
            pos_fold_sizes[i] += 1

        for i in range(len(neg_indices) % folds):
            neg_fold_sizes[i] += 1

        result = []
        pos_current, neg_current = 0, 0
            
        for pos_fold_size, neg_fold_size in zip(pos_fold_sizes, neg_fold_sizes):
            pos_end, neg_end = pos_current + pos_fold_size, neg_current + neg_fold_size

            test_indices = np.concatenate([pos_indices[pos_current:pos_end], neg_indices[neg_current:neg_end]])
            train_indices = np.setdiff1d(np.arange(len(X)), test_indices)

            result.append((X[train_indices], y[train_indices], X[test_indices], y[test_indices]))

            pos_current, neg_current = pos_end, neg_end

        return tuple(result)

    else:
        warnings.warn('cv_split is not yet implemented. Simply returning the entire dataset as a single fold...')
        return (X, y, X, y)


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
    """
    Computes the precision of the predictions.

    Args:
        y: True labels.
        y_hat: Predicted labels.

    Returns: Precision
    """
    if y.size != y_hat.size:
        raise ValueError('y and y_hat must be the same shape/size!')
    
    tp = np.sum((y == 1) & (y_hat == 1))
    fp = np.sum((y == 0) & (y_hat == 1))

    denominator = tp + fp
    if denominator == 0:
        warnings.warn("Both TP and FP are zero, returning precision as 0.0")
        return 0.0

    return tp / denominator

def recall(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Computes the recall of the predictions.

    Args:
        y: True labels.
        y_hat: Predicted labels.

    Returns: Recall
    """
    if y.size != y_hat.size:
        raise ValueError('y and y_hat must be the same shape/size!')
    
    tp = np.sum((y == 1) & (y_hat == 1))
    fn = np.sum((y == 1) & (y_hat == 0))

    denominator = tp + fn
    if denominator == 0:
        warnings.warn("Both TP and FN are zero, returning recall as 0.0")
        return 0.0

    return tp / denominator

def roc_curve_pairs(y: np.ndarray, p_y_hat: np.ndarray) -> Iterable[Tuple[float, float]]:
    """
    Computes the ROC curve points.

    Args:
        y: True labels.
        p_y_hat: Predicted probabilities.

    Returns: A list of tuples (false positive rate, true positive rate)
    """
    if y.size != p_y_hat.size:
        raise ValueError('y and p_y_hat must be the same shape/size!')
    
    thresholds = sorted(list(set(p_y_hat)), reverse=True)
    roc_points = []

    for t in thresholds:
        y_hat_t = (p_y_hat >= t).astype(int)
        fpr = np.sum((y == 0) & (y_hat_t == 1)) / np.sum(y == 0)
        tpr = np.sum((y == 1) & (y_hat_t == 1)) / np.sum(y == 1)
        roc_points.append((fpr, tpr))

    return roc_points


def auc(y: np.ndarray, p_y_hat: np.ndarray) -> float:
    """
    Computes the AUC (Area Under Curve) of the ROC.

    Args:
        y: True labels.
        p_y_hat: Predicted probabilities.

    Returns: AUC value
    """

    roc_pairs = list(roc_curve_pairs(y, p_y_hat))
    area = 0.0

    for i in range(1, len(roc_pairs)):
        fpr_prev, tpr_prev = roc_pairs[i-1]
        fpr, tpr = roc_pairs[i]
        area += (fpr - fpr_prev) * (tpr + tpr_prev) / 2

    return area