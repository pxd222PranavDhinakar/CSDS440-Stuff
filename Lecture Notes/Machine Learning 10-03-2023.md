Iterative Optimization (One Variable)




Random Restarts
- The solution we get from Gradient Ascent/Descent depends on the initialization
- One way to make it less dependent is to use *random restarts*
	- Run multiple gradient descents with different random initializations and keep the best overall solution
	- Can be done in parallel

Local and Global Optima
- A *global minimum* for a function is a point $x$ where $f(x) \leq f(x+u)$ for all $u$ 
- a *local minimum* is an $x$ where $f(x) \leq f(x+u)$ for all $u| < \epsilon$



Convex Sets

A set $C$ is convex if for any $x_{1}, x_{2}$ in $C$ $\lambda x_{1} + (1-\lambda)x_{2}$ is also in $C$
A set $C$ is convex if for any two points in the set, the line that joins those two points also resides within the set. 

*For a convex function, every local optimum is also a global optimum.*


Constrained Optimization
$$
\begin{align*}
&min_{x}f(x)\\
&s.t. g_{i}(x) \geq 0, i=1, \dots, m\\
&h_{j}(x) = 0, j = 1, \dots k
\end{align*}
$$

Linear Programming
- A special case of constrained optimization where the object and the constraints are all linear functions
$min_{x}\sum\limits_{i}c_{i}x_{i}$
$min_{x}\sum\limits_{i}a_{ri}x_{i} \geq 0, r=1, \dots, m$
$min_{x}\sum\limits_{i}b_{si}x_{i} \geq 0, s=1, \dots, k$


Simplex Algorithm
- Simple idea: around the polyhedron we go
- From any feasible vertex, walk along the edges of the polyhedron, following the vertices
- Once you are at a vertex where the neighboring vertices have higher $f$ values, stop
- This is a local optimum
	- But this is a convex problem, so this is also a good optimum
- Other algorithms exist such as "interior point methods", which have polynomial bounds

Duality in Linear Programming
- From any "primal" LP, we can derive a "dual" LP in the following way:





*Artificial Neural Networks:*

History
- We want "artificial intelligence"
	- Well, the brain posseses intelligence 
- Let's try to simulate the structure of the brain and hope the function will follow
- Create basic simulations of connected nuerons in large numbers and stand back
	- Maybe it will sing "Daisy, Daisy"
	- Thus the school of "Connectionism" was born

Neurons:
