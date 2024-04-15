import sys
import scipy
import argparse
import numpy as np
import pandas as pd
from scipy.special import logsumexp
from util import cv_split, accuracy, precision, recall, roc_curve_pairs, auc

# Set the random seed for repeatability
np.random.seed(12345)

class NaiveBayesClassifier:
    def __init__(self, num_bins, m_estimate):
        """
        Naive Bayes Classifier that handles continuous features by discretizing them into equal-length bins
        and uses m-estimates for probability smoothing.

        Args:
        num_bins (int): The number of bins to use for discretizing continuous features.
        m_estimate (float): The m value for m-estimates. If negative, use Laplace smoothing.
                            If zero, use maximum likelihood estimation with epsilon smoothing.
        """
        self.num_bins = num_bins
        self.m_estimate = m_estimate
        self.bin_edges = None
        self.class_priors = None
        self.feature_probs = None
        self.epsilon = 1e-9  # small value to prevent log(0)

    def fit(self, X, y):
        """
        Fit the Naive Bayes classifier according to X, y.

        Args:
        X (np.ndarray): Training data of shape (n_samples, n_features).
        y (np.ndarray): Target values (class labels) of shape (n_samples,).
        """
        # Discretize continuous features
        self.bin_edges = [np.linspace(np.min(X[:, j]), np.max(X[:, j]), self.num_bins + 1) for j in range(X.shape[1])]
        X_discrete = np.array([np.digitize(X[:, j], bins=self.bin_edges[j][1:-1]) for j in range(X.shape[1])]).T

        # Calculate class priors
        self.classes, counts = np.unique(y, return_counts=True)
        self.class_priors = counts / y.size

        # Calculate feature probabilities within each class
        self.feature_probs = {}
        for class_val in self.classes:
            self.feature_probs[class_val] = []
            X_class = X_discrete[y == class_val]
            for j in range(X.shape[1]):
                feature_counts = np.array([np.sum(X_class[:, j] == bin_idx) for bin_idx in range(self.num_bins)])
                # Apply m-estimates, Laplace smoothing, or epsilon smoothing based on the value of m_estimate
                if self.m_estimate == 0:  # Maximum likelihood estimation with epsilon smoothing
                    smoothed_counts = (feature_counts + self.epsilon) / (np.sum(feature_counts) + self.epsilon * self.num_bins)
                elif self.m_estimate < 0:  # Laplace smoothing
                    smoothed_counts = (feature_counts + 1) / (np.sum(feature_counts) + self.num_bins)
                else:  # m-estimate
                    p = 1.0 / self.num_bins  # p value for m-estimate
                    smoothed_counts = (feature_counts + self.m_estimate * p) / (np.sum(feature_counts) + self.m_estimate)
                self.feature_probs[class_val].append(smoothed_counts)

    def predict(self, X):
        """
        Perform classification on an array of test vectors X.

        Args:
        X (np.ndarray): Test data of shape (n_samples, n_features).

        Returns:
        y_pred (np.ndarray): Predicted class labels for each sample.
        """
        X_discrete = np.array([np.digitize(X[:, j], bins=self.bin_edges[j][1:-1]) for j in range(X.shape[1])]).T
        log_probabilities = []

        for x in X_discrete:
            log_probs_x = []
            for class_val in self.classes:
                # Calculate log probabilities to avoid underflow
                log_prob_x_class = np.log(self.class_priors[class_val])
                for j, bin_idx in enumerate(x):
                    # Avoiding log(0) by adding epsilon
                    prob = self.feature_probs[class_val][j][bin_idx]
                    log_prob_x_class += np.log(max(prob, self.epsilon))
                log_probs_x.append(log_prob_x_class)
            log_probabilities.append(log_probs_x)

        return self.classes[np.argmax(log_probabilities, axis=1)]

    def predict_proba(self, X):
        """
        Return probability estimates for the test vector X.

        Args:
        X (np.ndarray): Test data of shape (n_samples, n_features).

        Returns:
        probabilities (np.ndarray): Probability of the sample for each class in the model.
        """
        X_discrete = np.array([np.digitize(X[:, j], bins=self.bin_edges[j][1:-1]) for j in range(X.shape[1])]).T
        log_probabilities = []

        for x in X_discrete:
            log_probs_x = []
            for class_val in self.classes:
                # Calculate log probabilities to avoid underflow
                log_prob_x_class = np.log(self.class_priors[class_val])
                for j, bin_idx in enumerate(x):
                    log_prob_x_class += np.log(self.feature_probs[class_val][j][bin_idx])
                log_probs_x.append(log_prob_x_class)
            log_probabilities.append(log_probs_x)

        # Convert log probabilities back to normal scale
        probabilities = np.exp(log_probabilities - np.max(log_probabilities, axis=1, keepdims=True))
        # Normalize to get actual probabilities
        return probabilities / np.sum(probabilities, axis=1, keepdims=True)
    
    def predict_proba(self, X):
        """
        Return probability estimates for the test vector X.

        Args:
        X (np.ndarray): Test data of shape (n_samples, n_features).

        Returns:
        probabilities (np.ndarray): Probability of the sample for each class in the model.
        """
        X_discrete = np.array([np.digitize(X[:, j], bins=self.bin_edges[j][1:-1]) for j in range(X.shape[1])]).T
        log_probabilities = []

        for x in X_discrete:
            log_probs_x = []
            for class_val in self.classes:
                # Calculate log probabilities to avoid underflow
                log_prob_x_class = np.log(self.class_priors[class_val])
                for j, bin_idx in enumerate(x):
                    # Avoiding log(0) by adding epsilon
                    prob = self.feature_probs[class_val][j][bin_idx]
                    log_prob_x_class += np.log(max(prob, self.epsilon))
                log_probs_x.append(log_prob_x_class)
            log_probabilities.append(log_probs_x)

        # Convert log probabilities back to normal scale
        probabilities = np.exp(log_probabilities - np.max(log_probabilities, axis=1, keepdims=True))
        # Normalize to get actual probabilities
        probabilities = probabilities / np.sum(probabilities, axis=1, keepdims=True)

        return probabilities
    
