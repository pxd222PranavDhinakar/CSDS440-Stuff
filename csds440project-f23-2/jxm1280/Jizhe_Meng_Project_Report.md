### In order to have a clear understanding of the methods, please read the [Semi_supervised_learning_updated_final.ipynb](notebooks/Semi_supervised_learning_updated_final.ipynb) under /notebooks

 
 -----
## **1. Survey**
-----
### **Paper 1: "Learning Semi-supervised Gaussian Mixture Models for Generalized Category Discovery"**
- **Overview**: This paper introduces an innovative approach for GCD, addressing the challenge of clustering unlabeled data in mixed datasets. It proposes a semi-supervised Gaussian Mixture Model (GMM) that dynamically adjusts class numbers in unlabeled data, a significant step forward in semi-supervised learning.
### **Paper 2: "Pseudo-Label: The Simple and Efficient Semi-Supervised Learning Method for Deep Neural Networks"**
- **Overview**: This paper presents a semi-supervised learning method using Pseudo-Labels for deep neural networks. It focuses on maximizing the use of limited labeled data, enhancing learning efficiency through pseudo-labeling techniques.
#### ***Comparison***
- **Paper 1** excels in its adaptive clustering approach for complex datasets with unknown class numbers.
- **Paper 2** offers an efficient method for leveraging limited labeled data, suitable for scenarios where labeled data is scarce.


**Project Topic:** Anomaly Detection in Credit Card Transactions: Semi-Supervised Models   



-----
## **2. Methods Introduce**
-----


**Models Implemented**

- Gaussian Mixture Model (GMM)
- One-Class SVM (Support Vector Machine)
- Autoencoders
- Combined Approach (GMM + Autoencoder)

### Credit Card Transactions Dataset:

Overview

This dataset contains transactions made by European cardholders in September 2013. It offers insights into the nature of credit card transactions over a period of two days, with a specific focus on identifying fraudulent activities.

Dataset Details

General Information

- **Time Frame**: September 2013
- **Geographical Focus**: Europe
- **Duration Covered**: Two days

Transaction Statistics

- **Total Transactions**: 284,807
- **Fraudulent Transactions**: 492
- **Percentage of Fraudulent Transactions**: 0.172%

Characteristics

- The dataset is **highly unbalanced** with the positive class (frauds) accounting for only 0.172% of all transactions.
- **Primary Use Case**: This dataset is particularly useful for research and analysis in the fields of anomaly detection and fraud prevention in financial transactions.

Data Access

- [Download the Dataset from Kaggle](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.kaggle.com%2Fcode%2Fmatheusfacure%2Fsemi-supervised-anomaly-detection-survey%2Finput)
  link : <https://www.kaggle.com/code/matheusfacure/semi-supervised-anomaly-detection-survey/input>

-----
## **2.1 Gaussian Mixture Model**

### Data Exploration and Preprocessing:

![1702461411058](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/11520eff-162d-4e72-ae9f-e7f31f28cc30)

**Missing Values:** There are no missing values in any of the columns of the dataset.

**Statistical Summary:**

The features V1 to V28, which are the result of PCA, show varying ranges and distributions. The Time and Amount features have a wide range of values and might require scaling. The summary statistics of these features might not be very informative due to the PCA transformation. Class Distribution (Data Imbalance):

The dataset is highly imbalanced, with only about 0.173% (approximately 1 in 578) of transactions being fraudulent (Class = 1). The vast majority (99.827%) of transactions are normal (Class = 0).

### Training:

(((170589, 30), (56961, 30), (56962, 30)), ((170589,), (56961,), (56962,)))

**Training Set:** 170,589 samples (only normal transactions).

**Validation Set:** 56,961 samples.

**Test Set:** 56,962 samples.

The training set consists exclusively of normal transactions (Class = 0) to facilitate the semi-supervised learning approach. The validation and test sets contain a mix of both normal and fraudulent transactions, mirroring the original data distribution.

**Training Gaussian Mixture Model:** We start with a default number of components and can later adjust this based on validation set performance and displaying the first 10 scores(log likelihood of the validation set) for a quick check:

![1702461623787](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/93525b18-ed4a-40db-ae34-b4cfcfd434b4)

The log likelihood scores indicate how well each sample fits the model. In the context of anomaly detection:

Higher scores generally indicate that the sample is more likely to be a "normal" transaction. Lower scores suggest that the sample is more likely to be an anomaly or a fraudulent transaction.

The threshold with the maximum F2 score:

(111.08750612861401, 0.6325823223570191)

Calculated evaluation metrics:

(0.0017380007724447878, 1.0, 0.0034699707330751303, 0.008630008019805433)

**Gaussian Mixture Model (GMM) for semi-supervised learning in credit card fraud detection can be summarized and analyzed as follows:**

