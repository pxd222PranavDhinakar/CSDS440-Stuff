**Foundations**

What is "Machine Learning"?:
- "Machine" = autonomous system
- No (or limited) human intervention
- Robots, software agents, etc.

What is "Learning"?:
"Learning denotes *changes* in the system that enable the system to do the same *task* more *effectively* the next time."
	-Herbert Simon (1916-2001)
	-Also how to do related tasks more effectively.

A specification for a Learning System
- Given:
	- Learning task
	- Task examples, E
	- Performance measure, P
- Do: Produce a *concept* that is good with respect to P on all examples of the task
	- Measured by proxy on E

Example
- Learning Task: Learn to play chess
- Performance Measure?:
	- Play n games and see how many of those games are won
	- This is by far not the best measure there are many measures based on what behavior you wish your model to exhibit. 
- Examples?:
	- Databases of past games that people have played
- *Concept?:* 
	- A method to determine what next move to make based on the board state
	- *Some function mapping current state of game to suitable moves to play*

IDEA:
- If the learning system plays/sees enough games,
- And it produces a mapping from game state to moves (concept)
- And this concept does well with respect to the measure of "number of games won",
- Then the system has "*learned to play chess*"

Other Examples:
- Learn to recognize lions
	- E: animals, annotated "lion" or "not-lion"
	- P: fraction of animals correctly recognized as lion/not-lion
- Learn to drive:
	- E: sequence of road/traffic conditions and correct vehicle operation
	- P: distance traveled without accident.

Two Phases of Learning
- "Learning" or "Training" phase
	- *Reason* about the examples E
	- Formulate a *concept* that does well w.r.t P on E
	- Could also use any *prior knowledge*
- "Evaluation" or "Testing" phase
	- Use learned concept on future, novel examples

Online and Batch (offline) Learning
- *Batch/Offline* Learning: one learning phase, with a large set of examples, followed by a testing phase
- *Online* Learning: Examples arrive one at a time (or in small groups); learning and evaluation phases are iterated

*Inductive Generalization*
- In all learning problems, need to reason from specific examples to a general case
	- *MEMORIZATION $\cancel{=}$ LEARNING*
- Other kinds of reasoning 
	- Deduction (general to specific)
	- abduction (most likely cause)
		- Related to causality 

*Target Concept*
- The unknown underlying concept that solves the learning task
	- E.g., "has-fur" and "long-teeth" and "looks-scary" $\rightarrow$ lion
- Typically, P will be a measure of difference between the learner's concept and the target concept, with respect to E

*Hypothesis Space*
- Defines the space of general concepts the learning system will consider
	- E.g., all possible conjunctions of animal properties
	- "has-fur" and "long-teeth" and "looks-scary", "has-fur" and "long-teeth" and NOT-"looks-scary", "has-fur" and NOT-"long-teeth" and "looks-scary"...
- Ideally, target concept is a member of this space
	- You will have to craft your performance measure based on the hypothesis space that you will be exploring. 
- If we had $n$ attributes to analyze in our hypothesis space, then we were to construct our space out of every two-pair conjunction of our n attributes then we would have a space of size $2^{n}$ which is not computationally feasible to analyze at large values of $n$

*No "Tabula Rasa" Learning* 
- A space that includes all possible hypotheses also
	- Contains many overly complex concepts
	- Contains the concept that *memorizes E*
		- Indistinguishable from target by any P (w.r.t E)
	- May be too big to search feasibly
- For effective inductive generalization
	- *Must* restrict hypothesis space
	- while still (hopefully) keeping the target concept in it

*Inductive Bias*
- The set of assumptions used by a learning system to restrict its hypothesis space
- The more assumptions made, the "stronger" the bias
- Can quantify this (later)