def convert_voting_symbols(value):
    if value == '+':
        return 1  # Yea votes
    elif value == '-':
        return -1  # Nay votes
    elif value == '0':
        return 0  # Abstain
    else:
        # If there is another value, we keep it as it is.
        return value
    
# Identify and encode categorical features manually
def encode_categorical(array):
    # Identify unique categories
    categories = np.unique(array)
    encoding = {category: idx for idx, category in enumerate(categories)}
    # Encode the categorical features
    encoded_array = np.vectorize(encoding.get)(array)
    return encoded_array, encoding

# Function to one-hot encode a single column
def one_hot_encode(column):
    unique_values = np.unique(column)
    one_hot_encoded = np.zeros((column.size, unique_values.size))
    for i, unique in enumerate(unique_values):
        one_hot_encoded[:, i] = (column == unique).astype(float)
    return one_hot_encoded

# Load and preprocess data function
def load_data(filepath):
    data_df = pd.read_csv(filepath, header=None, sep=',')

    # Remove the first column (assuming it's an identifier)
    data_df.drop(columns=data_df.columns[0], inplace=True)

    # Convert '+' and '-' to numerical values for voting data
    if 'voting' in filepath:
        # Apply 'convert_voting_symbols' to each element in the DataFrame
        data_df = data_df.apply(lambda col: col.map(convert_voting_symbols))

    # If the file is spam.data, encode categorical variables
    if 'spam' in filepath:
        # Identify columns with string-type categorical data and apply encoding
        categorical_features_indices = [idx for idx, col in enumerate(data_df.columns) if data_df[col].dtype == 'object']
        for col_index in categorical_features_indices:
            encoded_column, encoding = encode_categorical(data_df.iloc[:, col_index])
            data_df.iloc[:, col_index] = encoded_column

            # Check if one-hot encoding is needed (based on number of unique values)
            if len(encoding) > 2:  # More than 2 unique values, one-hot encode
                one_hot = one_hot_encode(encoded_column)
                # Drop the original column and add the one-hot encoded columns
                data_df = data_df.drop(col_index, axis=1)
                for i, unique in enumerate(encoding):
                    data_df.insert(col_index + i, f'{col_index}_{unique}', one_hot[:, i])

    # Separate features and labels
    X = data_df.iloc[:, :-1].values
    y = data_df.iloc[:, -1].values

    # Convert all data to float, except for labels which should be integers
    X = X.astype(float)
    y = y.astype(int)

    return X, y

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Naive Bayes Classifier')
    parser.add_argument('data_path', type=str, help='Path to the data file')
    parser.add_argument('--no-cv', action='store_true', help='Disable cross-validation')
    parser.add_argument('--num-bins', type=int, default=10, help='Number of bins for discretizing continuous features')
    parser.add_argument('--m-estimate', type=float, default=1.0, help='Value of m for m-estimate smoothing')
    return parser.parse_args()

# Main function to run the Naive Bayes algorithm
def main(args):
    X, y = load_data(args.data_path)
    if args.no_cv:
        # If no cross-validation, fit the model on the entire dataset and predict
        train_size = int(0.8 * X.shape[0])  
        X_train, X_test = X[:train_size], X[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]
        
        # Fit the model on the training set
        model = NaiveBayesClassifier(args.num_bins, args.m_estimate)
        model.fit(X_train, y_train)
        
        # Predict on the test set
        predictions = model.predict(X_test)
        prob_predictions = model.predict_proba(X_test)
        
        # Calculate and print the metrics
        acc = accuracy(y_test, predictions)
        prec = precision(y_test, predictions)
        rec = recall(y_test, predictions)
        auc_score = auc(y_test, prob_predictions[:, 1])  
        
        print("No cross-validation performed. Model trained on training set and evaluated on test set.")
        print(f"Accuracy: {acc}")
        print(f"Precision: {prec}")
        print(f"Recall: {rec}")
        print(f"Area under ROC: {auc_score}")
    else:
        # Stratified cross-validation
        cv_results = cv_split(X, y, folds=5, stratified=True)
        accuracies, precisions, recalls, aucs = [], [], [], []
        # Training and testing on each fold
        for fold, (X_train, y_train, X_test, y_test) in enumerate(cv_results):
            model = NaiveBayesClassifier(args.num_bins, args.m_estimate)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            prob_predictions = model.predict_proba(X_test)
            accuracies.append(accuracy(y_test, predictions))
            precisions.append(precision(y_test, predictions))
            recalls.append(recall(y_test, predictions))
            aucs.append(auc(y_test, prob_predictions[:, 1])) 
        print("Cross-validation performed. Metrics averaged over folds.")
        print(f"Accuracy: {np.mean(accuracies)} ± {np.std(accuracies)}")
        print(f"Precision: {np.mean(precisions)} ± {np.std(precisions)}")
        print(f"Recall: {np.mean(recalls)} ± {np.std(recalls)}")
        print(f"Area under ROC: {np.mean(aucs)}")

if __name__ == '__main__':
    args = parse_arguments()
    main(args)
