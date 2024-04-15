- Naïve Bayes factorizes the *joint* distribution as the product of *marginals*. This assumes that *features are conditionally independent given the class label*.
- To infer the label of a new example, we *calculate the posterior probability for each class and select the class with the highest probability*
- We estimate parameters for probabilistic models using *Maximum Likelihood Estimation.*
- Bayes Rule for concept learning says that the *posterior* is equal to the *likelihood* times the *prior* divided by the *evidence*
- Maximizing the LHS gives us the *maximum a posteriori* hypothesis.
- If we assume that all hypotheses have *equal probability*, we get the *maximum likelihood* hypothesis.
- To apply Maximum Likelihood Estimation, we first write down the *likelihood function*. We then optimize it with respect to the *model parameters*

1. Naïve Bayes factorizes the *joint* distribution as the product of *marginals*. This assumes that *features are conditionally independent given the class label*.

**Joint Distribution**: Naïve Bayes models the joint probability distribution of the features and the class label. In mathematical terms, if \( C \) is the class variable and \( X_1, X_2, ..., X_n \) are feature variables, the joint distribution is \( P(C, X_1, X_2, ..., X_n) \).

**Product of Marginals**: The key idea in Naïve Bayes is to simplify the computation of the joint probability by assuming that the features are conditionally independent given the class. This assumption allows the joint probability to be factorized into the product of individual probabilities (marginals), i.e., \( P(C) \times P(X_1 | C) \times P(X_2 | C) \times ... \times P(X_n | C) \).

**Features are Conditionally Independent Given the Class Label**: This assumption is the "naïve" part of Naïve Bayes. It simplifies calculations significantly but is a strong assumption that may not hold in real-world scenarios. Despite this, Naïve Bayes often performs surprisingly well in practice, even when the conditional independence assumption is violated.

2. To infer the label of a new example, we *calculate the posterior probability for each class and select the class with the highest probability*
   
**Calculate the Posterior Probability**: In probabilistic classifiers like Naïve Bayes, the first step in inferring the label of a new example is to calculate the posterior probability for each possible class label. The posterior probability is typically calculated using Bayes' Theorem. For a classification problem with classes \(C_1, C_2, ..., C_n\) and a new example with features \(X\), the posterior probability for each class \(C_i\) is computed as \(P(C_i | X)\).

**Select the Class with the Highest Probability**: After calculating these probabilities, the next step is to choose the class with the highest posterior probability as the predicted label for the new example. This is essentially a decision rule that selects the most likely class given the observed features of the example. 

This process embodies the principle of maximum a posteriori (MAP) decision rule, which is used in various classification algorithms, not just Naïve Bayes.

3. We estimate parameters for probabilistic models using *Maximum Likelihood Estimation.*

**Maximum Likelihood Estimation** (MLE) is a statistical method used to estimate the parameters of a model by finding the values that make the observed data most probable. It involves setting up a likelihood function based on the model and the data, and then adjusting the model parameters to maximize this likelihood. MLE is widely used in various fields for its efficiency and consistency, especially as the sample size grows.

4. Bayes Rule for concept learning says that the *posterior* is equal to the *likelihood* times the *prior* divided by the *evidence*
   
**Posterior**: This is the probability of the hypothesis given the data. In concept learning, it represents our updated belief about the hypothesis after observing the data.

**Likelihood**: This is the probability of the data given the hypothesis. It measures how well the hypothesis explains the observed data.

**Prior**: This represents our initial belief about the hypothesis before observing any data. It reflects what we know about the hypothesis independently of the current data.

**Evidence**: Also known as the marginal likelihood, this is the probability of observing the data under all possible hypotheses. It acts as a normalizing constant to ensure that the posterior probabilities sum up to 1.

5. Maximizing the LHS gives us the *maximum a posteriori* hypothesis.

"Maximizing the LHS gives us the **most probable** hypothesis."

In the context of statistical learning or Bayesian inference, "LHS" usually refers to the left-hand side of a mathematical equation or formula, such as Bayes' Theorem. When applied to concept learning or hypothesis testing, maximizing the left-hand side of Bayes' Theorem (which represents the posterior probability) means finding the hypothesis that is most consistent with the observed data and the prior knowledge. This is generally referred to as the "most probable" hypothesis given the data and prior beliefs.

6. If we assume that all hypotheses have *equal probability*, we get the *maximum likelihood* hypothesis.

**Equal Probability**: This assumption implies that, prior to observing any data, each hypothesis is considered equally likely. In Bayesian terms, this means assigning a uniform prior to all hypotheses.

**Maximum Likelihood Hypothesis**: When all hypotheses are assumed to have equal prior probability, the focus shifts to finding the hypothesis that maximizes the likelihood of the observed data. This is known as the maximum likelihood hypothesis, which is the one that best explains the data under the assumption of equal priors for all hypotheses. In practice, this approach often involves choosing the hypothesis under which the observed data is most probable.

7. To apply Maximum Likelihood Estimation, we first write down the *likelihood function*. We then optimize it with respect to the *model parameters*

**Likelihood Function**: This is a function that expresses the probability of the observed data as a function of the parameters of the model. It's the core of Maximum Likelihood Estimation, capturing how likely the observed data is under different parameter values.

**Model Parameters**: These are the variables in the model that we seek to estimate. Optimizing the likelihood function with respect to these parameters means finding the values of these parameters that maximize the likelihood of observing the given data. This process typically involves differentiating the likelihood function with respect to the parameters and finding where this derivative equals zero (a process known as finding the critical points).
