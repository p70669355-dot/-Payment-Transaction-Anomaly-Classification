# Payment Transaction Anomaly Classification

A machine learning and FinTech project that classifies payment transactions into **routine and anomalous categories** using transaction characteristics such as amount, time, frequency, merchant/category indicators, and account-history features.

The project follows an end-to-end workflow from **data research and exploratory data analysis to machine learning, evaluation, and a Streamlit web application**.

---

## 📌 Project Overview

Financial transaction systems generate a large number of transactions every day. Identifying unusual or anomalous transactions is important for detecting potentially suspicious behavior and reducing financial risk.

This project develops a **binary classification system** that analyzes transaction-related features and predicts whether a new transaction belongs to a routine or anomalous category.

The project focuses on:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Behavioral pattern analysis
* Classification model development
* Model evaluation
* Error analysis
* False-positive investigation
* Explainable prediction
* Streamlit-based prototype application

> **Note:** This project is an educational prototype and is not intended for production financial or fraud-detection deployment.

---

## 🎯 Problem Statement

Classify transaction records into **routine and anomalous categories** using transaction characteristics.

The system should learn patterns from historical transaction data and use those patterns to classify a new transaction.

---

## 🎯 Project Objectives

* Understand the structure and characteristics of the transaction dataset.
* Identify missing values, duplicates, outliers, and inconsistent records.
* Perform exploratory data analysis to understand transaction behavior.
* Analyze relationships between transaction features and the target class.
* Prepare the data for machine learning.
* Build suitable classification models.
* Compare model performance using appropriate evaluation metrics.
* Analyze classification errors, particularly false positives.
* Develop a simple Streamlit application for making predictions.
* Provide probability/risk information where supported by the model.
* Document the complete methodology in a technical paper.

---

## 🔍 Research Direction

The project mainly studies:

* Behavioral patterns in payment transactions
* Routine vs anomalous transaction characteristics
* Feature relationships
* Class imbalance
* Outliers
* Classification errors
* False-positive cases
* Model performance

Special attention is given to **false positives**, because incorrectly identifying a normal transaction as anomalous can negatively affect legitimate users.

---

## 📥 Expected Inputs

The model can use transaction-related characteristics such as:

* Transaction amount
* Transaction time
* Transaction frequency
* Merchant/category indicators
* Account-history features
* Other relevant transaction attributes available in the dataset

The exact features depend on the selected dataset.

---

## 📤 Expected Output

For a new transaction, the system provides:

```text
Predicted Class: Routine / Anomalous
```

Where supported, the application can also display:

```text
Prediction Probability
Risk Indication
```

Example:

```text
Transaction Status: Anomalous
Risk Probability: 87.4%
```

---

# 🏗️ Project Workflow

```text
                    Transaction Dataset
                           |
                           ↓
                  Data Understanding
                           |
                           ↓
                    Data Cleaning
                           |
                           ↓
                        EDA
                           |
                           ↓
                Feature Engineering
                           |
                           ↓
                 Data Preprocessing
                           |
                           ↓
              Train / Test Split
                           |
                           ↓
               Classification Models
                           |
                           ↓
                    Model Evaluation
                           |
                           ↓
                  Error Analysis
                           |
                           ↓
              Best Suitable Model
                           |
                           ↓
              Save Trained Model
                           |
                           ↓
                 Streamlit Prototype
                           |
                           ↓
                  New Transaction
                           |
                           ↓
                    Prediction
```

---

# 📊 Project Phases

## 01. Research

The first phase focuses on understanding the problem domain and dataset.

Activities include:

* Understanding the problem statement
* Understanding the dataset
* Identifying the target variable
* Understanding transaction features
* Studying anomalous transaction patterns
* Reviewing relevant classification approaches

---

## 02. Data + EDA

The dataset is examined and prepared before model development.

### Data Analysis

The following checks are performed:

* Dataset shape
* Data types
* Missing values
* Duplicate records
* Class distribution
* Unique values
* Statistical summary
* Outliers
* Feature distributions
* Relationships between variables

### EDA Visualizations

Possible visualizations include:

* Class distribution
* Transaction amount distribution
* Feature distributions
* Correlation heatmap
* Box plots
* Transaction frequency analysis
* Time-based patterns
* Category/merchant analysis

---

## 03. Machine Learning Model

The project uses supervised classification techniques.

Candidate models include:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree

The models are trained using the prepared transaction dataset and evaluated using the same test data methodology.

The final model is selected based on the evaluation results rather than assuming a particular algorithm in advance.

---

# 📈 Model Evaluation

Because anomaly classification can be affected by class imbalance, multiple evaluation metrics are considered.

### Accuracy

Measures the overall percentage of correctly classified transactions.

### Precision

Measures how many transactions predicted as anomalous were actually anomalous.

### Recall

Measures how many actual anomalous transactions were successfully detected.

### F1-Score

Provides a balance between precision and recall.

