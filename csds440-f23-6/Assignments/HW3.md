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
There is no split all info gains are 0.

Label Entropy:
$H(L) = -\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2}) = 1.0$

Attribute Entropies:

$H(L| A1) = P(A1=F)H(L|A1=F) + P(A1=T)H(L|A1=T)$

$H(L| A1) = \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) +  \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) = 1.0$


$IG(L| A1) = H(L) - H(L|A1) = 0$

$-------------------------------$

$H(L| A2) = P(A2=F)H(L|A2=F) + P(A2=T)H(L|A2=T)$

$H(L| A2) = \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) +  \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) = 1.0$


$IG(L| A2) = H(L) - H(L|A2) = 0$

$-------------------------------$

$H(L| A3) = P(A3=F)H(L|A3=F) + P(A3=T)H(L|A3=T)$

$H(L| A3) = \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) +  \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) = 1.0$


$IG(L| A3) = H(L) - H(L|A3) = 0$

$-------------------------------$

$H(L| A4) = P(A4=F)H(L|A4=F) + P(A4=T)H(L|A4=T)$

$H(L| A4) = \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) +  \frac{1}{2}(-\frac{1}{2}log_{2}(\frac{1}{2}) -\frac{1}{2}log_{2}(\frac{1}{2})) = 1.0$


$IG(L| A4) = H(L) - H(L|A4) = 0$

$-------------------------------$

There is no split possible when using probability based entropy to calculate information gain for this dataset. The information gain of all attributes is 0 so no root for the decision tree can be assigned. 


2.	Now from the same table, find another split using "weighted" information gain. In this case, instead of counting the examples for each label in the information gain calculation, add the numbers in the Weight column for each example. You can use your code/a numerical package like Matlab to do this, and just report the final result. (10 points)

Answer:
There is a split available when considering weighted entropies.

Label Weighted Entropy:
$H(L) = -\frac{112}{256}log_{2}(\frac{112}{256}) -\frac{144}{256}log_{2}(\frac{144}{256}) = 0.989$

Attribute Weighted Entropies:

$W(A1=F) = \frac{64}{256}$, $W(A1=T) = \frac{192}{256}$ 

$H(L| A1) = W(A1=F)H(L|A1=F) + W(A1=T)H(L|A1=T)$

$H(L| A1) = \frac{64}{256}(-\frac{40}{64}log_{2}(\frac{40}{64}) -\frac{24}{64}log_{2}(\frac{24}{64})) +  \frac{192}{256}(-\frac{72}{192}log_{2}(\frac{72}{192}) -\frac{120}{192}log_{2}(\frac{120}{192})) = 0.954$

$IG(L| A1) = H(L) - H(L|A1) = 0.989 - 0.954 = 0.0346$

$-------------------------------$

$W(A2=F) = \frac{64}{256}$, $W(A2=T) = \frac{192}{256}$ 

$H(L| A2) = W(A2=F)H(L|A2=F) + W(A2=T)H(L|A2=T)$

$H(L| A2) = \frac{64}{256}(-\frac{40}{64}log_{2}(\frac{40}{64}) -\frac{24}{64}log_{2}(\frac{24}{64})) +  \frac{192}{256}(-\frac{72}{192}log_{2}(\frac{72}{192}) -\frac{120}{192}log_{2}(\frac{120}{192})) = 0.954$

$IG(L| A2) = H(L) - H(L|A2) = 0.989 - 0.954 = 0.0346$

$-------------------------------$

$W(A3=F) = \frac{64}{256}$, $W(A3=T) = \frac{192}{256}$ 

$H(L| A3) = W(A3=F)H(L|A3=F) + W(A3=T)H(L|A3=T)$

$H(L| A3) = \frac{64}{256}(-\frac{40}{64}log_{2}(\frac{40}{64}) -\frac{24}{64}log_{2}(\frac{24}{64})) +  \frac{192}{256}(-\frac{72}{192}log_{2}(\frac{72}{192}) -\frac{120}{192}log_{2}(\frac{120}{192})) = 0.954$

$IG(L| A3) = H(L) - H(L|A3) = 0.989 - 0.954 = 0.0346$

$-------------------------------$

$W(A4=F) = \frac{64}{256}$, $W(A4=T) = \frac{192}{256}$ 

$H(L| A4) = W(A4=F)H(L|A4=F) + W(A4=T)H(L|A4=T)$

