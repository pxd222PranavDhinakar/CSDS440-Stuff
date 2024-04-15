# CSDS440 Written Homework 3
**Instructions:** Each question is worth 10 points unless otherwise stated. Write your answers below the question. Each answer should be formatted so it renders properly on github. **Answers that do not render properly may not be graded.** Please comment the last commit with "FINAL COMMIT" and **enter the final commit ID in canvas by the due date.** 

When working as a group, only one answer to each question is needed unless otherwise specified. Each person in each group must commit and push their own work. **You will not get credit for work committed/pushed by someone else even if done by you.** Commits should be clearly associated with your name or CWRU ID (abc123). Each person is expected to do an approximately equal share of the work, as shown by the git logs. **If we do not see evidence of equal contribution from the logs for someone, their individual grade will be reduced.** 


Names and github IDs (if your github ID is not your name or Case ID):


1.	Consider the following table of examples over Boolean attributes, annotated with the target concept's label. Ignore the "Weight" column and use information gain to find the first split in a decision tree (remember that ID3 stops if there is no information gain). You can use your code/a numerical package like Matlab to do this, and just report the final result.(10 points)

|A1|	A2|	A3|	A4|	Label|	Weight|
|---|---|---|---|---|---|
|F|	F|	F|	F|	0	|1/256|
|F	|F	|F	|T|	0	|3/256|
|F	|F	|T	|F	|1	|3/256|
|F	|F	|T	|T	|1	|9/256|
|F	|T	|F	|F	|1	|3/256|
|F	|T	|F	|T	|1	|9/256|
|F	|T	|T	|F	|0	|9/256|
|F	|T	|T	|T	|0	|27/256|
|T	|F	|F	|F	|1	|3/256|
|T	|F	|F	|T	|1	|9/256|
|T	|F	|T	|F	|0	|9/256|
|T	|F	|T	|T	|0	|27/256|
|T	|T	|F	|F	|0	|9/256|
|T	|T	|F	|T	|0	|27/256|
|T	|T	|T	|F	|1	|27/256|
|T	|T	|T	|T	|1	|81/256|

Answer:

Information gain from each attribue:

$'A1': 0.0, 'A2': 0.0, 'A3': 0.0, 'A4': 0.0$

After calculation, the information gains from each attribute are all $0s$. This dataset is perfectly even distributed, so neither of the attributes will bring any information gain after spliting the tree. If we have to choose, we can use the first attribute $'A1'$ as our first split.

2.	Now from the same table, find another split using "weighted" information gain. In this case, instead of counting the examples for each label in the information gain calculation, add the numbers in the Weight column for each example. You can use your code/a numerical package like Matlab to do this, and just report the final result. (10 points)

Answer:

Information gain from each attribue after considering the weights:

$'A1': 0.04557, 'A2': 0.04557, 'A3': 0.04557, 'A4': 0.01130$

The best attribute to split on is: $'A1'$

3.	There is a difference between the splits for Q1 and Q2. Can you explain what is happening? (10 points)

Answer:

Without Weights(Q1):

Every data point is treated equally. The entropy and information gain are computed based only on the distribution of labels of whole dataset and subsets(after partitioning). In our case, the labels are perfectly and evenly distributed, so we have no information gain by using the ID3 algorithm. 

With Weights(Q2):

After considering the weights, some data are more important or contributable to dataset based on their weights. When we calculate the information gain, the data with higher weights have a larger impact on the calculations. 

That is, the presence of weights can arise bias or imbalance in the decision tree. If some data points have large weights, the algorithm tends to fit (or even overfit) to those data points with larger weights. 

4.	Restriction biases of learning algorithms prevent overfitting by restricting the hypothesis space, while preference biases prevent overfitting by preferring simpler concepts but not necessarily restricting the hypothesis space. Discuss the pros and cons of preference vs restriction biases. (10 points)

Answer:

**Preference Biases:**

Pros:

(1) Simpler rule: Preference Biases tends to choose the simpler hypotheses, it means the ability to solve and find the concept quickly because it requires less computation. Also, if we are given two explanations for an event, the simpler one is always better(if the outputs are quite same).

(2) Flexibility: Since we have no constraints on specific hypotheses, we can consider a wide variety of them. If the true hypothese is complex, we will not omit this possibilty.

(3) Avoid omitting the true hypothesis: As we mentioned in (2), this will not exclude the true hypothesis, and allowing for potential adjustments if more complex/specific models are needed.

Cons:

(1) Intense Computation: Since no hypothese is excluded, this method will take more time and computation to consider the wide open hypotheses space. 

(2) Potential Overfitting: Since we have no constraints on the hypotheses space, it is easily to be overfitting. This method may start exploring complex hypotheses sfter considering the simpler ones if they don't work well on performance. 

**Restriction Biases:**

Pros:

(1) Efficiency: Due to the constraints on the hypotheses space, we are narrowring down the hypotheses space. The learning will be faster as the possibilities are few to consider. 

(2) Reduces Overfitting: By constraining the hypotheses space, we also reduce the potential of overfitting because we may discard those over-complex models. 

Cons:

(1) Loss of Potential True Solutions: The risk of excluding the real solution exists. 

(2) Risk of Underfitting: the real concept may be complex, but due to a severe restriction, it results in a underfitting problem. 

