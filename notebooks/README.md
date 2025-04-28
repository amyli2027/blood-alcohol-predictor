# Notebooks Guide
This folder contains Jupyter notebooks used throughout the project. Here’s the order to navigate them to understand our data science process.

### 1. Blood_Alcohol_Content_Exploratory_Data_Analysis.ipynb
Includes useful context for later notebooks such as:
 - Information about the dataset
 - Scatter plots of different potential features against target variable

### 2. Ohio_BAC_Dataset_Pre_Processing.ipynb
Shows the process used to get the dataset ready for model training, saving the processed csv to the data folder.

### 3. Australia_BAC_Dataset_Pre-Processing.ipynb
Includes the same process but for the other dataset

### 4. Ohio_BAC_Model_Training.ipynb
Shows the process used to train and evaluate the model

### 5. Australia_BAC_Model_Training.ipynb
Includes the same process but for the other dataset.

### 6. Model_Selection.ipynb
Explains why we chose to base our model on the Ohio dataset not the Australian one and saves our Ohio dataset model for future use along with its metrics.

### 7. Test_Widmark_Equation.ipynb (optional)
A miscellaneous notebook that tests the standard BAC equation (a.k.a. the Widmark equation) against our dataset.

## Notes
- Several notebooks use functions from the file: model_training_functions.py in the src folder
- The raw and processed datasets the notebooks read from can be found in the data folder
- Outputs such as generated plots, trained model, and model summary may be found in the output folder.

