import numpy as np
from sklearn.metrics.pairwise import rbf_kernel

class LocalGlobalConsistencyClassifier:
    def __init__(self, sigma=1.0, alpha=0.99):
        self.sigma = sigma
        self.alpha = alpha

    """"""
    def fit(self, X_labeled, Y_labeled, X_unlabeled):

        # combining labeled and unlabeled data
        X = np.concatenate((X_labeled, X_unlabeled), axis=0)

        # creating the affinity matrix using RBF kernel
        self.W = rbf_kernel(X, gamma=1/(2*self.sigma**2))
       # np.fill_diagonal(self.W, 0)

        # constructing a normalized matrix
        D = np.diag(np.sum(self.W, axis=1))
        D_inv_sqrt = np.linalg.inv(np.sqrt(D))
        self.S = D_inv_sqrt @ self.W @ D_inv_sqrt

        # initializing labels for unlabeled data
        Y = self.initialize_unlabeled(Y_labeled, len(X_unlabeled))

        # label propogation
        F = self.iterative_process(Y)

        self.F = F
        self.X_train = np.concatenate((X_labeled, X_unlabeled), axis=0)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, X_new):
        # Calculate affinities between new data and training data
        affinities = rbf_kernel(X_new, self.X_train, gamma=1/(2*self.sigma**2))

        # Predict labels based on weighted sum of F
        predictions = np.dot(affinities, self.F)

        # Transform predictions to probability-like scores using sigmoid function
        probabilities = self.sigmoid(predictions)

        # Threshold the probabilities to get binary labels
        predicted_labels = (probabilities > 0.5).astype(int)
        return predicted_labels

    def initialize_unlabeled(self, Y_labeled, num_unlabeled):
        # initializing labels for unlabeled data to 0 as a placeholder for unlabeled
        Y_unlabeled = np.zeros(num_unlabeled)
        return np.concatenate((Y_labeled, Y_unlabeled))

    def iterative_process(self, Y):
        F_old = Y
        F_new = np.copy(Y)
        while not self._converged(F_new, F_old):
            F_old = np.copy(F_new)
            F_new = self.alpha * np.dot(self.S, F_old) + (1 - self.alpha) * Y
        return F_new

    # checks for convergence using norm
    def _converged(self, F_new, F_old, threshold=1e-3):
        return np.linalg.norm(F_new - F_old) < threshold


