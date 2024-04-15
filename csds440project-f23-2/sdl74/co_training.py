import sklearn
import numpy as np

class CoTrain(object):
    def __init__(self, models):
        self.type = 'co train'
        self.model = models

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

        # number of datapoints added last iteration
        diff = 1

        # training loop
        while diff > 0 and len(unlabeled_X) > 0:
            # stores the predictions for each model
            predictions = np.zeros((len(self.model), len(unlabeled_X)))

            # train all models with labeled data then predict for unlabeled examples
            for i in range(len(self.model)):
                # train model
                self.model[i].fit(train_X, train_y)

                # predict unlabeled data
                predictions[i] = self.model[i].predict(unlabeled_X)

            # if x number of classifiers agree, add the pseudo-label point to the other classifiers
            # this specific implementation only adds unlabeled points when two classifiers agree and the third disagrees
            counts = np.sum(predictions, axis=0)

            to_add_negative = counts == 0
            to_add_positive = counts == len(self.model)
            to_delete = np.logical_or(to_add_negative, to_add_positive)

            # add points to labeled dataset
            new_X = unlabeled_X[to_add_negative]
            new_y = np.zeros(len(new_X))
            train_X = np.concatenate((train_X, new_X))
            train_y = np.concatenate((train_y, new_y))

            new_X = unlabeled_X[to_add_positive]
            new_y = np.ones(len(new_X))
            train_X = np.concatenate((train_X, new_X))
            train_y = np.concatenate((train_y, new_y))

            unlabeled_X = np.delete(unlabeled_X, to_delete, axis=0)  # remove points from unlabeled dataset

            # record how many points were added
            diff = np.sum(to_delete * 1)

    def predict(self, X: np.ndarray):
        # stores the predictions for each model
        predictions = np.zeros((len(self.model), len(X)))

        # have each classifier individually predict the labels
        for i in range(len(self.model)):
            # predict unlabeled data
            predictions[i] = self.model[i].predict(X)

        # take an average of all the predictions, if the average > 0.5, then guess positive!
        predictions = np.average(predictions, axis=0)

        return (predictions > 0.5) * 1
