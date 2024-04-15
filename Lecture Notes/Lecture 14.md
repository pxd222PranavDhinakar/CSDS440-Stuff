- Convolution is a *linear* operation. The *kernel* can be *learned* from *data*.
- A tensor is a *multi-dimensional matrix*. It is used to preserve *locality* across layers. 
- A pooling layer *aggregates information* from adjacent layers.
- Deep NNs suffer from the *vanishing gradients* problem.
- The ReLU activation is defined as h(x)=max(0, x).
- In a *residual* network, the learned representation at each layer is a *perturbation* of the previous.
- One way to control overfitting in ANNs is to use *weight decay*. This adds a *cost penalty* to the loss function.

1. Convolution is a *linear* operation. The *kernel* can be *learned* from *data*.
**Linear Operation**: Convolution is considered a linear operation because it involves the linear combination of input data with a set of weights (contained in the kernel or filter). Each output value of the convolution is a weighted sum of the input values, which adheres to the principles of linearity.

**Kernel Learned from Data**: In the context of convolutional neural networks (CNNs), the kernel (or filter) is a small matrix used to extract features from the input data (like images). Instead of being manually designed, these kernels are typically learned during the training process. The neural network adjusts the values in the kernels to minimize some loss function, thereby learning the most effective filters for the task at hand (e.g., edge detection, texture recognition) directly from the data.

2. A tensor is a *multi-dimensional matrix*. It is used to preserve *locality* across layers. 
**Multi-Dimensional Matrix**: A tensor in the context of machine learning and neural networks is essentially a multi-dimensional matrix or array. While a 2D matrix has rows and columns, a tensor extends this concept to higher dimensions. For instance, a 3D tensor could be thought of as a cube of numbers, and higher-dimensional tensors have more complex structures.

**Preserve Locality**: In neural networks, especially convolutional neural networks (CNNs) used for image processing, tensors are used to preserve the spatial locality of the data. For example, in image processing, a 3D tensor could represent an image with dimensions for height, width, and color channels. Using tensors allows these networks to maintain the relationship between adjacent pixels (locality) in the image across various layers of the network, which is crucial for effectively learning features like edges, textures, and patterns in images.

3. A pooling layer *aggregates information* from adjacent layers.
**Aggregates Information**: Pooling layers in neural networks, particularly in convolutional neural networks (CNNs), are used to reduce the spatial dimensions (i.e., width and height) of the input volume for the next convolutional layer. They work by aggregating information from small regions (usually 2x2 or 3x3) in the previous layer. The most common types of pooling are max pooling and average pooling. Max pooling takes the maximum value from each region of the input, while average pooling takes the average value. This process helps to reduce the computation required in the network, control overfitting by providing an abstracted form of the representation, and retain important information about the presence of features in the regions of the input.

4. Deep NNs suffer from the *vanishing gradients* problem.
**Vanishing Gradient Problem**: In deep neural networks, especially those with many layers, the gradients used in the backpropagation process can become very small, effectively approaching zero. This happens due to the multiplication of gradients through the network's layers. When the gradients vanish like this, it becomes difficult for the network to learn and update the weights of the earlier layers, leading to slow or stalled training progress. This problem is particularly prominent in networks with saturating activation functions like the sigmoid or tanh functions.

5. In a *residual* network, the learned representation at each layer is a *perturbation* of the previous.
**Residual Network**: A residual network (often abbreviated as ResNet) is a type of neural network architecture that introduces the concept of residual learning. It's particularly useful for training very deep networks.

**Perturbation of the Previous**: In ResNet architectures, each layer learns a residual (or a perturbation) with respect to the layer inputs, rather than learning unreferenced functions. This is typically achieved by using shortcut connections (or skip connections) that bypass one or more layers. The output of a residual block is the addition of the input to the block and the output of the stacked layers in the block. This approach helps to address the vanishing gradient problem and allows the training of much deeper networks by enabling the efficient flow of gradients during training.

6. One way to control overfitting in ANNs is to use *weight decay*. This adds a *cost penalty* to the loss function.
**Weight Decay**: Weight decay is a regularization technique used in training neural networks. It works by adding a penalty to the loss function based on the magnitude of the weights. The idea is to prevent the weights from becoming too large, which can lead to a model that is overly complex and more likely to overfit the training data.

**Cost Penalty**: The penalty typically involves the sum of the squares of the weights (L2 regularization), and it is added to the original loss function. This cost penalty encourages the network to keep the weights small, which can lead to simpler models that generalize better to new, unseen data. The overall effect is to balance the fit of the model to the training data with the complexity of the model.