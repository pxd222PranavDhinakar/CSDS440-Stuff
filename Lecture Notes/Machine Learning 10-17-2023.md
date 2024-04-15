
Convolutional NNs
- A kernel detects a specific feature, but what kernels should we use?
- In a CNN, the kernels (detectors/filters) themselves can be learned
	- Parameterize as a set of weights, and lean via backpropagation

*Tensors*
- In order to maintain locality and invariance, instead of concatenating new kernels 

Example
- Suppose we have a batch of 32x32 images
	- Each input has dimensions (32,32)
- Suppose we apply 10 4x4 kernels to each image with stride 1x1
- The output will be a tensor with dimensions (10,32,32)

*Pooling Layers*
- A pooling layer aggregates information from an adjacent layer
- Average pooling: $k = (\frac{1}{l}, \frac{1}{l}, \dots, \frac{1}{l})$
- Max pooling: computes the maximum value of $l$ inputs

*Vanishing Gradients: Strategies to counter them*
- A key problem in ANNs is vanishing gradients
- To prevent vanishing gradients, we can use the "Rectified Linear Unit" (ReLU) activation function:
$$
h(x) = max(0,x)
$$

- Each layer in an ANN learns a completely new representation from the previous layer
	- Can cause catastrophic failure due to one "bad" layer
- Instead, each layer can add on to the learned representation of the previous layer
	- Allows building much deeper structures robustly

*Residual Networks*
- Perturbing the representation is done through adding a "residual" function to each layer
- $z^{l}$: output of layer $l$
- $W^{l}$: weights between layer $l$ and $l+1$
- Replace: $z^{l+1} = h(W^{l}z^{l})$
- With: $z^{l+1} = h(z^{l} + f(z^{l}))$,  $f(z^{l}) \sim W^{l}z^{l}$

*How do we prevent overfitting?*
- ANNs are very prone to overfitting
	- Structure can be very complex, lots of parameters
	- Decision surface can be very nonlinear

*Controlling Overfitting*
- One strategy: add a "weight decay" term
$$
L_{oc}(w) = L(w) + \gamma\sum\limits_{i}\sum\limits_{j}w^{2}_{ji}
$$
- When $\gamma$ is extremely large, all weights get pushed down to $0$ during backpropagation