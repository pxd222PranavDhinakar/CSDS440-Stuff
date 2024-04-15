# CSDS440 Written Homework 1-Group 6
**Instructions:** Each question is worth 10 points unless otherwise stated. Write your answers below the question. Each answer should be formatted so it renders properly on github. **Answers that do not render properly may not be graded.** Please comment the last commit with "FINAL COMMIT" and **enter the final commit ID in canvas by the due date.** 

When working as a group, only one answer to each question is needed unless otherwise specified. Each person in each group must commit and push their own work. **You will not get credit for work committed/pushed by someone else even if done by you.** Commits should be clearly associated with your name or CWRU ID (abc123). Each person is expected to do an approximately equal share of the work, as shown by the git logs. **If we do not see evidence of equal contribution from the logs for someone, their individual grade will be reduced.** 

1. For three random variables A, B and C, show with a clear example that the statement “A is independent of B” does not imply the statement “A is independent of B given C.” 

Answer:

$A$ = the event that a randomly drawn card from a shuffled deck is a red card (*heart or diamond*) 

$B$ = the event that a randomly drawn card from a shuffled deck is a black card (*spades or clubs*)

$C$ = the event that a randomly drawn card from a shuffled deck is an *odd numbered* card

$P(A) = \frac{26}{52}$
$P(B) = \frac{26}{52}$
$P(C) = \frac{12}{52}$

$A$ and $B$ are independent of one another because drawing a red card does not affect the chances of the card being black. 

$P(A|C)$ = the probability of drawing a red card given the card is odd
$P(B|C)$ = the probability of drawing a black card given the card is odd

The information that the given card is odd does not help us determine whether or not the card is black or red. Therefore,

$P(A|C) = P(A)$
$P(B|C) = P(B)$

This means that $A$ and $B$ remain independent despite being given $C$.

2. Points are sampled uniformly at random from the interval $(0,1)^2$ so that they lie on the line $x+y=1$. Determine the expected squared distance between any two sampled points. 

Answer: 

Defining parametric equations for $x$ and $y$

$x+y = 1$
$Let, \ 0\leq t \leq 1$
$So \ that,$
$x(t)=t$
$y(t)=1-t$


Defining random variables for the $x$ and $y$ coordinates of the randomly selected points.

$X$: represents the $x$-coordinate of a point chosen uniformly at random from the interval $(0,1)^2$ such that it lies on the line $x+y=1$
$X \sim U[0,1]$

$Y$: represents the $y$-coordinate of a point chosen uniformly at random from the interval $(0,1)^2$ such that it lies on the line $x+y=1$ 

$Y \sim U[0,1]$,
$Y=1-X$

$Y$ is uniquely determined by the value of $X$ and is equal to $1-X$ due to the constrain $x+y=1$ 

Establishing a probability density function for the system

PDF of $X$:

$P_{X}(x) = 1 \ for \ 0\leq x \leq 1$

PDF of $Y$:

$P_{Y}(y) = 1 \ for \ 0\leq y \leq 1$

Setting up equation for squared distance between two sampled points:
Two randomly sampled points:

$(X_{1}, Y_{1}), (X_{2}, Y_{2})$

Distance formula for two randomly sampled points:

$D^{2} = (X_{2}-X_{1})^{2}+(Y_{2}-Y_{1})^{2}$ 

Calculating Expectation: 

$E[D^{2}] = \int\int_{(0,1)^{2}} D^{2}p_{X}(x)p_{Y}(y)dxdy = \frac{1}{3}$


3. For any two random variables $X$ and $Y$, the conditional expectation of $X$ given $Y=y$ is defined by $E(X|Y=y)=\sum_x p_X(x|Y=y)$ for a fixed $y$. Show that, for any three random variables $A$, $B$ and $C$, $E(A+B|C=c)=E(A|C=c)+E(B|C=c)$.


Answer: 

Recall the Linearity of Expectations:

$E(a_{1}​X_{1}​+a_{2}​X_{2}​+\dots+a_{n}​X_{n}​)=a_{1}​E(X_{1}​)+a_{2}​E(X_{2}​)+\dots+a_{n}​E(X_{n}​)$

Setting up Expectation Equation:

$E(A+B|C=c) = \sum\limits_{a,b}(a+b)P_{A+B}(a+b|C=c)$
Using the linearity of expectations we can rewrite the above equation as:
$\sum\limits_{a,b}(a \cdot P_{A+B}(a+b|C=c)+b \cdot P_{A+B}(a+b|C=c))$

Since we condition the above equation on $C=c$ and $A$ and $B$ are independent we can rewrite:

$P_{A+B}(a+b|C=c) \rightarrow P_{A}(a|C=c) \cdot P_{b}(b|C=c)$

Now our expectation equation looks like:

$\sum\limits_{a,b}(a \cdot P_{A}(a|C=c) \cdot P_{b}(b|C=c) + b \cdot P_{A}(a|C=c) \cdot P_{B}(b|C=c))$
$=(\sum\limits_{a}(a \cdot P_{A}(a|C=c)\cdot P_{B}(b|C=c))) + (\sum\limits_{b}(b \cdot P_{A}(a|C=c)\cdot P_{B}(b|C=c)))$

We can use the linearity of expectations to again, split these sums:

$= (\sum\limits_{a}(a \cdot P_{A}(a|C=c))) + (\sum\limits_{b}(b \cdot P_{B}(b|C=c)))$

The two sums above are simply the conditional expectation equations for the random variables $A$ and $B$ given $C=c$

$= E(A|C=c) + E(B|C=c)$

We have now shown that:

$E(A+B|C=c) = E(A|C=c) + E(B|C=c) \blacksquare$


4. Describe two learning tasks that might be suitable for machine learning approaches. For each task, write down the goal, a possible performance measure, what examples you might get and what a suitable hypothesis space might be. Be original---don’t write about tasks discussed in class or described in the texts. Preferably select tasks from your research area (if any). Describe any aspect of the task(s) that may not fit well with the supervised learning setting and feature vector representation we have discussed. 

Answer:
1. A suitable task for a machine learning application could be the classification of the famous Iris Dataset. In this dataset there are three classes, or species of flowers, each datapoint has five features and one label. While teaching the model, each of the five features would be provided and it would have three outputs between 0 and 1. The largest output would signify its prediction on the datapoints as that specific species of flower. Our performance measure would indicate how wrong the model's prediction is. If the model outputs a low value for species 1, and a higher value for species 2 and 3, while the correct answer is species 1, we would assign the model with a particularly low performance measure. A suitable hypothesis space would have to include all the features on which the species of the flower is dependent upon. The final concept would have to precisely distinguish between the three species based on the various possible combinations of the 5 features. 
2. Another interesting possible application for machine learning would be as a content recommendation system for users on sites like Youtube, Facebook, Netflix etcetera. The attributes to be fed to the model would be user data like, tags for content the user has 'interacted' with. The output for the model would be tags for content the model thinks the user will 'like'. A performance measure would be the relative amount of interaction the user has with the recommended content from the model. Examples would be actual users from the site and their respective interaction data. The hypothesis space for the model would simply be the set of optimized weights and biases calculated from gradient optimization. 

5. Explain in your own words: why memorization should not be considered a valid learning approach. Try to use good, intuitive examples from human learning to motivate your arguments.

Answer: 
 Though memorizing as a major learning strategy has its place in certain contexts, depending solely on memorization might stifle deeper knowledge and critical thinking. Consider a learner who is memorizing mathematical formulae or concepts from a computer programming language. While they may be able to solve issues using the formula or principles they have learned, they may struggle when confronted with a slightly different challenge that needs them to modify what they have learned.
	Furthermore, difficulties in practice are frequently complicated and need a better comprehension of principles as well as training. For example, a soldier who has memorized the whole handbook of any weapon handed to him would be unable to utilize it adequately to protect themselves or others on a battlefield unless they have undergone rigorous training with that weapon to manage stressful scenarios.

6. Explain in your own words: why tabula rasa learning is impossible. 

Answer: 
 Basically, tabula rasa learning is the concept of starting with a completely blank slate, where the learning system has no prior knowledge or assumptions about the problem it is attempting to solve. In practice, however, machine learning algorithms always benefit from existing knowledge; they require data to learn and cannot begin from scratch. The idea is not to start from scratch, but to efficiently harness existing information and data to discover patterns and generate predictions. Furthermore, the process of learning entails generating informed assumptions based on evidence and existing knowledge. As a result, in regard to machine learning algorithms, tabula rasa learning is impossible.

7. Explain in your own words: why picking a good example representation is important for learning. Try to use good, intuitive examples from human learning to motivate your arguments.

Answer: 
When you're learning, a good example representation to present or explain anything is like laying sturdy foundations. It opens the door to learning and helps you grasp things better.
	When learning a new language, for example, you begin with the alphabet and grammatical rules, which serve as the basic building blocks of the language. Once you have these, learning new words and phrases becomes easy since they fit together like jigsaw pieces. Similarly, when you learn something well, you become quite well-versed in it and can use it in a variety of contexts. Assume you learn to ride a bike and can adapt that ability to new bikes or terrains because you have a solid mental model of it.
	So, choosing the best manner to convey anything is critical. It allows you to learn faster, grasp things more fully, and apply your knowledge in a variety of ways. It's like having a solid learning foundation.


8. Consider a learning problem where the examples are described by $n$ Boolean attributes. Prove that the number of *distinct* decision trees that can be constructed in this setting is $2^{2^n}$. *Distinct* means that each tree must represent a different hypothesis in the space. \[Hint: Show that there is a bijection between the set of all Boolean functions over $n$ Boolean attributes and the set of all distinct trees.\] (20 points)