(3) Requires Empirical Knowledge: The experts must be experienced enough to come up with a proper set restrictions on hypotheses space, otherwise, it leads to a poor model performance. 

**Conclusion:**

Preference biases lean towards simpler solutions, allowing quick conceptualization and broad flexibility, may demand more computational resources and pose a risk of overfitting in expansive hypothesis spaces. Restriction biases prioritize efficiency by narrowing the range of potential solutions. The choice between the two hinges on the specific requirements of a problem.

5.	Person X wishes to evaluate the performance of a learning algorithm on a set of $n$ examples ( $n$ large). X employs the following strategy:  Divide the $n$ examples randomly into two equal-sized disjoint sets, A and B. Then train the algorithm on A and evaluate it on B. Repeat the previous two steps for $N$ iterations ( $N$ large), then average the $N$ performance measures obtained. Is this sound empirical methodology? Explain why or why not. (10 points)

Answer: 

Apparently, X's model has some clear advantages, such as: easy to understand and implement, aslo more efficient especially when $N$ and $n$ are large.

However, compared to its disadvantages, we don't think this is a good method of learning (at least under some circumstances). 

(1) Missing information: 

Even though the data is selected randomly everytime. But the partitions of A and B may result in two possible consequences: (a) some information is missing (we only learn on half of the data each time), or (b) some information is repteatedly learned(the patition of the data may contain only one feature, and we are not learning anything new). This strategy may yield very bad performance when our samples are unbalanced or skewed. 

(2) Randomness Resulting Unstableness: 

Since the data is randomly chosen everytime, the performance may vary greatly on evaluation results. It makes hard for us to compare the learned models without an invariant. 

(3) Wasting Resources: 

As we mentioned in (1), only one half of the data is used to learn the models, meaning that the model doesn't make full use of available data.

It looks like deploying a k-cross-validation. But in k-fold cross-validation, each subset is used as a test set once, and we are making full use of avaliable data.

6.	Two classifiers A and B are evaluated on a sample with P positive examples and N negative examples and their ROC graphs are plotted. It is found that the ROC of A dominates that of B, i.e. for every FP rate, TP rate(A) $\geq$ TP rate(B). What is the relationship between the precision-recall graphs of A and B on the same sample? (10 points)

Answer: 

$TPR = Recall = \frac {TP}{TP+FN}$

$FPR = \frac {FP}{FP+TN}$

$Precision = \frac {TP}{TP+FP}$

Since the ROC of A dominates that of B, we can also conclude that: for every TP rate, FP rate(A) $\leq$ FP rate(B). 

So we have, FP(A) $\leq$ FP(B) (Given the same TN).

In the precision-recall graph, the precision is negatively correlated with FP, that is we have Precison(A) > Precision(B).

So for every recall, Precison(A) > Precision(B). A dominates B as well in the precision-recall graph.

7.	Prove that an ROC graph must be monotonically increasing. (10 points)

Answer:

In the ROC graph, 

x-axis: FPR(False Positive Rate)

y-axis: TPR(True Positive Rate)

$TPR = \frac {TP}{TP+FN}$

$FPR = \frac {FP}{FP+TN}$

(1) As we decrease the threshold, more samples will be classified as positive. This implies both $TP$ and $FP$ can increase, thus $TPR$ and $FPR$ increase. 

(2) Let's consider two threshold $t_1 > t_2$.

Suppose the score $a_1$ for a negative instance at $t_1$ is greater than the score $a_2$ for a positive instance at $t_2$. Then at threshold $t_1$, both instances are classified as negative. TPR and FPR both decrease as we move from $t_2$ up to $t_2$.

If we goes down the threshold $t_2$, then both instances are classified as positive. TPR and FPR both increase as we move from $t_1$ down to $t_2$.

(3) As we talked in (2), both $TPR$ and $FPR$ are monotonically decreasing funtions of threshold. It's impossible for $TPR$ and $FPR$ go different directions. 

(4) Even if as we decrease the threshold, the $TPR$ may remains unchanged for a particular interval, $FPR$ would increase(because the FP may increase), or if $FPR$ remains constant, $TPR$ would increase.

Thus, as we decrease the threshold, either TPR will increase, FPR will increase, or both will increase. We can conclude that an ROC graph must be monotonically increasing. It cannot move downwards or towards the left at any point(meaning that $TPR$ remains unchaged but $FPR$ decreases).



8.	Prove that the ROC graph of a random classifier that ignores attributes and guesses each class with equal probability is a diagonal line. (10 points)

Answer: 

Since it is a random classifier, the probability of classifier guessing an instance as positive given it is indeed positive, $Prob(TP) = 0.5$.

Similarly, $Prob(FP) = 0.5$.

$TPR = \frac {TP}{TP+FN} = 0.5$ because $FN$ is also $0.5$(the guessing is binary, either true or flase with same probability).

Similarly, $FPR = \frac {FP}{FP+TN} = 0.5$

As we change the threshold for our random classifier, the probabilities of guessing an instance as positive or negative will not change, still $0.5/0.5$, since the guessing remains completely random.

That is, for each threshold, we always have point (0.5,0.5) on our ROC graph. After aggregating these pairs of identical points, it yields a diagonal line.  