### Confusion Matrix

Shows:

```text
                 Predicted
              Routine  Anomalous

Actual
Routine          TN        FP

Anomalous        FN        TP
```

Where:

* **TP** = True Positive
* **TN** = True Negative
* **FP** = False Positive
* **FN** = False Negative

### ROC-AUC

ROC-AUC can be used to evaluate how well the model separates the two classes across different classification thresholds.

---

# 🔎 Error Analysis

A major focus of this project is understanding **classification errors**.

Particularly:

### False Positives

Normal transactions incorrectly classified as anomalous.

### False Negatives

Anomalous transactions incorrectly classified as routine.

The project investigates possible reasons behind these errors by examining the relevant transaction characteristics.

---

# 🧠 Features

The project can work with features related to:

| Feature Category | Examples                        |
| ---------------- | ------------------------------- |
| Transaction      | Amount, transaction type        |
| Time             | Hour, date/time                 |
| Frequency        | Number of recent transactions   |
| Merchant         | Merchant/category indicators    |
| Account          | Account-history characteristics |
| Behavioral       | Historical transaction patterns |

The actual features used depend on the dataset selected for implementation.

---

# 🖥️ Streamlit Prototype

A simple web-based prototype is developed using **Streamlit**.

The application allows a user to enter transaction information and receive a machine learning prediction.

### Application Flow

```text
User enters transaction details
            ↓
      Input validation
            ↓
     Data preprocessing
            ↓
      Trained ML model
            ↓
        Prediction
            ↓
Routine / Anomalous
            ↓
 Probability / Risk indication
```

### Example Interface

The application may contain fields such as:

```text
Transaction Amount
Transaction Time
Transaction Frequency
Merchant Category
Account History
        ↓
     Predict
        ↓
Prediction: Anomalous
Risk Probability: XX%
```

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Web Application

* Streamlit

### Development Environment

* Google Colab / Jupyter Notebook
* GitHub

---

# 📁 Project Structure

```text
Payment-Transaction-Anomaly-Classification/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── payment_transaction_anomaly.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── app/
│   └── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── technical-paper/
    └── project-paper.pdf
```

> File and folder names can be changed according to the final implementation.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/payment-transaction-anomaly-classification.git
```

Move into the project directory:

```bash
cd payment-transaction-anomaly-classification
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

---

# 📦 Requirements

Typical dependencies include:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
```

The final `requirements.txt` should contain the exact packages used by the completed project.

---

# 📊 Expected Results

The completed project should provide:

* Cleaned transaction dataset
* Exploratory data analysis
* Feature analysis
* Trained classification model
* Classification metrics
* Confusion matrix
* ROC-AUC where applicable
* Error analysis
* False-positive analysis
* Saved trained model
* Streamlit prediction application
* Technical project documentation

---

# 🔐 Important Disclaimer

This project is created for **educational and academic purposes**.

It is not a production-ready banking or financial fraud-detection system.

Real-world financial systems require:

* Large-scale transaction data
* Strong security
* Privacy protection
* Regulatory compliance
* Real-time monitoring
* Robust fraud detection systems
* Continuous model monitoring
* Extensive validation

The Streamlit application developed in this project is a **prototype demonstration** of the machine learning workflow.

---

# 🚀 Future Scope

The project can be extended by adding:

* Real-time transaction monitoring
* Advanced anomaly detection algorithms
* Ensemble machine learning models
* Hyperparameter optimization
* Explainable AI techniques
* SHAP-based feature explanations
* Real-time dashboards
* Alert/notification systems
* User authentication
* Transaction history
* Database integration
* API-based model serving
* Cloud deployment
* Continuous model monitoring

---

# 📚 Technical Paper

The technical paper for this project can contain:

1. Abstract
2. Introduction
3. Problem Definition
4. Related Work
5. Dataset
6. Methodology
7. Exploratory Data Analysis
8. Model Development
9. Results
10. Discussion
11. Limitations
12. Future Scope
13. Conclusion
14. References

---

# 📋 Final Deliverables

The final project includes:

* Source code
* Jupyter/Colab notebook
* Dataset / dataset source citation
* Cleaned dataset
* Trained machine learning model
* `requirements.txt`
* README documentation
* Streamlit application
* Technical paper
* Project presentation
* Final demonstration

---

# 👩‍💻 Author

**Priyanka**
Artificial Intelligence & Data Science Engineering Student
GSSSIETW, Mysuru

---

## ⭐ Project Summary

**Payment Transaction Anomaly Classification** is an end-to-end **FinTech + Machine Learning** project that studies transaction behavior, prepares transaction data, develops classification models, evaluates their performance, investigates errors, and demonstrates predictions through a Streamlit web application.

**Domain:** FinTech
**Task:** Binary Classification
**Application:** Transaction Anomaly Detection
**Duration:** 10 Days
**Type:** Final Capstone Project
**Status:** In Development
