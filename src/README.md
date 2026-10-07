# 📊 Telecom Customer Churn Prediction

## 📌 Project Overview

Customer churn is a major challenge for telecom companies. When customers leave a service, it can directly affect revenue and business growth.

This project uses **Machine Learning** to predict whether a telecom customer is likely to **Stay** or **Churn** based on customer, service, and billing information.

The project follows a complete machine-learning workflow from data exploration and cleaning to model training and evaluation.

---

## 🎯 Objective

The objective is to develop a binary classification model that can predict customer churn and help telecom companies identify customers who may be at risk of leaving.

### Target Classes

* **Stay**
* **Churn**

---

## 🔄 Project Workflow

The project is divided into four stages:

### 1️⃣ Data Exploration

* Load the dataset
* Understand dataset dimensions
* Inspect data types
* Identify missing values
* Check duplicate records
* Analyze churn distribution
* Examine categorical values

File:

`src/01_data_exploration.py`

---

### 2️⃣ Data Cleaning & Preprocessing

The raw dataset contains missing values and inconsistencies that need to be addressed before machine learning.

The cleaning process includes:

* Removing unnecessary columns
* Removing duplicate records
* Standardizing categorical values
* Converting numerical columns to appropriate data types
* Handling missing values
* Removing invalid tenure records
* Standardizing Internet Service and Contract categories

File:

`src/02_data_cleaning.py`

---

### 3️⃣ Model Training

A **Logistic Regression** model is used for binary classification.

The stage includes:

* Separating features and target
* Encoding categorical variables
* Splitting data into training and testing sets
* Training the Logistic Regression model

File:

`src/03_model_training.py`

---

### 4️⃣ Prediction & Evaluation

The trained model is used to predict whether customers will stay or churn.

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

File:

`src/04_model_evaluation.py`

---

## 🤖 Machine Learning Model

### Logistic Regression

Logistic Regression was selected because customer churn is a **binary classification problem**.

The model predicts one of two outcomes:

```text
0 → Stay
1 → Churn
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**

---

## 📁 Project Structure

```text
telecom-customer-churn-prediction/
│
├── src/
│   ├── 01_data_exploration.py
│   ├── 02_data_cleaning.py
│   ├── 03_model_training.py
│   └── 04_model_evaluation.py
│
├── .gitignore
├── requirements.txt
└── README.md
```
Data Flow:.........

      churnguard_data.csv
              ↓
      Data Exploration
              ↓
      Data Cleaning & Preprocessing
              ↓
      cleaned_churn_data.csv
              ↓
      Logistic Regression
              ↓
      Prediction & Evaluation
---

## 📊 Evaluation Metrics

The model performance is evaluated using:

| Metric           | Purpose                                |
| ---------------- | -------------------------------------- |
| Accuracy         | Overall prediction correctness         |
| Precision        | Correctness of predicted churn cases   |
| Recall           | Ability to identify actual churn cases |
| F1-score         | Balance between precision and recall   |
| Confusion Matrix | Detailed prediction breakdown          |

---

## 💼 Business Use Case

A telecom company can use a churn prediction model to identify customers who are more likely to leave.

These insights can support strategies such as:

* Targeted customer retention campaigns
* Personalized offers
* Service improvements
* Customer engagement initiatives

The goal is not simply to predict churn, but to provide information that can support **proactive customer retention**.

---
## 📂 Dataset

The dataset used for this project is not included in the public repository.

To run the project locally, place the dataset in the project root with the filename:

`churnguard_data.csv`

The dataset is then processed through the four-stage machine-learning workflow.

## 🚀 Future Improvements

Possible improvements to this project include:

* Testing additional classification algorithms
* Hyperparameter tuning
* Feature importance analysis
* Handling class imbalance
* ROC-AUC analysis
* Building a customer churn prediction dashboard
* Deploying the model as a web application

---

## 👩‍💻 Author

**Inol Abisha**

Aspiring AI/ML Engineer
