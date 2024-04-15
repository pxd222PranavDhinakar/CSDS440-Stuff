- Some pros of probabilistic approaches for classification are: 
	- Optimal approach in terms of decision-theory
	- Can use prior knowledge
	- Produces confidence measures
	- Well studied
	- Simple models that are easy to implement
	- Can nicely capture causal influences (we know why they work)
- Some cons are:
	- Inference and estimation are hard
	- Discriminative approaches can be hard to interpret
- High dimensional generative models are based on *latent variables* which capture *hidden features* of the outputs. 
- Typically we have no idea what these latent variables could be, so we sample them from a *normal* distribution and warp them into the distribution required using a *neural network*.
- In high dimensions, most *latent variables* will not lead to *trivial sample errors* with high probability.
- So we learn a second function Q that attempts to produce $p( z| X )$. 
- The KL divergence between two distributions X and Y is defined as $D(X,Y)=E_{z~X}(log(X(z)) - log(Y(z)))$.


**Normal Distribution**: In many machine learning models, especially those related to generative models like Variational Autoencoders (VAEs) or Generative Adversarial Networks (GANs), latent variables are often initially sampled from a normal (or Gaussian) distribution. This is because the normal distribution is a common, well-understood statistical distribution that provides a good starting point for a wide range of values.

**Trivial Sample Errors**: In high-dimensional spaces, the concept of "trivial sample errors" refers to the idea that the errors or deviations in the samples (generated from the latent variables) are simplistic or insignificant. However, due to the complexity and the curse of dimensionality in high-dimensional spaces, most latent variables will not lead to such simple errors. Instead, the errors or deviations can be complex and significant, requiring careful modeling and understanding of the underlying data distribution. This concept is particularly relevant in the field of machine learning and statistics, where understanding and handling high-dimensional data is a common challenge.

*Kullback-Liebler Divergence:*
The Kullback-Leibler (KL) Divergence is a concept from information theory, often used in statistics and machine learning, particularly in the context of probabilistic models. It's a measure of how one probability distribution diverges from a second, expected probability distribution. Here's a detailed explanation: