Recap:
- A learning system is specified by a given, *task* *example* and a *performance measure*.
- What are the two phases of learning? What happens in these phases?
	- "Learning" or "Training" phase
		- *Reason* about the examples E
		- Formulate a *concept* that does well w.r.t P on E
		- Could also use any *prior knowledge*
	- "Evaluation" or "Testing" phase
		- Use learned concept on future, novel examples
- What are online and offline learning?
	- *Batch/Offline* Learning: one learning phase, with a large set of examples, followed by a testing phase
	- *Online* Learning: Examples arrive one at a time (or in small groups); learning and evaluation phases are iterated
- Every ML system must reason from *specific examples* to the *general
case*. This is called *inductive generalization*.
- The system is looking for the *target concept*, which is the *unknown underlying concept that solves the learning task*
- To find this the system searches a *hypothesis space*.
- All possible hypotheses can/cannot be considered. Why?
- This is called _______.
- What is the “inductive bias” of a learning algorithm?
	- The set of assumptions used by a learning system to restrict its hypothesis space
	- The more assumptions made, the "stronger" the bias
	- Can quantify this (later)

*Supervised Learning:* 
- Examples $E$ are *annotated with target concept's output by a teacher/oracle*
- Learning system must find a concept that matches annotations ($P$)
- Example: learn to recognize animals


Other Learning Paradigms

• Unsupervised Learning  
• Semi-supervisedLearning  
• ActiveLearning  
• Transductive Learning  
• TransferLearning  
• StructuredPrediction  
• ReinforcementLearning  
• Preference Learning (Ranking) • “Few-shot”learning

*Example Representation*
- What is the *internal representation* of an example in a learning system?
- Representation choice affects reasoning and the choice of hypothesis space, and the cost of learning

Feature Vector Representation
- examples are *attribute-value pairs* (note = "feature" == "attribute")
- Number of attributes are fixed 
- Can be written as an $n$-by-$m$ matrix
![[Screen Shot 2023-09-07 at 10.18.43 AM.png]]

Types of Features
- Discrete, Nominal
- Continuous
- Discrete, Ordered
- Hierarchical 
- Color∈(red,blue, green)

*Feature Space:* 
- We can think of examples embedded in an $n$ dimensional vector space
![[Screen Shot 2023-09-07 at 10.24.10 AM.png]]

Because mapping is arbitrary if you change the mapping the position and the relationship between the examples change. The mapping is part of the *concept*.

Other Example Representations
- Relational representation  
- Multiple-instance representation
- Sequential representation  
- Multi-view representation

The Binary Classification Problem
- Simplest supervised learning problem
- Target concept assigns one of two labels ("$positive$" or "$negative$") to all examples -- the *class label*
- Can extend to "multi-class", "regression", "multi-label" problems
	- Look at algorithms that solve 

Example:
![[Screen Shot 2023-09-07 at 10.32.32 AM.png]]

*Features:* Denoted by $X$
*Labels:* Denoted by $Y$

Example in Feature Space
![[Screen Shot 2023-09-07 at 10.35.18 AM.png]]

- We have a collection of examples with one label the $\textcolor{blue}{blue}$ set
- We have a collection of examples with the other label the $\textcolor{red}{red}$ set

The Learning Problem:
- Given: A binary classification problem
- Do: Produce a "*classifier*" (*concept*) that assigns a label to a new example

Binary Classifier Concept Geometry
- (Union of) $N$-dimensional volume(s) in feature space (possible a disjoint collection) 

![[Screen Shot 2023-09-07 at 10.38.04 AM.png]]

The *concept* manifests as a discriminating algorithm that maps a sort of physical separation between the examples in the feature space. 

The inductive bias of the model affects the final shape of its decision boundary. 

We do not want to represent the label as on the dimensions of our feature space, during training that information is not generally available to the learning agent. 

*Decision Tree Induction* (Chapter 3, MItchell)
- A "classical" (1980's) family of machine learning algorithms for classification
- Widely used and extremely popular, available in nearly all ML toolkits

What is a Decision Tree?
- *Tree: directed acyclic graph, each node has at most one parent*
- Internal nodes (nodes that have children): *Tests on features/attributes*
- Leaves (nodes that don't have children): *Class labels* 

Example:
![[Screen Shot 2023-09-07 at 10.50.12 AM.png]]


![[Screen Shot 2023-09-07 at 10.50.41 AM.png]]

Classification with a decision tree
- Suppose we are given a tree and a new example
- Starting at the root, check each attribute test
- This identifies a path through the tree, follow this until we reach a leaf
- Assign the class label in the leaf

![[Screen Shot 2023-09-07 at 10.52.35 AM.png]]

Decision Tree Induction
- Given a set of example, produce a decision tree
- Decision tree induction works using the idea of *recursive partitioning*
	- At each step, the algorithm will *choose an attribute test*
		- If no attribute looks good, return
	- The chosen test will partition the examples into disjoint partitions
	- The algorithm will then recursively call itself on each partition until
		- A partition only has data from one class (*pure* node) OR 
		- it runs out of attributes
(Ask professor Ozguner about this algorithm)
![[Screen Shot 2023-09-07 at 11.07.47 AM.png]]

With this given set of examples we are able to partition them effectively using a tree that leaves out the attribute of "scary".

Choosing an Attribute
- Which attribute should we choose to test first?
	- Ideally, the one that is "most predictive" of the class label
		- i.e, the one that gives us the "most information" about what the label should be
- This idea is captured by the "*(Shannon) entropy*" of a random variable

Entropy of a Random Variable
- Suppose a random variable $X$ has density $p(x)$ its (Shannon) "entropy" is defined by:
$$
\begin{array}{}
H(X) = E(-log_{2}(p(X))) \\
 = -\sum\limits_{x}(p(X = x) log_2(p(X=x))
\end{array}
$$
- Note: $0log(0) = 0$
