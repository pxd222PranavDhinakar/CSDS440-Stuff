# CSDS440 Written Homework 1
**Instructions:** Each question is worth 10 points unless otherwise stated. Write your answers below the question. Each answer should be formatted so it renders properly on github. **Answers that do not render properly may not be graded.** Please comment the last commit with "FINAL COMMIT" and **enter the final commit ID in canvas by the due date.** 

When working as a group, only one answer to each question is needed unless otherwise specified. Each person in each group must commit and push their own work. **You will not get credit for work committed/pushed by someone else even if done by you.** Commits should be clearly associated with your name or CWRU ID (abc123). Each person is expected to do an approximately equal share of the work, as shown by the git logs. **If we do not see evidence of equal contribution from the logs for someone, their individual grade will be reduced.** 

1. For three random variables A, B and C, show with a clear example that the statement “A is independent of B” does not imply the statement “A is independent of B given C.” 

Answer: (by mxl1166)

**Example : rolling a dice twice**

Define events below:

A = The first roll shows a $3$,

B = The second roll shows a $4$,

C = Two rolls sum up to $7$.

A and B are clearly independent with each other. Given that C occurs, if we know the first roll is $3$ (A happens), we will know that the second roll is $4$ for sure (probability of B is $1$).

2. Points are sampled uniformly at random from the interval $(0,1)^2$ so that they lie on the line $x+y=1$. Determine the expected squared distance between any two sampled points. 

Answer:(by mxl1166)

Suppose that two randomly picked point are represented as $(x_1,y_1)$, and $(x_2,y_2)$.

The expected squared distance: $D^2 = (x_1-x_2)^2 + (y_1-y_2)^2$

Since they are sampled on line $x+y=1$, we can substitute $y$ with $1-x$. $D^2$ can be further simplified as:

$D^2 = (x_1-x_2)^2 + ((1-x_1)-(1-x_2))^2$

$D^2 = 2(x_1-x_2)^2$

Since they are uniformly sampled on $x+y=1$, the p.d.f should be 1. 

$E(D^2) = \int_{0}^{1}\int_{0}^{1} 2(x_1-x_2)^2dx_1dx_2$

After solving the equation, we get:

$E(D^2) = \frac 13$

3. For any two random variables $X$ and $Y$, the conditional expectation of $X$ given $Y=y$ is defined by $E(X|Y=y)=\sum_x p_X(x|Y=y)$ for a fixed $y$. Show that, for any three random variables $A$, $B$ and $C$, $E(A+B|C=c)=E(A|C=c)+E(B|C=c)$.

Answer: (Done together by jxm1280 & mxl1166 )

By definition, 

$E(A+B|C=c)=\sum_{a,b} (a+b)p_{A,B}(a,b|C=c)$

So we can re-arrange this equation to get:

$E(A+B|C=c)$

$=\sum_a a·(\sum_b p_{A,B}(a,b|C=c)) + \sum_b b·(\sum_a p_{A,B}(a,b|C=c))$

$=\sum_a a·p_A(a|C=c) + \sum_b b·p_B(b|C=c)$

$=E(A|C=c) + E(B|C=c)$ (by definition of expectation)

4. Describe two learning tasks that might be suitable for machine learning approaches. For each task, write down the goal, a possible performance measure, what examples you might get and what a suitable hypothesis space might be. Be original---don’t write about tasks discussed in class or described in the texts. Preferably select tasks from your research area (if any). Describe any aspect of the task(s) that may not fit well with the supervised learning setting and feature vector representation we have discussed. 

Answer: (by jxm1280)

**Task 1: Voice Cloning for Text-to-Speech Synthesis**

Goal:

Developing a machine learning system capable of emulating a real individual's voice and generating speech from textual inputs using that mimicked voice.

Performance Metric:

Evaluation will rely on the Mean Opinion Score (MOS), as determined by human assessors. MOS gauges the authenticity and likeness of the generated voice to the target voice and can vary from 1 (poor) to 5 (excellent).

Data Examples:

High-quality audio recordings featuring the target person uttering various sentences.
Transcribed text passages illustrating what the target person might articulate in diverse scenarios.

Viable Hypothesis Space:

Variational Autoencoders (VAEs) or Generative Adversarial Networks (GANs) for generating speech waveforms.
Recurrent Neural Networks (RNNs) or Transformer-based models for transforming text inputs into spectrograms, subsequently translated into speech.

Challenges and Limitations:

Scarce availability of data from the target individual, rendering the capture of their unique vocal traits challenging.
Ethical concerns associated with potential misuse, especially in deepfake applications.
Ensuring that the cloned voices exhibit both naturalness and emotional expressiveness.

**Task 2: Traffic Accident Risk Forecasting**

Goal:

Constructing a machine learning model to predict the risk level of traffic accidents for individuals in traffic based on various parameters, including time of day and day of the week.

Performance Metric:

Evaluation metrics encompass the Area Under the Precision-Recall Curve (AUC-PR) or Mean Absolute Error (MAE) for regression tasks, providing insights into the accuracy of risk level forecasts.

Data Samples:

Historical records of traffic accidents, encompassing timestamps, locations, weather conditions, road types, and participant details.
Real-time data streams sourced from traffic cameras, weather stations, and traffic flow sensors.

Suitable Model Space:

Time series forecasting models like Long Short-Term Memory (LSTM) networks, which are adept at capturing temporal dependencies within accident data.
Decision tree-based models, adept at encapsulating the influence of diverse factors on accident risk.

