import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# Load dataset
df = pd.read_csv("churnguard_data.csv")


# Separate features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]


# Convert categorical variables into numerical variables
X = pd.get_dummies(
    X,
    drop_first=True
)


# Convert target variable into numerical values
y = y.map({
    "No": 0,
    "Yes": 1
})


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Create and train model
model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)


# Make predictions
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Model Accuracy:")
print(accuracy)


# Classification Report
print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Stay", "Churn"]
    )
)


# Confusion Matrix
print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)