$H(L| A2) = \frac{64}{256}(-\frac{28}{64}log_{2}(\frac{28}{64}) -\frac{36}{64}log_{2}(\frac{36}{64})) +  \frac{192}{256}(-\frac{84}{192}log_{2}(\frac{84}{192}) -\frac{108}{192}log_{2}(\frac{108}{192})) = 0.989$

$IG(L| A2) = H(L) - H(L|A2) = 0.989 - 0.954 = 0$

$-------------------------------$

Three of the above attributes have equal information gain and one has 0. Technically our algorithm can pick any one of the three as a split. For the sake of simplicity I will say that the decision tree will have its root node split on attribute $A1$.

3.	There is a difference between the splits for Q1 and Q2. Can you explain what is happening? (10 points)

Answer:
The difference between the splits found in Q1 and Q2 is simply that in Q2 there are splits possible whereas in Q1 no split is possible. 

In Q1 we calculate splits based off of the standard entropy of each attribute. Given the specific distribution of the label and attribute values our entropies all come out to be the same value as our total label entropy. This leads to a value of 0 for the information gain of every attribute. This means we cannot choose a split when trying to find a root for our decision tree. 

In Q2 we use weighted entropies. This value takes into account the 'importance' of each example. This 'importance' value takes the place of the probability of each state in our entropy calculations. The introduction of this weight allows us to ignore the perfectly random distribution of our labels. The resulting entropies give us a non-zero Information Gain for some of our attributes which allows us to choose a split. 


4.	Restriction biases of learning algorithms prevent overfitting by restricting the hypothesis space, while preference biases prevent overfitting by preferring simpler concepts but not necessarily restricting the hypothesis space. Discuss the pros and cons of preference vs restriction biases. (10 points)

Answer:
   Learning algorithms use preference and restriction biases as two tactics to prevent overfitting, although they work differently and have advantages and disadvantages of their own. When comparing the advantages and disadvantages of preference and restriction bias together:
  
**Preference Bias vs. Restriction Bias:**

**Flexibility vs. Robustness:**

Preference Bias: Since it leaves up all possibilities, it provides greater flexibility. If needed, it can adjust and choose more intricate models.

Restriction Bias: It prevents overfitting to noise by explicitly capping the number of hypotheses the algorithm can produce, which adds resilience. If patterns are truly complicated and outside of the constrained domain, it may not be able to adjust to them.

**Computational Complexity:**
Preference Bias: can require more computing power because it may need to examine a larger space of hypotheses.

Restriction Bias: Due to the limited space, implementations are typically easier to implement and may require less computing power.

**Risk of Overfitting:**
Preference Bias: Even while it usually favours simpler models, overfitting can nevertheless occur if an overly complicated model is erroneously chosen.

Restriction Bias: If the real hypothesis, or a close approximation, is outside the confined space, there is a greater chance of underfitting.

**Adaptability to Availability of Data:**
Preference Bias: More adaptable. Preference biases have the ability to move towards more complicated models as additional data become available.

Restriction Bias: Less adaptable. The algorithm may not be able to identify complicated patterns in the data if they are not included in the narrow hypothesis space.

In conclusion, there are distinct trade-offs between preference bias and restriction bias. Preference bias is flexible and adaptive; it can select complex models but prefers simpler ones. Although restriction bias is more reliable and could be computationally efficient, underfitting is a possibility. To take use of each bias's advantages, a combination of the two could be used in a variety of real-world situations.


5.	Person X wishes to evaluate the performance of a learning algorithm on a set of $n$ examples ( $n$ large). X employs the following strategy:  Divide the $n$ examples randomly into two equal-sized disjoint sets, A and B. Then train the algorithm on A and evaluate it on B. Repeat the previous two steps for $N$ iterations ( $N$ large), then average the $N$ performance measures obtained. Is this sound empirical methodology? Explain why or why not. (10 points)

Answer: 
This methodology is generally sound. For each training and validation run, we are training a new concept off of the set A and then testing that concept on B. To make the methodology even more robust we are reshuffling the data between sets A and B for each training and validation split. This means that we are training and testing a new concept each time allowing us to grasp the performance of our training method. 

There are some possible issues that ought to be considered. The methodology described above randomly generates subsets of data for training and validation. During the generation of these subsets nothing is seemingly done to ensure that they are representative of the data in our superset. This could mean our learned concept in each test and validation run may score well, but fail to generalize when applied to data not found in sets A and B. What would be better possibly would be to partition $k$ number of equal sized subsets. Train our model on set A and then test on each of the $k$ subsets. This way, each little subset is brand new and unseen data unmixed with our training set. 


