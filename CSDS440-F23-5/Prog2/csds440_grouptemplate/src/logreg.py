import sys
import scipy
import argparse
import numpy as np
import pandas as pd
from scipy.special import expit
from util import cv_split, accuracy, precision, recall, roc_curve_pairs, auc
# Set the random seed for repeatability
np.random.seed(12345)
    
class LogisticRegression:
    # Constructor for the LogisticRegression class.
    def __init__(self, learning_rate=0.01, num_iterations=1000, lambda_reg=0.1):
        # learning_rate: The step size used in gradient descent.
        # num_iterations: The number of iterations for training the model.
        # lambda_reg: The regularization strength, used in L2 regularization.
        # weights and bias are initialized to None, will be set in the fit method.
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.lambda_reg = lambda_reg
        self.weights = None
        self.bias = None

    # Sigmoid function to map predictions to probabilities.
    def sigmoid(self, z):
        # Using scipy's expit function for numerical stability.
        return expit(z)

    # Compute the cost (loss) with L2 regularization.
    def compute_cost(self, X, y):
        # Number of training examples.
        m = X.shape[0]
        # Predicted probabilities.
        h = self.sigmoid(np.dot(X, self.weights) + self.bias)
        # Logistic loss calculation.
        cost = (-1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
        # L2 regularization term.
        regularization = (self.lambda_reg / (2 * m)) * np.sum(np.square(self.weights))
        # Total cost.
        return cost + regularization

    # Perform a gradient descent step to update weights and bias.
    def gradient_descent_step(self, X, y):
        # Number of training examples.
        m = X.shape[0]
        # Predicted probabilities.
        h = self.sigmoid(np.dot(X, self.weights) + self.bias)
        # Gradient of the loss w.r.t. weights.
        dw = (1 / m) * np.dot(X.T, (h - y)) + (self.lambda_reg / m) * self.weights
        # Gradient of the loss w.r.t. bias.
        db = (1 / m) * np.sum(h - y)
        # Update weights and bias.
        self.weights -= self.learning_rate * dw
        self.bias -= self.learning_rate * db

    # Fit the logistic regression model to the training data.
    def fit(self, X, y):
        # Initialize weights and bias to zeros.
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        # Perform gradient descent for the specified number of iterations.
        for _ in range(self.num_iterations):
            self.gradient_descent_step(X, y)

    # Predict the probability of the positive class for each instance in X.
    def predict_proba(self, X):
        # Compute the probabilities.
        proba = self.sigmoid(np.dot(X, self.weights) + self.bias)
        # Return probabilities for both classes.
        return np.column_stack((1-proba, proba))

    # Predict the class label for each instance in X.
    def predict(self, X):
        # Classify as 1 if the probability of the positive class is >= 0.5, else 0.
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)
    
    

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
    parser = argparse.ArgumentParser(description='Logistic Regression Classifier')
    parser.add_argument('data_path', type=str, help='Path to the data file')
    parser.add_argument('--no-cv', action='store_true', help='Disable cross-validation')
    parser.add_argument('--lambda-reg', type=float, default=0.0, help='Regularization strength')
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
        model = LogisticRegression(lambda_reg = args.lambda_reg)
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
        for fold, (X_train, y_train, X_test, y_test) in enumerate(cv_results):
            model = LogisticRegression(lambda_reg = args.lambda_reg)
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

