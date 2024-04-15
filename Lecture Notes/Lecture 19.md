- Using the KL divergence, we can write the log likelihood of the training set approximately as (expectation of $log(P( X | \Theta ))+ D( Q || P )$. This holds when $Q = P''$
- This is an *“encoder decoder”* architecture. The *encoder* is *'responsible for compressing the input data into a compact representation'*. The *decoder* is *'responsible for reconstructing the input data from this compact representation'*. • 
- To compute the first term we only need *one sample*. This is because *the first term typically represents the expectation of a log likelihood, which can be estimated accurately with a single, well-chosen sample in scenarios where the probability distribution is well-behaved or when the model's variance is low.*
- However, this is problematic because *it can lead to high variance in the gradient estimates*. To solve this, we sample from a noise distribution at the input layer, then multiply and add. This is called the *"reparameterization trick."*. 
- Support vector machines combine three ideas: *linear decision boundaries*, *margins*, and *kernels* 
- A *Linear Discriminant* has the general form $w \times \phi(x) + b = 0$. 

