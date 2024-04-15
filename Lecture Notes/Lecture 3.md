*Overview*
- In supervised learning, examples are *annotated* by an *oracle*. 
- The “feature vector” representation creates a fixed size *matrix* where the rows are *examples* and the columns are *attributes*. 
- Features can be *nominal*, *continuous*, *ordered* or *hierarchical*. 
- What is the “feature space”? 
- In the binary classification problem, the annotation is *binary*. This is called the *class label*. 
- What is the “decision boundary”? 
- In a decision tree, internal nodes are *attribute tests* and leaves are *class label*. 
- To classify a new examples we *identify a path through the tree until we reach a leaf and return the class label of the leaf*. 
- Tree induction works through *recursive partitioning*. First we choose an *attribute test* if available. This creates *disjoint partitions* from the data. We repeat until (1) *partition only has data from one class (PURE NODE)* or (2) *run out of attributes to test*.

Decision Tree Induction  
- Given a set of examples, produce a decision tree
- Decision tree induction works using the idea of recursive partitioning
- At each step, the algorithm will choose an attribute test
- If no attribute looks good, return  
- The chosen test will partition the examples into
- The algorithm will then recursively call itself on each partition until
- a partition only has data from one class (pure node) OR • it runs out of attributes


Choosing an Attribute
- Which attribute should we choose to test first?
	- Ideally, the one that is "most predictive" of the class label
		- i.e, the one that gives us the "most information" about what the label should be. 
- This idea is captures by the "*(Shannon) entropy*" of a random variable.

Entropy of a Random Variable
- Suppose a random variable $X$ has density $p(x)$ its (Shannon) "entropy" is defined by:
  $$
  \begin{align*}
  H(X) =& E(-log_{2}(p(x)))\\
=&-\sum\limits_{x}p(X=x)log_{2}(p(X=x))
\end{align*}
$$
Example
- Suppose $X$ has two values, $0$ and $1$, and pdf
	$p(0) = 0.5, p(1) = 0.5$
	- Then $H(X) = 1$
- Suppose $X$ has two values, $0$ , and $1$, and pdf
	$p(0) = 0.99, p(1) = 0.01$
	- Then $H(X) = 0.081$
- Suppose $X$ has two values, $0$ , and $1$, and pdf
	$p(0) = 0.01, p(1) = 0.99$
	- Then $H(X) = 0.081$


![[Screen Shot 2023-09-12 at 10.19.44 AM.png]]

*What is Entropy?*
- Measure of "information content" in a distribution
- Suppose we wanted to describe an r.v $X$ with $n$ values and distribution $p(X=x)$
	- Shortest lossless description takes $-log_{2}(p(x))$ bits for each $x$
	- So entropy is thee expected length of the shortest lossless description of the r.v.

What's the connection?
- Entropy measures the information content of a random variable
- Suppose we treat the class variable, $Y$, as a random variable and measure its entropy
- Then we measure its entropy after partitioning the examples with an attribute $X$ 

The Entropy Connection
- The difference will be a measure of the "information gained" about $Y$ by partitioning the examples with $X$
- So if we can choose the attribute $X$ that maximizes this "information gain", we have found what we needed

The class as a random variable
- Suppose at some point we have $N$ training examples, of which $pos$ are labeled "positive" and $neg$ are labeled "negative" ($pos+neg=N$) 
- We'll treat the class label as a Bernoulli r.v $Y$ that takes value $1$ with prob. $p^{+}=\frac{pos}{N}$ and $0$ with prob. $p^{-}=\frac{neg}{N}$
- Then $H(Y)=-p^{+}log_{2}(p^{+})-p^{-}log_{2}(p^{-})$

Information Gain
- $IG(X)$ = *reduction in entropy of the class label if the data is partitioned using $X$* 
- Suppose an attribute $X$ takes two values $1$ and $0$. After partitioning, we get the quantities $p_{X=1}^{+}, p_{X=1}^{-}, p_{X=0}^{+}, \ and \ p_{X=0}^{-}$. Then,


Information Gain continued
![[Screen Shot 2023-09-12 at 10.49.54 AM.png]]

Normal Attributes
- if $X$ has $v$ values:
  $$
  \begin{align*}
&H(Y|X=v)=-p_{X=v}^{+}log_{2}(p_{X=v}^{+})-p_{X=v}^{-}log_{2}(p_{X=v}^{-})\\
&H(Y|X)=\sum\limits_{x}p(X=v)H(Y|X=v)\\
&IG(X)=H(Y)-H(Y|X)
\end{align*}
$$
There is a problem
- If an attribute has a lot of values, IG prefers if (resulting partitions tend to be pure)
- E.g., consider an "Example-ID" attribute
![[Screen Shot 2023-09-12 at 10.57.40 AM.png]]
- This memorizes the data, so has a perfect IG score, which is an extreme example of overfitting. 

The more pure nodes, in our decision tree example, the higher amount of information or entropy we have. 


Fix: GainRatio
- Normalize IG with entropy of the attribute's distribution (computed from training data)
  $$
  \begin{align*}
GR(X)=\frac{IG(X)}{H(X)}
\end{align*}
$$
Considering the entropy of $X$ in the above example:
$$
\begin{align*}
H(X)=-\sum\limits_{x=0}^{546}\frac{1}{546}log_2(\frac{1}{546})=log_2(546)
\end{align*}
$$
For any discrete random variables the density that gives you the maximum entropy, is an equal distribution of probabilities

Highest entropy of a system with $n$ possible states, is achieved if each state is equally possible $p(N=n)=\frac{1}{n}$
$$H(N)=-\sum\limits_{n=0}^{N}\frac{1}{N}log_2(\frac{1}{N})=log_2(N)$$

Continuous Attributes
- Cannot test for equality
- Consider all boolean tests of the form $X \geq v$ (or $X \leq v$)
	- Only values of interest are those $v$ that separate adjacent training examples with different classes (why?)
- Note: in this case, the attribute cannot be removed, through the test ((attribute, value) tuple) can be