**Data Preparation:**

Features are standardized using StandardScaler.

The dataset is split into training, validation, and test sets. Notably, the training set consists only of normal transactions (Class = 0), which is a typical setup for semi-supervised anomaly detection. GMM Training:

A GMM with 4 components is trained on the training set. The model is then used to compute log likelihood scores for each transaction in the validation set. These scores indicate how well each transaction fits into the model's understanding of "normal" behavior.

**Threshold Determination:**

You calculated precision, recall, and F2 scores across various thresholds to find the optimal point for classifying a transaction as fraudulent. The chosen threshold (111.09) and its corresponding F2 score (0.633) reflect a model that emphasizes recall (catching as many frauds as possible).

**Model Evaluation:**

When applied to the test set, the model achieved a perfect recall (1.0), meaning it identified all fraudulent transactions. However, the precision is extremely low (0.00174), indicating that many normal transactions were incorrectly flagged as fraudulent.

![1702460444263](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/5402b3e5-a63f-4f69-8a4a-00dacd5cf735)

**ROC Curve:** The ROC curve is close to the top left corner, indicating a high true positive rate (TPR) and low false positive rate (FPR). The area under the curve (AUC) is 0.95, which generally indicates a very good classifier. However, given the extreme class imbalance, the ROC curve can be overly optimistic; fraud cases are so rare that the model can achieve a low FPR while still having many false positives.

![1702460466654](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/4a92e638-80ef-450c-96fb-8e3d3bb44b0e)

**Histogram of Log Likelihood Scores:** This plot shows a clear separation between the scores of normal transactions and fraud transactions, with fraud transactions tending to have much lower scores. This suggests that the GMM is effectively differentiating between the two types of transactions on the likelihood score basis. However, the overlap is still significant, hence the low precision in practice.

![1702460484248](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/3a6e4e81-1aad-4cb0-a2ea-fd8beffddd18)

**Precision-Recall Curve:** The precision-recall curve shows that as recall increases, precision drops significantly. This is typical in imbalanced datasets where achieving high recall often means accepting a lower precision. The sharp decline at the start suggests a small subset of predictions are very confident, after which precision degrades.

![1702460409696](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/ce33af05-2734-4f13-ac41-754bb44058eb)

**Confusion Matrix:** The confusion matrix shows that the model has identified all fraud cases (99) in the test set. However, there are no normal transactions predicted as normal, which means there are a significant number of false positives. This aligns with the precision score being close to zero — most normal transactions are misclassified as frauds.

-----
## **2.2 One-Class SVM**

### Classification Report and Confusion Matrix:

![1702460576425](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/1b8b215c-c225-420d-8ffb-60d91b0a87a0)

**1)** For the normal transactions (class 0), the precision is quite high at 0\.98, meaning that when the model predicts a transaction is normal, it is correct 98% of the time\. However, the recall is very low at 0\.10, indicating that the model only correctly identifies 10% of all normal transactions\.

**2)** For the fraudulent transactions (class 1), both precision and recall are very low, at 0\.00 and 0\.09, respectively\. This suggests that while the model identifies 9% of fraudulent transactions, when it does predict a transaction as fraud, it is almost always wrong\.

**3)** The accuracy is 0\.10, which is not meaningful in this context due to the imbalanced nature of the data\.

**4)** The F1-score, which is the harmonic mean of precision and recall, is very low for both classes, indicating a poor performance of the model\.

**5)** The confusion matrix shows that out of 56,863 normal transactions, only 5,758 were correctly identified as normal, while 51,105 were incorrectly flagged as frauds\. Out of 99 frauds, only 9 were correctly identified, with 90 missed\.

![1702460687732](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/35d59ca7-5be2-447a-94eb-67810ac984d5)

**Histogram of Decision Function Scores:** This shows the distribution of the distance from the separating hyperplane for the normal and fraud classes. Ideally, we want to see a clear separation between the two distributions. However, there appears to be significant overlap, indicating that the model is not clearly distinguishing between normal and fraudulent transactions. Moreover, the majority of scores for normal transactions are closer to zero, which could be why there are so many false positives.

![1702460657299](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/ecf2fb6a-00ac-4300-825e-739acca66fba)

**Confusion Matrix:** This visualization confirms the model's tendency to misclassify: it shows a large number of false positives (51,105). This suggests that while the model is capable of detecting fraud (with 9 true positives), it is also flagging a high number of normal transactions as fraud.

![1702460727157](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/4285fd4f-9879-477e-8b06-f192d0ae4518)

**Receiver Operating Characteristic (ROC) Curve:** The ROC curve is usually a tool to evaluate the trade-off between true positive rate (sensitivity) and false positive rate (1-specificity) for different threshold settings of a classification model. However, in our case, the curve stays flat at the bottom and then abruptly rises, suggesting that the model has a very high false positive rate for most thresholds and only begins to correctly classify the positive class (fraud) at very high thresholds. The AUC of 0.04 is indicative of a model that performs poorly, almost as if it is making decisions at random.

