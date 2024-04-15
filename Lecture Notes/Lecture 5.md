*Overview*
- We can/cannot remove continuous attributes after partitioning with them. Why? 
	- *We create test partitions based on whether the attribute value is less than a chosen test. This does not eliminate the attribute entirely, just the subset of that attribute that fit the test. We can remove once we have finished with all possible tests of that attribute*
- What is overfitting? 
	- *Every leaf in the decision tree is pure, given enough examples*
	- *When a learned concept has high performance on training data, but lower performance on average across all examples*
- We control overfitting in trees through (ES) and (PP). 
	- (ES) = *Early Stopping*
	- (PP) = *Post Pruning*
- How does ES work? Why might it not work well in practice?
	- *Standard ID3 stops growing when IG(X) = 0 for all remaining attributes X*
	- *Early stopping stops growing the tree when $IG(X) \leq \epsilon$ for some chosen $\epsilon$* 
	- *Easy to implement, but does not work very well in practice*
	- *Reason for it not working could be that the results are highly sensitive to our chosen $\epsilon$*
	- *We could stop too early and have an incomplete and ineffective tree*
	- *Or we could stop too late and be left with an overfitted tree regardless of our effort*
- PP uses a *validation* set. It iteratively *deletes* a node and evaluates the result on the *validation* set. It keeps the tree that has best performance. It stops when *improvement in performance is no longer affected by node removal*.





- We partition on continuous features by considering all tests of the form.
- We only need to consider values that _______.


*Continuous Attributes*
- Cannot test for equality
- Consider all Boolean tests of the form $X \geq v$ or $X \leq v$
	- Only values of interest are those $v$ that separate adjacent training examples with different classes. (why?)
- Note: In this case, the attribute cannot be removed, though the test ((attribute, value) tuple) can be. 

*ID3 Algorithm* Training Phase

![[Screen Shot 2023-09-14 at 10.12.39 AM.png]]

Example:
![[Screen Shot 2023-09-14 at 10.16.16 AM.png]]

$n=3$ features, 2 nominal variables: Color, Shape. 1 Continuous variable, Area.

1. *Tests*: Color, Shape, Area: $\{\cancel{0.15}, 0.25, 0.35, 0.5, \cancel{0.65}, \cancel{0.75}\}$
   The only partitions that are worth considering are the ones in between examples with different labels
2. *IG(X)*:
   *H(Y)* = $-p_{+}log_{2}p^{+}-p^{-}log_{2}p^{-} = \frac{-1}{3} log_{2} \frac{1}{3} - \frac{2}{3} log_{2} \frac{2}{3} = H(\frac{1}{3})$ 
   $p^{+}=\frac{1}{3}$
   $p^{-}=\frac{2}{3}$
   $IG(Color) = H(Y)-H(Y|Color) = H(\frac{1}{3}) - [\frac{1}{3}\times H(\frac{1}{3}) + \frac{1}{3}\times H(\frac{1}{3}) + \frac{1}{3}\times 0]$
   $H(Y|Color=red) =H\left(\frac{1}{3}\right)$   
   $p^{+}=\frac{2}{3}$
   $p^{-}=\frac{1}{3}$
   
   $H(Y|Color=blue) =H\left(\frac{1}{3}\right)$   
   $p^{+}=\frac{2}{3}$
   $p^{-}=\frac{1}{3}$
       
   $H(Y|Color=green) = 0$   
   $p^{+}=\frac{0}{3}$
   $p^{-}=\frac{3}{3}$
   
   $IG(Area\leq 0.25) =$
   
   $H(Y|A\leq0.25) = 0$
   
   $H(Y|A>0.25) = H(\frac{1}{2})$
   
   $IG(A) = H(\frac{1}{3}) - \frac{7}{9}H(\frac{1}{7})$ 
Continue this on own and work out fully constructed tree.


An Issue
- Given enough features, ID3 will usually be able to fit training examples exactly (i.e. every leaf is pure), because the tree can be grown as much as needed.
- But real data is *noisy*


   
   