- One way to control overfitting is to use *dropout*. Here a *random sample* of the nodes is left out during *backpropogation*.
- It is useful to *standardize* the inputs to an ANN. When done at internal nodes this is called *batch normalization*
- Nominal features have to be encoded via *one-hot encoding* or *label encoding* when input to an ANN.
- Probabilistic classifiers are useful to determine the optimal hypothesis using *Bayesian Decision Theory*
- They also incorporate *prior knowledge* and produce *confidence* estimates.
- They can be *generative* or *discriminative*. The first models *joint probabilities of features and labels*, the second *directly models the conditional probability of a label given the features*

1. One way to control overfitting is to use *dropout*. Here a *random sample* of the nodes is left out during *backpropogation*.
**Dropout**: Dropout is a regularization technique used in neural networks to prevent overfitting. The basic idea is to randomly deactivate a subset of neurons (or nodes) in the network during training. This prevents the network from becoming overly reliant on any specific set of features, thereby enhancing its generalization capabilities.

**Random Subset**: During training, and specifically at each iteration or epoch, a random subset of the nodes in the neural network is 'dropped out' or temporarily removed from the network. The selection is random and usually involves setting a predefined probability that each node will be dropped.

**Backpropagation**: This is the process used during training of a neural network where the error is propagated backward through the network. By dropping out nodes during backpropagation, the network learns to distribute the learned information across all nodes, reducing the chance of overfitting on the training data.

2. It is useful to *standardize* the inputs to an ANN. When done at internal nodes this is called *batch normalization*
**Scale**: Scaling the inputs to a neural network is a common preprocessing step. It involves normalizing or standardizing the input data so that it has certain desirable properties, like a mean of zero and a standard deviation of one. This helps in speeding up the training process and can lead to better performance because it ensures that no single input feature dominates the learning process due to its scale.

**Batch Normalization**: This is a technique used in deep learning to standardize the inputs to a layer for each mini-batch. This helps stabilize the learning process and dramatically reduces the number of training epochs required to train deep networks. Batch normalization is applied to internal nodes (i.e., the hidden layers) of a neural network and works by normalizing the output of a previous activation layer by subtracting the batch mean and dividing by the batch standard deviation. This process also includes learnable parameters that allow the network to undo the normalization if it is beneficial for the learning process.

3. Nominal features have to be encoded via *one-hot encoding* or *label encoding* when input to an ANN.
**One-Hot Encoding**: This method involves creating a new binary (0 or 1) column for each category in the nominal feature. For instance, if a feature has three categories - say, red, blue, green - one-hot encoding would create three new columns, one for each color. A '1' in one of these columns indicates the presence of that category, while '0' indicates absence. This method is particularly useful when there is no ordinal relationship between the categories.

**Label Encoding**: In this approach, each category is assigned a unique integer. Continuing with the color example: red might be 1, blue 2, and green 3. This method is simpler and more memory-efficient than one-hot encoding, but it implies an ordinal relationship between the categories, which might not be appropriate for all nominal features. However, for neural network models, one-hot encoding is generally preferred over label encoding, as it avoids the implication of an ordinal relationship between categories.

4. Probabilistic classifiers are useful to determine the optimal hypothesis using *Bayesian Decision Theory*
**Bayesian Decision Theory**: This is a fundamental statistical approach to the problem of pattern classification. It leverages probability theory and Bayes' Theorem to predict the likelihood of different hypotheses given the observed data. In the context of probabilistic classifiers, Bayesian decision theory provides a framework for making decisions or predictions based on the probability estimates output by the classifier. It allows for the calculation of the most probable hypothesis (or class) by considering both the data evidence and the prior knowledge about the hypothesis probabilities.

5. They also incorporate *prior knowledge* and produce *confidence* estimates.
**Prior Knowledge**: Probabilistic classifiers, especially those based on Bayesian principles, incorporate prior knowledge about the data or the problem domain. This can be in the form of prior probabilities of different classes or hypotheses. The incorporation of prior knowledge is a fundamental aspect of Bayesian inference, where prior beliefs are updated with new evidence to form posterior beliefs.

**Confidence Estimates**: Probabilistic classifiers not only predict the most likely class for a given input but also provide estimates of the confidence (or probability) associated with each class prediction. These confidence estimates are valuable in many applications, especially where it's crucial to understand the uncertainty or reliability of the predictions made by the model.

6.  They can be *generative* or *discriminative*. The first models *joint probabilities of features and labels*, the second *directly models the conditional probability of a label given the features*

**Generative Models**: These models learn the joint probability distribution \( P(X, Y) \) of the features \( X \) and the labels \( Y \). They not only classify data but also can generate new instances of data. Examples include Naive Bayes and Hidden Markov Models.

**Discriminative Models**: These models directly learn the conditional probability \( P(Y | X) \) of the label \( Y \) given the features \( X \). They focus on the boundary between different classes and are generally used for classification purposes. Examples include Logistic Regression and Support Vector Machines.

