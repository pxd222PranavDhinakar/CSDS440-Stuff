- We may not use Maximum Likelihood Estimation in generative models because *it can lead to overfitting*
- For Naive Bayes, an alternative is to use *Laplace Smoothing*. Here we add *1* to the numerator and *the number of classes* to the denominator. 
- Continuous features can be modeled in Naïve Bayes using *Gaussian* distributions. 
- Naïve Bayes produces a *linear* decision boundary under a *log* transform.
- A discriminative learning algorithm is *Logistic Regression*. It models the *log odds* as a *linear function*. 
- How do we classify a new example with Logistic Regression?
- To estimate parameters we optimize the *conditional log likelihood*. This has no analytical solution, so we solve with *gradent descent* or variants. We can add a *complexity penalty*, in which case we optimize the *negatie log likellihood*.
- LR produces a linear decision boundary. However it is different from naïve Bayes because _____.
- In a generative-discriminative pair, the _____ approach generally converges faster, however the ____ approach generally has a better asymptote.

1. 
**Overfitting in Maximum Likelihood Estimation**: Maximum Likelihood Estimation (MLE) can lead to overfitting, particularly in scenarios where the dataset is small or has sparse features. Overfitting occurs when the model learns the training data too well, including its noise and outliers, which can result in poor generalization to new, unseen data.
    
**Laplace Smoothing**: This is a technique used to smooth categorical data, particularly effective in the Naive Bayes algorithm. It's used to address the issue of zero probability in the dataset (for instance, when a particular class or feature value does not appear in the sample). This is crucial because Naive Bayes relies on calculating probabilities, and having a zero probability for a class-feature combination can skew the results.

**Adding 1 to the Numerator**: In Laplace Smoothing, adding 1 to the count of each class-feature combination in the numerator ensures that no probability is zero.
    
**Adding the Number of Classes to the Denominator**: This adjustment keeps the probabilities normalized. By adding the total number of unique classes (or categories) to the denominator, the sum of the probabilities remains equal to 1, maintaining the integrity of the probability distribution. This is particularly important in multi-class classification problems where you have more than two classes.

2. 
**Gaussian Distributions for Continuous Features**: In Naïve Bayes, when dealing with continuous data, a common approach is to assume that the features follow Gaussian (or normal) distributions. This is because a Gaussian distribution is defined by its mean and variance, making it relatively simple to estimate these parameters from the training data. By assuming a Gaussian distribution, each feature is modeled using the Gaussian probability density function, which is characterized by the mean and standard deviation of the feature values in each class.
    
**Linear Decision Boundary under Log Transform**: Naïve Bayes, despite its simplicity, can produce effective classification results. When the logarithm of the probabilities is considered (which is a common practice to avoid numerical underflow), the decision boundary of Naïve Bayes becomes linear. This is because taking the logarithm of the product of probabilities (as done in Naïve Bayes) turns it into a sum, which results in a linear function with respect to the features. However, it's important to note that this linearity is in the log space, and the actual decision boundary in the original feature space might not be linear.

3.
The blanks in your statement can be filled as follows:

"A discriminative learning algorithm is **Logistic Regression**. It models the **log odds** as a **linear function**."

Explanation:

**Logistic Regression**: This is a type of discriminative learning algorithm. Discriminative models, like logistic regression, focus on modeling the boundary between classes rather than modeling the distribution of each class (which is what generative models do). Logistic regression is particularly used for binary classification tasks, although it can be extended to multiclass problems.

**Log Odds as a Linear Function**: In logistic regression, the relationship between the input features and the probability of the outcome is modeled through the logit function, which is the log of odds. The logit (log odds) is expressed as a linear combination of the input features. Mathematically, if \( p \) is the probability of the positive class, the logit is \( \log\left(\frac{p}{1-p}\right) \), and it is modeled as a linear function of the features: \( \log\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n \), where \( \beta_0, \beta_1, ..., \beta_n \) are the model parameters and \( x_1, x_2, ..., x_n \) are the input features.

4.
**Conditional Log Likelihood**: In Logistic Regression (LR), the conditional log likelihood is used for parameter estimation. This likelihood measures how well the model predicts the actual class labels given the predictors. The 'conditional' aspect refers to the fact that the likelihood of the outcomes is conditioned on the input features.
    
**No Analytical Solution**: The optimization problem for maximizing the conditional log likelihood does not have a closed-form solution, so numerical methods are necessary.
    
**Gradient Descent or Variants**: To find the model parameters that maximize the conditional log likelihood, algorithms like gradient descent are employed. These iterative methods update the parameters gradually to increase the log likelihood of the observed data under the model.

**Complexity Penalty**: The term "complexity penalty" in this context likely refers to a regularization term added to the optimization objective in logistic regression. It's a way to penalize more complex models (typically those with larger or more coefficients) to avoid overfitting.
    
**Negative Log Likelihood**: With the inclusion of a complexity penalty, the objective becomes maximizing the conditional log likelihood minus the penalty term, which is typically framed as minimizing the negative of this quantity (since many optimization algorithms are designed to minimize rather than maximize). The complexity penalty term often takes the form of L1 or L2 regularization, which penalizes the sum of the absolute values or the sum of the squares of the model coefficients, respectively.