![1702460705085](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/2930a7e2-f72b-4ad5-b53b-9e297469c333)

**Precision-Recall Curve:** This plot typically shows the trade-off between precision and recall for different threshold values. In our plot, both precision and recall are low for almost all thresholds, which is not ideal. A good model would show a curve that stays high on the precision axis as recall increases.

-----
## **2.3 Auto-Encoder**

### Confusion Matrix and Classification Report:

![1702461210182](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/ecfab597-7306-4e70-a350-0104fc1313a4)

![1702461302780](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/4b05c92f-2a96-415d-9492-8e3d5f2cb431)

**Reconstruction MSE by Class:** The histogram shows the distribution of reconstruction mean squared error (MSE) for both normal and fraudulent transactions. It seems that the majority of normal transactions have a low MSE, while fraudulent transactions tend to have a higher MSE, although there is still significant overlap between the two. This is a good sign that the autoencoder is learning features representative of normal behavior and that anomalies are being identified by their higher reconstruction error.

![1702461274331](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/611ce683-fdfa-4396-9911-33db19315b01)

**Reconstruction MSE Distribution:** This histogram shows the overall distribution of reconstruction MSE for all transactions. It follows that the majority of transactions are reconstructed with low error, which suggests the model is well-tuned to the "normal" class, as expected in semi-supervised learning scenarios.

**Confusion Matrix:** The confusion matrix output indicates that:

- 51,256 normal transactions were correctly identified (true negatives).
- 5,607 normal transactions were incorrectly flagged as fraudulent (false positives).
- 90 fraudulent transactions were correctly identified (true positives).
- 9 fraudulent transactions were missed (false negatives).

**Classification Report:** The precision for the fraudulent class is very low at 0.02, meaning that many of the transactions that the model flagged as fraud were actually normal. However, the recall for the fraudulent class is high at 0.91, indicating that the model is capable of identifying most of the fraudulent transactions.

Accuracy: The overall accuracy of the model is 0.90, which might seem high, but given the imbalance in the dataset, this metric is not very informative.

-----
## **3. Analysis result of methods**
-----

### Comparison of models

**Gaussian Mixture Model (GMM):**

GMM was used to model the distribution of normal transactions and then used to score how likely it is that new transactions fit that same distribution. Transactions with very low likelihoods were considered anomalies.

**One-Class SVM:**

The One-Class SVM was trained on normal transactions and then used to detect anomalies based on the distance from the decision boundary. Transactions that were far from the learned boundary were labeled as anomalies.

**Autoencoder:**

An autoencoder neural network was trained to reconstruct normal transactions. Anomalies were detected based on the reconstruction error; transactions with high error were considered outliers.

-----
### Results summary and discussion

**Gaussian Mixture Model (GMM):**

**Results Summary:**

The GMM achieved a high recall but suffered from a very low precision, leading to many false positives. The threshold for detecting fraud was set by the quantile of log-likelihood scores, which may not have been the optimal method for threshold determination. Discussion:

The model was sensitive enough to identify most of the fraudulent transactions but at the cost of incorrectly labeling many normal transactions as fraud. Adjusting the number of components or the method for setting the threshold could potentially improve performance. The GMM assumes that data follows a mixture of Gaussian distributions, which might not be the case for complex fraud patterns.

**One-Class SVM:**

**Results Summary:**

The One-Class SVM also had a high recall but with very low precision, similar to the GMM. The large number of false positives indicates that the decision function might be too lenient or the model has not learned an effective boundary. Discussion:

The choice of kernel and hyperparameters (like nu and gamma) are crucial for the One-Class SVM performance and need careful tuning. Given that One-Class SVM only uses the normal data for training, it can struggle if the anomalies are not distinct enough from the normal data in the feature space. This method is less prone to assumptions about the distribution of data, which can be both an advantage and a drawback.

**Autoencoder:**

**Results Summary:**

The autoencoder had better precision than the other two models, though it also flagged a significant number of false positives. The recall was high, meaning the autoencoder was successful at detecting a large proportion of the fraudulent transactions.

**Discussion:**

The reconstruction error is a good indicator of anomalies since it was able to differentiate between normal and fraudulent transactions better than the GMM and One-Class SVM.

The model could be further improved by fine-tuning the architecture, like adding more layers or using different types of layers (e.g., convolutional layers for feature extraction).

Autoencoders are data-driven and learn to capture the underlying patterns in the data, which may make them more robust to different types of fraud.

**Combined Graphs and Values:**

