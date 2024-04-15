Iterations:
Voting Data:
num_features = 3

First step: For each column of data calculate the information gain of feature w.r.t the label



$class \ Node(schema, tests):$ // Note schema being passed is for node feature not total schema
	$self.children = []$
	$self.tests = tests$
	$self.schema = schema$

$Train(X,y)$
	$infoGains = []$
	*for* $column$ *in* $X$:
		$infoGain = getInfoGain(column, y)$
		$infoGains.add(infoGain)$
	$maxInfoGainIndex = getMax(infoGains)$ // Finds the feature that has the highest info gain.
	$root = new \ Node(self.schema[maxInfoGainIndex], tests[maxInfoGainIndex])$ //Create root
	// Generate the children for the node
	*for* $test$ *in* $root.getTests()$:
		// Create sub-label set and sub-data set, by removing the attribute the root tests for.
		$mask = X[:, maxInfoGainIndex] == test$ // Mask for the current feature value
		$filteredData = X[mask]$ 
		$filteredLabels = y[mask]$
		*if* $filteredData = X$:
			*return* $root$ 
		$child = Train(filteredData, filteredLabels)$
		$root.addChild(child)$
	*return* $root$



ID3 Pseudo Code Rewrite

$Global \ Vars:$
$maskedIndeces = []$
$schema = [Feat_{0}, \dots, Feat_{n}] \forall x_{n} \in X$

$Fit(X, y)$:
	// Determine the split points of each feature in the dataset
	$splitCriterion = self.determineSplitCriterion(X,y, self.schema)$
	// Function returns the IG(Y|X=x), or infogain of each feature w.r.t the labels
	$infogains = util.getInfoGains(X, y, )$
	$maskedInfoGains = applyMask(infogains, maskedIndeces)$
	$maxIGIndex = findMax(maskedInfoGaims)$
	*if* $infogains[maxIGIndex] == 0$:
	$leaf = Node(schema[maxIGIndex], tests = None, label = util.majorityLabel(y))$
	