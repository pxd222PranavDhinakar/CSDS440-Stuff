import sklearn
import numpy as np
from scipy.stats import entropy
import copy

class CoTrainView(object):
    def __init__(self, model, threshold=0.9):
        self.type = 'co train view'
        self.model1 = model
        self.model2 = copy.deepcopy(model)
        self.view1 = None
        self.view2 = None
        self.threshold = threshold

    def fit(self, X: np.ndarray, y: np.ndarray):
        # sort the examples into labeled and unlabeled
        mask = y != -1
        train_X = X[mask]
        train_y = y[mask]

        train_y = train_y.astype('int')  # the internet says this will fix my problem

        # calculate the view split
        self.view1, self.view2 = self.find_split(train_X, train_y)

        unlabeled_X1 = np.flatnonzero(~mask)
        unlabeled_X2 = np.flatnonzero(~mask)
        labeled_X1 = X[mask]
        labeled_X1 = labeled_X1[:, self.view1]
        labeled_X2 = X[mask]
        labeled_X2 = labeled_X2[:, self.view2]
        labeled_y1 = train_y
        labeled_y2 = np.copy(train_y)

        # make sure there's at least one labeled example
        if len(train_y) == 0:
            raise Exception("The model needs at least one labeled datapoint to begin training")

        # number of datapoints added last iteration
        diff = 1

        # training loop
        while diff > 0 and len(unlabeled_X1) > 0 and len(unlabeled_X2) > 0:
            # train each model with labeled data
            self.model1.fit(labeled_X1, labeled_y1)
            self.model2.fit(labeled_X2, labeled_y2)

            # predict labels
            X1 = X[unlabeled_X1]
            X1 = X1[:, self.view1]
            X2 = X[unlabeled_X2]
            X2 = X2[:, self.view2]
            predict1 = self.model1.predict_proba(X1)
            predict2 = self.model2.predict_proba(X2)

            # find the most confident guesses using a threshold
            confidence1 = predict1.max(axis=1)
            confidence2 = predict2.max(axis=1)
            to_label1 = confidence1 > self.threshold
            to_label2 = confidence2 > self.threshold

            # add datapoints to labeled group of other classifier
            # retrieve pseudo-labels for the confident datapoints (1 & 2 are swapped on purpose, because confident estimates from model 1 are added to dataset 2)
            new_y2 = (predict1[to_label1][:, 1] > 0.5) * 1
            new_y1 = (predict2[to_label2][:, 1] > 0.5) * 1

            # retrieve example in view form for confident datapoints (1 & 2 are swapped on purpose, because confident estimates from model 1 are added to dataset 2)
            new_X2 = X[(unlabeled_X1[to_label1])]
            new_X2 = new_X2[:, self.view2]
            new_X1 = X[(unlabeled_X2[to_label2])]
            new_X1 = new_X1[:, self.view1]

            # actually add to labeled set
            labeled_X1 = np.concatenate((labeled_X1, new_X1))
            labeled_X2 = np.concatenate((labeled_X2, new_X2))
            labeled_y1 = np.concatenate((labeled_y1, new_y1))
            labeled_y2 = np.concatenate((labeled_y2, new_y2))

            # remove unlabeled datapoints from unlabeled set
            unlabeled_X1 = np.delete(unlabeled_X1, to_label1, axis=0)
            unlabeled_X2 = np.delete(unlabeled_X2, to_label2, axis=0)

            # record how many points were added
            diff = len(new_y1) + len(new_y2)


    def predict(self, X: np.ndarray):
        # split X by view
        X1 = X[:, self.view1]
        X2 = X[:, self.view2]

        # have each classifier predict the examples
        y1 = self.model1.predict_proba(X1)
        y2 = self.model2.predict_proba(X2)

        # sum the calculations and take the more likely classification
        predictions = np.add(y1, y2)
        return (predictions[:, 1] > 1) * 1

    # uses conditional mutual information to find a split between the features in X such that the two views of the data are as independent as possible while still retaining information about the label
    def find_split(self, X: np.ndarray, y: np.ndarray):
        num_features = len(X[0])
        # find the conditional mutual information between every pair of features
        cmi = np.zeros((num_features, num_features))  # matrix of cmi pairs
        for i in range(num_features):
            for j in range(i+1, num_features):
                cmi[i, j] = conditional_mutual_information(X[:, i], X[:, j])
                cmi[j, i] = cmi[i, j]  # don't want to have to worry about symmetry

        # create initial split
        group1 = np.asarray(range(int(num_features/2)))
        group2 = np.asarray(range(int(num_features/2), num_features))

        # iterate until local optima found
        best_cut = cut_size(cmi, group1, group2)

        # calculate the contribution every node has from each group
        # every entry in cmi will be negative if the two nodes are in different groups, but positive if they're in the same group
        for i in group2:
            cmi[:, i] = cmi[:, i] * -1
            cmi[i, :] = cmi[i, :] * -1

        # how much mutual information would change if node i was swapped to the other side
        contrib = np.sum(cmi, axis=0)

        improvement = True
        while improvement:
            improvement = False

            # loop through every node pair
            lowest_diff = 1
            diff_pair = [-1, -1]
            for v1 in group1:
                for v2 in group2:
                    # we want to find the lowest diff (if no diff is below 0, then we have found an optima)
                    diff = contrib[v1] + contrib[v2] - 2 * cmi[v1, v2]
                    if diff < 0 and diff < lowest_diff:
                        lowest_diff = diff
                        diff_pair = [v1, v2]
                        improvement = True

            # if possible swap found, swap nodes and continue
            if improvement:
                # multiply cmi for each node swapped
                v1 = diff_pair[0]
                v2 = diff_pair[1]
                cmi[v1, :] = cmi[v1, :] * -1
                cmi[:, v1] = cmi[:, v1] * -1
                cmi[v2, :] = cmi[v2, :] * -1
                cmi[:, v2] = cmi[:, v2] * -1

                # alter contrib to reflect the swap
                contrib = contrib + (2 * cmi[:, v1])
                contrib = contrib + (2 * cmi[:, v2])
                contrib[v1] = np.sum(cmi[v1])
                contrib[v2] = np.sum(cmi[v2])

                # swap elements
                group1 = np.delete(group1, np.where(group1 == v1))
                group2 = np.delete(group2, np.where(group2 == v2))
                group1 = np.append(group1, v2)
                group2 = np.append(group2, v1)
        return group1, group2


def conditional_mutual_information(x, y):
    p_xy = np.histogram2d(x, y, bins=(len(np.unique(x)), len(np.unique(y))))[0]
    p_xy /= np.sum(p_xy)
    p_x = np.histogram(x, bins=len(np.unique(x)))[0] / len(x)
    p_y = np.histogram(y, bins=len(np.unique(y)))[0] / len(y)

    p_xy[p_xy == 0] = 1e-12  # Avoid division by zero
    p_x[p_x == 0] = 1e-12
    p_y[p_y == 0] = 1e-12

    cmi = np.sum(p_xy * np.log2(p_xy / (np.outer(p_x, p_y))))

    return cmi

def cut_size(cmi, group1, group2):
    cut = 0
    for v1 in group1:
        for v2 in group2:
            cut += cmi[v1][v2]
    return cut