When considering the combined results from all three models, it’s clear that there is a trade-off between recall and precision. High recall is desired in fraud detection to catch as many fraudulent transactions as possible, but not at the expense of flagging too many normal transactions as fraudulent, which would result in low precision.

-----
## **4. Research Extension: Combining Gaussian Mixture Model (GMM) and Autoencoder for Anomaly Detection**
-----

In the pursuit of enhancing fraud detection in credit card transactions, we explore a combined approach that leverages the strengths of Gaussian Mixture Models (GMM) and Autoencoders. Here's how the integration of these two models can lead to a more robust anomaly detection system:

Step-by-Step Integration Process:

1. **Feature Compression with Autoencoder**:
   1. An Autoencoder is first trained exclusively on normal transaction data to learn a compact and informative representation of the data.
   1. This unsupervised learning model focuses on minimizing the reconstruction error, effectively capturing the underlying patterns of normal transactions.
1. **Data Transformation**:
   1. The trained encoder part of the Autoencoder is then used to transform the entire dataset (including both normal and anomalous transactions) into a lower-dimensional feature space.
   1. This transformation is expected to highlight features that are most representative of normal behavior, thereby amplifying anomalies in the data.
1. **Anomaly Clustering with GMM**:
   1. A GMM is subsequently trained on the encoded data from the Autoencoder. The GMM attempts to model the data as a mixture of multiple Gaussian distributions, with each distribution representing a cluster.
   1. Since GMM is a soft-clustering algorithm, it assigns a probability to each instance being part of a given cluster, rather than a hard classification.
1. **Anomaly Detection**:
   1. Using the GMM, we classify transactions based on their cluster probabilities. Transactions that fall into clusters with low probabilities (potentially representing anomalies) are flagged for further investigation.
   1. The combined approach utilizes both the reconstruction error from the Autoencoder and the cluster probabilities from the GMM for classifying a transaction as normal or anomalous.

Advantages of the Combined Model:

- **Improved Feature Space**: Autoencoders can reduce noise and dimensionality, providing a cleaner feature space for GMM to work with.
- **Enhanced Detection**: GMM benefits from the Autoencoder's ability to emphasize variations in the data, potentially improving the separation between normal and anomalous transactions.
- **Robustness**: The combined model is less likely to be influenced by outliers or non-essential variations in the data, making it more robust to various types of fraud.

Implementation Considerations:

- **Model Training**: Both models should be trained in sequence, with the Autoencoder being trained first, followed by the GMM on the encoded features.
- **Hyperparameter Tuning**: The number of components in GMM and the dimensionality of the encoded space in the Autoencoder are critical hyperparameters that need careful tuning.
- **Cluster Analysis**: Post-training, a thorough analysis of the clusters formed by the GMM can provide insights into which clusters are likely to correspond to fraudulent transactions.

By fusing the capabilities of Autoencoders and GMMs, we create a powerful tool for anomaly detection that capitalizes on the feature extraction prowess of Autoencoders and the probabilistic clustering of GMMs. This synergy could be the key to advancing fraud detection methodologies.

-----
### Model Performance Analysis

![1702461349614](https://github.com/cwru-courses/csds440project-f23-2/assets/143857493/f1a3811e-a4ca-4f8f-bcab-2836bdd14787)

The confusion matrix and the obtained performance metrics provide important insights into the model's capabilities:

- **Recall (Approx. 93.94%)**: This high value indicates the model's strength in identifying most fraudulent transactions. In fraud detection, a high recall is crucial because failing to detect fraud can have significant consequences.
- **Precision (Approx. 0.37%)**: The extremely low precision suggests that the model labels many non-fraudulent transactions as fraudulent. This could lead to a high operational cost if every flagged transaction needs to be reviewed manually.
- **F1 Score (Approx. 0.73%)**: As a measure that balances precision and recall, the low F1 score indicates that the model is not effectively balancing these metrics. The model's utility is diminished by the number of false positives it generates.
- **F2 Score (Approx. 1.8%)**: Given that the F2 score weighs recall more than precision, this higher score is more relevant in scenarios where missing actual fraud is more critical than false positives. However, the score is still relatively low, suggesting room for improvement.

Confusion Matrix Interpretation

The confusion matrix visualizes the model's classification accuracy. In the context of fraud detection, the matrix shows that while the model is adept at identifying fraudulent transactions, it also misclassifies a large number of normal transactions as fraudulent.


-----
## **5.Bibliography**
-----

- Zhao, B., Wen, X., Han, K. "Learning Semi-supervised Gaussian Mixture Models for Generalized Category Discovery."
- Lee, D.-H. "Pseudo-Label: The Simple and Efficient Semi-Supervised Learning Method for Deep Neural Networks."

requirements:

Credit Card Transactions Dataset

package pandas

package sklearn

package numpy

package matplotlib

package seaborn

package keras


