import sklearn
import numpy as np


class SelfTrain(object):
    def __init__(self, model, k_highest=10, threshold=0.90, criterion='threshold'):
        self.type = 'self train'
        self.model = model
        self.k_highest = k_highest  # will select the k best examples in the dataset to give pseudo-labels each iteration
        self.threshold = threshold  # will select all datapoints with confidence above this threshold to give pseudo-labels
        self.criterion = criterion

    # train the model with examples X and labels y
    # as this is semi-supervised learning, examples with no label should have corresponding element in y be -1
    def fit(self, X: np.ndarray, y: np.ndarray):
        # sort the examples into labeled and unlabeled
        mask = y != -1
        train_X = X[mask]
        train_y = y[mask]

        train_y = train_y.astype('int')  # the internet says this will fix my problem

        unlabeled_X = X[~mask]

        # make sure there's at least one labeled example
        if len(train_y) == 0:
            raise Exception("The model needs at least one labeled datapoint to begin training")

        # the number of unlabeled points that were given pseudo-labels last iteration (initialized to 1 bc a termination condition is no points being added)
        diff = 1

        # training loop
        while len(unlabeled_X) > 0 and diff != 0:
            # if there aren't enough points to add in next iteration then break
            if self.criterion != 'threshold' and len(unlabeled_X) > self.k_highest:
                break

            # train the model
            self.model.fit(train_X, train_y)

            # predict confidence for each unlabeled example
            predicted_y = self.model.predict_proba(unlabeled_X)

            # convert to overall confidence (rather than a different confidence for each label)
            confidence = predicted_y.max(axis=1)

            # get the k most confident points
            if self.criterion == 'threshold':
                to_label = confidence > self.threshold
            else:
                to_label = np.argpartition(confidence, self.k_highest)[-self.k_highest:]

            diff = np.sum(to_label)

            # add pseudo labels to dataset
            new_X = unlabeled_X[to_label]
            new_y = (predicted_y[to_label][:, 1] > 0.5) * 1

            train_X = np.concatenate((train_X, new_X))
            train_y = np.concatenate((train_y, new_y))

            # remove those examples from unlabeled dataset
            unlabeled_X = np.delete(unlabeled_X, to_label, axis=0)

    def predict(self, X):
        return self.model.predict(X)
