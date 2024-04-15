import numpy as np
import random

# input: type of classifier, models, dataset, %unlabeled, output: when true, will print accuracy and precision information
# output: performance before self/co-training, performance after self/co-training

def performAnalysis(classifier, data, target, percent_unlabeled, output=True):
    # copy data so labels can later be used for scoring the model
    X = np.copy(np.asarray(data))
    y = np.copy(np.asarray(target))

    # remove labels for part of the data
    while True:
        rng = np.random.RandomState(random.randint(0, 100))
        to_hide = rng.rand(len(y)) < percent_unlabeled
        y[to_hide] = -1
        # make sure 1 and 0 occur at least once
        if 0 in y and 1 in y:
            break
        y = np.copy(np.asarray(target))

    # perform analysis of model before fitting (only training on unlabeled data)
    # copy only labeled datapoints
    mask = y != -1
    train_X = X[mask]
    train_y = y[mask]

    # train each classifier with only labeled points (supervised learning)
    if classifier.type == 'co train':
        models = classifier.model
    elif classifier.type == 'self train':
        models = [classifier.model]
    else:
        models = [classifier.model1]

    for i in models:
        i.fit(train_X, train_y)

    # get all unlabeled examples
    mask = y == -1
    test_X = X[mask]
    test_y = target[mask]

    # predict the unlabeled examples
    if classifier.type == 'co train view':
        predictions = models[0].predict(test_X)
    else:
        predictions = classifier.predict(test_X)

    # calculate and print accuracy
    matches = test_y == predictions * 1
    before_accuracy = sum(matches) / len(matches)
    # calculate precision
    positive_matches = np.dot(matches, test_y)
    before_precision = positive_matches / sum(test_y)

    # allow model to do semi-supervised learning
    classifier.fit(X, y)

    # perform analysis of model after semi-supervised learning
    predictions = classifier.predict(test_X)
    matches = test_y == predictions * 1
    after_accuracy = sum(matches) / len(matches)
    # calculate precision
    positive_matches = np.dot(matches, test_y)
    after_precision = positive_matches / sum(test_y)

    # print results
    if output:
        print("accuracy before semi-supervised training: ", before_accuracy)
        print("precision before semi-supervised training: ", before_precision)
        print("accuracy after semi-supervised training: ", after_accuracy)
        print("precision after semi-supervised training: ", after_precision)

    # return results as a tuple
    return [before_accuracy, after_accuracy, before_precision, after_precision]
