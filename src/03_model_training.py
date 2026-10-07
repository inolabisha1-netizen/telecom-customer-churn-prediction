import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Load dataset
df = pd.read_csv("cleaned_churn_data.csv")


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


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Create Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)


# Train the model
model.fit(
    X_train,
    y_train
)


print("Model training completed.")

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print("Number of features:", X_train.shape[1])
