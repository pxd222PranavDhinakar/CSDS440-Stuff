# CSDS440 Written Homework 2
**Instructions:** Each question is worth 10 points unless otherwise stated. Write your answers below the question. Each answer should be formatted so it renders properly on github. **Answers that do not render properly may not be graded.** Please comment the last commit with "FINAL COMMIT" and **enter the final commit ID in canvas by the due date.** 

When working as a group, only one answer to each question is needed unless otherwise specified. Each person in each group must commit and push their own work. **You will not get credit for work committed/pushed by someone else even if done by you.** Commits should be clearly associated with your name or CWRU ID (abc123). Each person is expected to do an approximately equal share of the work, as shown by the git logs. **If we do not see evidence of equal contribution from the logs for someone, their individual grade will be reduced.** 


1.	(i) Give an example of a nontrivial (nonconstant) Boolean function over $3$ Boolean attributes where $IG(X)$ would return zero for *all* attributes at the root. (ii) Explain the significance of this observation. 

Answer:

Suppose we have three Boolean attributes $A,B,C$, all of them can take either $1$ or $0$.

We can consider a simple logic gate Output = $A$ xor $B$ xor $C$ (XOR outputs 1(+) if two numbers are different, otherwise 0(-)).

There are $8$ Combinations of these three attributes, and we consider the correspongding outputs as below:

$A  &emsp;B  &emsp;C$     &emsp; output

$0  &emsp;0  &emsp;0$     &emsp; &emsp;-

$0  &emsp;0  &emsp;1$     &emsp; &emsp;+

$0  &emsp;1  &emsp;0$     &emsp; &emsp;+

$0  &emsp;1  &emsp;1$     &emsp; &emsp;-

$1  &emsp;0  &emsp;0$     &emsp; &emsp;+

$1  &emsp;0  &emsp;1$     &emsp; &emsp;-

$1  &emsp;1  &emsp;0$     &emsp; &emsp;-

$1  &emsp;1  &emsp;1$     &emsp; &emsp;+

As we can see, for each attribute, half of the time it is 0 and the other is 1. Everytime we split the dataset with attribute, the output is still evenly balanced, with half of them being positive and the other half being negative. The data set is perfectly balanced, it will always be a 50-50 split.

This observtion tells us that the information gain has its limitation of handling the cases when attributes themselves are interactive. 

2. Estimate how many functions satisfying Q1 (i) could exist over $n$ attributes, as a function of $n$. 

Answer:

Take above case as example: 

When we have $3$ boolean attributes, we can pick up any $2$ attributes and all $3$ attributes. 

If we have $n$ attributes. we start at picking up any $2$, then $3$, $4$ until $n$. The functions satisfy the condition should be concluded as the sum of combinations of choosing $2$ to $n$ attributes from $n$.

Numbers of functions = $$\sum_{i=2}^{n}C_{n}^{i}$$

3.	Show that for a continuous attribute $X$, the only split values we need to check to determine a split with max $IG(X)$ lie between points with different labels. (Hint: consider the following setting for $X$: there is a candidate split point $S$ in the middle of $N$ examples with the same label. To the left of $S$ are $n$ such examples. To the left of $N$, there are $L_0$ examples with label negative and the $L_1$ positive, and likewise $(M_0, M_1)$ to the right. Express the information gain of $S$ as a function of $n$. Then show that this function is maximized either when $n=0$ or $n=N$ with all else constant.) (20 points)

Answer:
![](/ImagesHW2Q3/1.jpg)
![](/ImagesHW2Q3/2.jpg)
![](/ImagesHW2Q3/3.jpg)
![](/ImagesHW2Q3/4.jpg)
![](/ImagesHW2Q3/5.jpg)
![](/ImagesHW2Q3/6.jpg)

4.	Write a program to sample a set of $N$ points from $(−1,1)^2$. Label the points using the classifier $y=sign(0.5x_1+0.5x_2)$. Generate datasets from your program and use your ID3 code from Programming 1 to learn trees on this data (there is no need to do cross validation or hold out a test set). Plot a graph where the $x$-axis is the value of $N$, over $N={50, 100, 500, 1000, 5000}$, and the $y$-axis is the depth of the tree learned by ID3. Explain your observations. (20 points)

Answer: 

![](/ImagesHW2Q4Q5/Q4_1.png)

The depth of the tree tends to increase with the size of the dataset. This is because with more data points, the decision tree has more samples from where to learn the concept, and thus the tree become deeper to classify these data points correctly. 

5.	Show the decision boundaries learned by ID3 in Q4 for $N=50$ and $N=5000$ by generating an independent test set of size 100,000, plotting all the points and coloring them according to the predicted label from the $N=50$ and $N=5000$ trees. Explain what you see relative to the true decision boundary. What does this tell you about the suitability of trees for such datasets? (20 points)

Answer:

![](/ImagesHW2Q4Q5/Q5_1.png)

![](/ImagesHW2Q4Q5/Q5_2.png)

The true decision boundary is y = -x. Because the lable is determined by $y = sign(0.5x_1 +0.5x_2)$, the boundary should be $0.5x_1 +0.5x_2 = 0$, that is, the line shown on the graph is $y = -x$. 

When $N=50$, The decision decision tree is easily to be overfitted. Because the samples are so small, and the tree is too specific to generalize to other novel cases. 

When $N=5000$, The decision boundary is closer to the true boundary, however it still creates some overfitting regions due to the nature of the tree.

Trees segment the space based on data input. For linear decision boundaries like this($y=-x$), trees might not be the best option as trees may overfit to the training data with smaller number of samples. Even with more data, it still ends up creating unnecessary complex boundaries(segments of overfitting).

6.	Under what circumstances might it be beneficial to overfit? 

Answer:

(1) Inverse Inference and Memory Assistance: When a model is trained on a sufficiently large dataset and overfits, it responds extremely accurately to the training data itself. When the data you need is within the training set but is hard to search directly or the known conditions are incomplete, you can use this model to refine the incomplete conditions to specific scenarios or locations.

Example: Even if the model's training data includes all the data available in the market to date, the stock market remains unpredictable. However, if our goal is to look back and identify recurring historical patterns, an overfitted model might be helpful.

(2) Known Feature Data: if we are quite sure the future data is almost identical to our training data, then overfitting is definitely good to us.

(3) Model Complexity Exploration: overfitting means that our model is too complex, but it also means we can learn how complex our model can be by detecting the fact that it starts overfitting. 

---
FINAL COMMIT

mxl1166