6.	Two classifiers A and B are evaluated on a sample with P positive examples and N negative examples and their ROC graphs are plotted. It is found that the ROC of A dominates that of B, i.e. for every FP rate, TP rate(A) $\geq$ TP rate(B). What is the relationship between the precision-recall graphs of A and B on the same sample? (10 points)

Answer: 
The precision-recall graph is constructed using two metrics: True Positive Rate $(TPR)$ and Precision

Y-Axis: Precision = $\frac{TP}{TP+FP}$
X-Axis: $TPR = \frac{TP}{TP+FN}$

For the ROC Graph we use $TPR$ and $FPR$
$FPR  = \frac{FP}{FP+TN}$

If for each decrease in the confidence threshold of our learning model the $TPR(A) \geq TPR(B)$ this means that the model A has a higher number of correctly predicted positive values than model B.  
This should imply that the False Positive value for model A is also less than the False Positive value for model B.
Knowing this we can say that the Precision of model A dominates that of model B: $Precision(A) \geq Precision(B)$ 


7.	Prove that an ROC graph must be monotonically increasing. (10 points)

Answer: 
An ROC curve is constructed using two metrics: True Positive Rate $(TPR$) and False Positive Rate $(FPR)$

Y-Axis: $TPR$, 
X-Axis: $FPR$

Each new point along the curve is $(TPR_{n}, FPR_{n})$.

We go from $(TPR_{n}, FPR_{n}) \rightarrow (TPR_{n+1}, FPR_{n+1})$ by decreasing the confidence threshold between examples $n$ and $n+1$ .

As the threshold decreases along the examples, instances that were previously classified as negative may now be classified as positive. 

Some of these new positives may be true: increasing $TPR$

Some of these new positives may be false: increasing $FPR$

Either case, causes the curve to move up, to the right, or both. 

The only case in which the curve moves downwards, is if $TPR$ decreased while $FPR$ increased. Given that $TPR$ only ever increases with a decreasing confidence threshold, this case is impossible. 

Therefore, the ROC curve is monotonically increasing, as it is impossible for a decrease in the confidence threshold to cause a decrease in $TPR$.



8.	Prove that the ROC graph of a random classifier that ignores attributes and guesses each class with equal probability is a diagonal line. (10 points)

Answer: 

Outputs of a random binary classifier: 

$$
\hat{Y} = \begin{bmatrix} \hat{y}_1, \\ \hat{y}_2, \\ \dots \\ \hat{y}_n \end{bmatrix} 
$$

$$P(\hat{Y}=\hat{y}) = 
\begin{cases} 
0.5 & \text{if } \ \hat{y} = 1, \\
0.5 & \text{if } \ \hat{y} = 0.
\end{cases}
$$

It is a coin flip whether $\hat{y}$, the label assigned to some example will be positive or negative. 

The two metrics that we use to construct an ROC curve are: 

True Positive Rate $(TPR$) = $\frac{TP}{TP+FN}$
False Positive Rate $(FPR)$ = $\frac{FP}{FP + TN}$

If the distribution of labels for a given set of $n$ examples is perfectly random. Both the metrics $(TPR, FPR) \rightarrow (0.5, 0.5)$

|Examples|	True Label|	Confidence|	$TPR$|	$FPR$|
|---|---|---|---|---|
|$x_{1}$|-/+|$c_{1}$|0.5|0.5|
|$x_{2}$|-/+|$c_{2} = c_{1}-\epsilon$|0.5|0.5|	
|$\vdots$|-/+|$c_{i} = c_{i-1}-\epsilon$|0.5|0.5|
|$x_{n}$|-/+|$c_{n} = c_{n-1}-\epsilon$|0.5|0.5|


$TPR$ Metric Analysis: Probability of guessing a label correctly is 0.5 therefore all true positive instances $TP = \frac{1}{2}(AllPos)$ and the rest of the positive labels will be missed, $FN = \frac{1}{2}(AllPos)$ meaning $TPR = \frac{0.5}{0.5+0.5} = 0.5$ in all possible examples

$FPR$ Metric Analysis: Probability of guessing a label correctly is 0.5 therefore all true negative instances $TN = \frac{1}{2}(AllNeg)$ and the rest of the negative labels will be missed, $FP = \frac{1}{2}(AllPos)$ meaning $FPR = \frac{0.5}{0.5+0.5} = 0.5$ in all possible examples

This gives our ROC curve a constant slope of $\frac{\frac{1}{2}}{\frac{1}{2}}= 1$
A constant slope of equal $x$ and $y$ axis growth gives us a diagonal line. 
