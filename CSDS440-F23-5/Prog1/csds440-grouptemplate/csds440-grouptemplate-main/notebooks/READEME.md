# Decision Tree Implementation

### Experience with the Skeleton/Utility Code
1. Structure and Clarity: The provided skeleton code is modular and well-structured. It breaks down the decision tree building process into various parts, including evaluation, tree construction, and utility functions. This modularity made the implementation and debugging process smoother. However, since I am a beginner of learning python, it takes me a while to even understand how to use these documentations. Especially for how to use the outer package "sting" at first, I just simply download this package to my local computer trying to import it successfully.

2. Utility Functions: The utility functions provided (like util.accuracy()) abstract away some of the complexities and allow the main code to remain clean and focused on decision tree logic. It would be beneficial to see more of such utility functions for other common tasks. It teaches me to seperate functions that are not relavant from our main program when build it. Also thanks to this good habit, we can maintain and modify our codes effectively.

3. Comments and Documentation: The code comes with some inline comments, especially for helper functions. These were valuable in understanding the purpose and logic behind each function.

4. Flexibility: The design of the code allows for easy toggling between using Information Gain or Gain Ratio and provides the option for cross-validation and the limit of the learning depth. This flexibility is a significant advantage as it makes experimenting with different settings straightforward.

### Documentation:

1. Method Descriptions: Every function is accompanied by a docstring that describes the purpose, parameters, and expected return. This made it easier to understand the function's expectations and its role in the overall process.

2. Variable Naming: The variables are descriptively named (like total_accuracy, tree_depth_limit), which makes the code more readable and reduces the need for excessive comments.

### Confuing Aspects:

1. I am still confused on how to construct the tree. I think I kind of get the sense of defining a new class representing node or something, but actually I am not sure about the process. It would be more clear if I was provided with more contexts.

2. The program runs so slow on dataset, I tried to apply the numba, but it seems that the problems occur when it is used on complex calculation. In terms of this issue, I should try to break each function into smaller pieces (like _information_gain() which involves complex computation), especially for those functions with complicate math calculation.

3. I didn't figure out how to structure the entire program to run efficiently, perhaps some fancy propertites on numpy or other packages are not well used by me. 
