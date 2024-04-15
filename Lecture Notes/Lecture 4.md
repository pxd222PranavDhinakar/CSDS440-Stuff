*Overview*
- To choose a test, we look for an attribute that provides *information* about the *label*. A quantity that encodes this is the *entropy* of a random variable.
- *Entropy* is the expected length of the *shortest lossless description* of a random variable.
- *information gain* is the *reduction of entropy* of the class variable *before* and *after* partitioning.
- What problem arises with nominal features and info gain?
	- *When an attribute has a lot of possible values, IG prefers it because the more attributes, the more labels it can partition. However, a single nominal attribute can have as many possible values as there are datapoints and this would cause a single partition to hog the entire label set, which memorizes the data. This would lead to a perfect Information Gain score*
- We can attempt to resolve this issue by adjusting the split-criterion. *GR(X)=IG/H(X)*. This works because the H(X) increases as the range of values for X increases.