Answer: 
For every set of $n$ attributes, there are $2^{n}$ possible combinations available to us. This means that if we were to construct a set of all possible functions that take in up to $n$ boolean we could feed up to $2^{n}$ possible inputs. For each input combination in the set of $2^{n}$ possible inputs we can create two functions, one that outputs $true$ and another that outputs $false$. 

$$f: S_{2^{n}} = \{0,1,...,2^{n}\} \rightarrow \{0,1\}$$
 
This means that there are $2^{2^{n}}$ possible boolean functions that can be created from a set of $n$ boolean attributes. 

When considering the set of all possible distinct decision trees we must first take into account the fact that each tree contains $n$ nodes as each attribute can be tested with a single node. Each node will branch two ways, either $true$ or $false$. The number of leaf nodes that arises from the construction of a tree should be $2^{n}$ as the number of nodes in the tree doubles each layer. On top of this we must also consider the distinct trees that can arise from the specific layering of all terminal and leaf nodes. Taking this into account we can have up to $2^{2^{n}}$ number of distinct decision trees. 

Define the set of all possible boolean functions over the $n$ attributes:

$B_{n} = [f_{1}, \dots, f_{2^{2^{n}}}|f: [0,1]^{n} \rightarrow [0,1]| f \ is \ a \ boolean \ function]$

Define the set of all possible decision trees made from the $n$ attributes:

$D_{n} = [T_{1}, \dots, T_{2^{2^{n}}}|T \ is \ a \ distinct \ tree \ using \ n \ boolean \ attributes]$

$B_{n}$ is distinct from $D_{n}$ as $B_{n}$ represents the set of all possible boolean functions that take $n$ boolean inputs. $D_{n}$ represents the set of all possible distinct decision trees that can be formed using the $n$ attributes. 

Defining a mapping between the two sets

There exists for every $f$ in $B_{n}$ a $T$ in $D_{n}$ such that 

$$
f_i(n) = 
\begin{cases}
\text{True} & \text{if } T_i(n) = \text{True} \\
\text{False} & \text{if } T_i(n) = \text{False} \\
\end{cases}
$$

Proving the injection between the sets $B_{n}$ and $D_{n}$:

In order to prove that there is an injection between the two sets we must establish that for every decision tree in the set $B_{n}$ there is one and only one boolean function with matching behavior in the set $B_{n}$.

Let's suppose there are two different boolean functions that both take $n$ attributes as input:

$f(n) \ and \ g(n)$

These two functions each map to 2 distinct trees. 

$f(n) \rightarrow T_{f}$
$g(n) \rightarrow T_{g}$

These two boolean functions are distinct from one another, therefore there must exist a set of $n$ boolean attributes that serve as input for both such that

$f(n) \cancel{=} g(n)$

Assuming our mapping holds

$T_{f} \cancel{=} T_{g}$ 

Since there will always exist at least one set of $n$ boolean attributes such that the two functions $f(n),g(n)$ and the two trees $T_{f},T_{G}$ will remain distinct from one another the two sets $B_{n}$ and $D_{n}$ *must have an injective relationship.*

Proving the surjection between the sets $B_{n}$ and $D_{n}$:

In order to prove that there is a surjection between the two sets we must establish that for every decision tree in the set $B_{n}$ there is at least one boolean function with matching behavior in the set $B_{n}$.

Let's suppose there is a decision tree that evaluates a set of $n$ attributes:

$T(n)$

From this one tree we can construct a boolean function $f(n)$ that maps to our decision tree. 

Considering all the possible sets of $n$ boolean attributes. For each set, $T(n)$ will generate an output of either $true$ or $false$. 

Let us construct two sets $P$ and $N$ such that

$P = [\forall n \in [T(n)=True]]$
$N = [\forall n \in [T(n)=False]]$

We can construct our boolean function $f(n)$ such that
$f(n) = True \ if \ n \in P$
$f(n) = False \ if \ n \in N$

Since it is possible to construct a boolean function given a single arbitrary decision tree we have shown that it is possible for every decision tree in the set $D_{n}$ to have a corresponding boolean function in the set $B_{n}$ *this means that there is a surjective relationship between the two sets.*

<<<<<<< HEAD
Consider an abstract boolean function of 3 attributes $(A,B,C)$:
$f : \{0,1\}^{3} \rightarrow \{0,1\}$
 
We would start at the root node, and branch out twice, to represent the two possible states of the first boolean attribute, we would continue this branching for all 3 attributes until we run out. This is how we would construct a unique decision tree for a given boolean function.
=======
Now that we have shown the two sets have both an injective and surjective relationship *this means that they are also bijective.* Since the two sets are bijective their sizes must match, therefore we have proven that since there are $2^{2^{n}}$ possible boolean functions there must also be $2^{2^{n}}$ distinct possible decision trees as well. 
>>>>>>> main

