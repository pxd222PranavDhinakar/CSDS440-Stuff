*Overview*
- What is the geometry of the tree’s decision boundary? 
- Tree learners don’t need a m___ s___ representation, can represent c____ concepts, are human i_____ and easy to e___. 
- But they have trouble with features that have lots of v___, features that i___, and o_____ easily. • What is goal of learning algorithm performance evaluation? 
- Given a finite dataset, we want the training set to an algorithm to be as l____ as possible. We also want the test sets to be i___. 
- These goals are achieved by -- - -- ___ ---. 
- In this procedure, we p____ the data into f___. Each iteration we use ___ as the train set and __ as the test set. 
- What is leave one out cross validation? 
- What is stratified CV? 
- What is internal CV?

Measuring performance of ID3 Algorithm

Goal
- Want a reliable measure of *expected future performance* of the *learning algorithm* on a specific learning problem
- How to measure *future* performance?
- How to get *expectation*?

Idea
- Separate available data into sets for training and evaluation
- The examples for evaluation will be new to the earned classifier
	- Proxy for "future examples"
- Do this lots of times to get expectation

$n$-fold cross validation
- Generally, data is limited
- To learn a good concept, need training sets to be as large as possible
- For good estimates of future performance, need a number of independent test sets
- Idea: partition the available examples into "folds"

Stratified Cross Validation
- Same as cross validation, but folds are sampled so the proportions of class labels are the same in each fold and equal to the overall proportion
- Produces more stable performance estimates overall, recommended. 

Internal Cross Validation
- Can use same method to tune parameters, select features, prune trees etc.
- Do another $m$-fold c.v. within each fold
	- In this case, held out data called "validation set" or "tuning set"
	- Each fold might produce different parameter settings
		- Need a consensus procedure to identify a single setting
- Needs many examples to work well. 

