**Credit Card Fraud Detection Project**

Notebook direction: [Semi_supervised_learning_updated_final.ipynb](notebooks/Semi_supervised_learning_updated_final.ipynb)

**Getting Started**

This project involves analyzing credit card transactions to detect fraudulent activities using various semi-supervised learning models. Follow these steps to set up and run the analysis.

**Prerequisites**

- Python environment with Jupyter Notebook
- Access to Google Drive (for dataset storage)

**Dataset Download and Setup**

1. **Download Dataset**:
   1. Visit the Kaggle dataset page: [Credit Card Fraud Detection Dataset](https://www.kaggle.com/code/matheusfacure/semi-supervised-anomaly-detection-survey/input)
   1. Download the dataset, which is provided as a zip file.
1. **Upload Dataset to Google Drive**:
   1. Upload the downloaded zip file to your Google Drive in a desired folder.
1. **Unzipping the Dataset**:
   1. Use the following commands in your Jupyter Notebook to unzip the dataset:

*# Define the path to the zip file and the target folder for unzipping*

*zip\_path = '/content/drive/MyDrive/Card\_fraud\_data/archive (2).zip'*

*unzip\_folder = '/content/drive/MyDrive/Card\_fraud\_data/credit\_card\_fraud\_data'*

*# Unzipping command*

*!unzip -o {zip\_path} -d {unzip\_folder}*


1. After unzipping, you will find the dataset in CSV format.
1. **Running the Notebook**
- Open the Jupyter Notebook in your environment.
- Ensure the path to the CSV file is correctly set in the Notebook:


`       `*file\_path = os.path.join(unzip\_folder, 'creditcard.csv')*

**6** . Run the Notebook cells sequentially to perform the analysis.