Challenges and Limitations:

Management of imbalanced data, as traffic accidents constitute relatively infrequent occurrences compared to accident-free instances.
Integration of real-time data sources for precise and up-to-the-minute risk assessments.
Addressing privacy concerns linked to the utilization of data related to individual traffic participants.


5. Explain in your own words: why memorization should not be considered a valid learning approach. Try to use good, intuitive examples from human learning to motivate your arguments.

Answer: (by mxl1166)

**(1) Memorization is a **shallow** learning.**

Learning requires an understading of concepts, and it knows how to apply the learned knowledge to novel cases in different contexts.

**Example:** Given a math formula, like pythagorean theorem, $a^2 + b^2 = c^2$, memorization means that we only remember this equation, and apply it to the triangle. But it can also be applicable to circle, square, rectangle.

**(2) Memorization is **distinct** from incorpating prior information.**

While learning is an evolving process that builds upon and integrates with previous knowledge, memorization doesn't. Memorization is a static method that doesn't actively engage with or adapt from prior information. It lacks the creative depth of genuine learning, which involves recognizing patterns, making connections between old and new knowledge, and continually updating our understanding.

**Example:** Consider the process of learning a new language. Merely memorizing involves repeating sentences word for word. On the other hand, truly learning the language means grasping its structure, understanding elements like subjects, verbs, and objects, and using that foundational knowledge to construct original sentences.

**(3) Memorization has its limitations in capacity.**

Memorization entails storing information in its exact form, which can rapidly consume memory space. This method, even when applied by powerful computers, has its bounds. Conversely, learning emphasizes understanding underlying patterns or principles. Once we've grasped a foundational concept, we can often discard specific examples or details, freeing up memory while retaining the ability to apply the concept in diverse situations.

**Example:** Take example of summation of numbers. There's an infinite number of combinations for adding two numbers together, and it's unfeasible for anyone to remember all possible outcomes. However, by understanding the basic principle of addition, we can readily calculate the sum of any two numbers, and even expand this understanding to more complex calculations.

6. Explain in your own words: why tabula rasa learning is impossible. 

Answer: (by mxl1166)

**(1) Risk of Memorization**

As we talked before, if we consider all possible hypotheses space, we merely memorize the data. It makes inpossible to generalize concept well to new data. 

**(2) Infeasibility of Search**

Nowadays, the data is astronomically huge and likely noisy. The time and resources required to search all possible space are overwhelming. Thus, it is computationally infeasible.

**(3) Risk of Overfitting**

This will result in overly complex concept. Such concept will do good on perforamance on training data, but lead to a low performance on unseen data, or ineffectively inductive generalization. 


7. Explain in your own words: why picking a good example representation is important for learning. Try to use good, intuitive examples from human learning to motivate your arguments.

Answer: (by mxl1166)

**(1) Facilitate Generalization & Reduce misunderstanding**

A good feature helps us to reduce the ambiguities while trying to learn the concept. Thus, it allows us to identify the patterns which effectively imporve the generalization on novel cases. 

**Example:** Suppose we want to distinguish the bird from the lion.  If "has-fur" is chosen as our representation, it is likely to group the birds as a lion, because they both have furs. If we use "beak", "ability to fly", such features that is more distinguishable to classify a bird, it definiely will help us to label a bird or a lion.

**(2) Simplifies Complexity**

The more distinguishable feature we pick, the simpler(but still powerful) concept we learn. A good feature can capture the essence of a concept which is used to achieve the purpose of our task. 

For instance, if we try to differentiate between a bird and a lion using the feature "has fur", we'll require additional features for accurate classification. On the other hand, attributes like "having a beak" or "the ability to fly" are more definitive of birds. By focusing on these distinguishing features, we reduce the complexity of our conceptual framework, thereby enhancing the efficiency of our learning. This is because features like "has fur" become redundant and offer limited value in this context.


8. Consider a learning problem where the examples are described by $n$ Boolean attributes. Prove that the number of *distinct* decision trees that can be constructed in this setting is $2^{2^n}$. *Distinct* means that each tree must represent a different hypothesis in the space. \[Hint: Show that there is a bijection between the set of all Boolean functions over $n$ Boolean attributes and the set of all distinct trees.\] (20 points)

Answer: (by jxm1280)

**(1)Mapping Between Boolean Functions and Decision Trees:**

Boolean functions take n Boolean attributes and produce binary outputs (0 or 1).
Decision trees serve as hypotheses by making attribute-based decisions, leading to classifications (0 or 1).

**(2)Bijection Between the Two Sets:**

For each Boolean function, there is a corresponding decision tree where input combinations become paths in the tree leading to output nodes.
Conversely, for each decision tree, there is a corresponding Boolean function that can be constructed by traversing the tree.
One-to-One Correspondence (Bijection):

**(3)A one-to-one relationship exists:**

Each Boolean function uniquely corresponds to a decision tree.
Each decision tree uniquely corresponds to a Boolean function.

**(4)Counting Decision Trees:**

There are $2^{2^n}$ distinct Boolean functions for n Boolean attributes because each of the 2^n possible input combinations can yield 2 distinct outputs (0 or 1).
Due to the established bijection, the number of distinct decision trees is also $2^{2^n}$.

Therefore, the number of distinct decision trees for a learning problem with n Boolean attributes is indeed $2^{2^n}$.

---
FINAL COMMIT by 

Mingxuan Liu(mxl1166)

