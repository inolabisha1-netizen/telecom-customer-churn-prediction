import pandas as pd

# Load dataset
df = pd.read_csv("churnguard_data.csv")

# Remove unnecessary column
df = df.drop("customerID", axis=1)

# Remove duplicate rows
df = df.drop_duplicates()

# Clean text columns
df["gender"] = df["gender"].str.strip()
df["PaymentMethod"] = df["PaymentMethod"].str.strip()
df["Churn"] = df["Churn"].str.strip().str.title()
df["PhoneService"] = df["PhoneService"].str.strip().str.title()
df["PaperlessBilling"] = df["PaperlessBilling"].str.strip().str.title()

# Standardize Contract values
contract_mapping = {
    "month-to-month": "Month-to-month",
    "Month-to-month": "Month-to-month",
    "One year": "One year",
    "One Year": "One year",
    "one year": "One year",
    "two year": "Two year",
    "Two year": "Two year",
    "Two Year": "Two year"
}

df["Contract"] = (
    df["Contract"]
    .str.strip()
    .replace(contract_mapping)
)

# Standardize InternetService values
internet_mapping = {
    "Fiber optic": "Fiber optic",
    "fiber optic": "Fiber optic",
    "FiberOptic": "Fiber optic",
    "Fibre optic": "Fiber optic",
    "DSl": "DSL",
    "DSL": "DSL",
    "dsl": "DSL",
    "Dsl": "DSL",
    "No": "No",
    "NO": "No",
    "no": "No"
}

df["InternetService"] = (
    df["InternetService"]
    .str.strip()
    .replace(internet_mapping)
)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove invalid tenure values
df = df[df["tenure"] > 0]

# Keep valid MonthlyCharges values
df = df[
    df["MonthlyCharges"].isna() |
    (
        (df["MonthlyCharges"] >= 10) &
        (df["MonthlyCharges"] <= 200)
    )
]

# Fill missing MonthlyCharges
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

# Fill missing TotalCharges
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].mean()
)

# Fill missing tenure
df["tenure"] = df["tenure"].fillna(
    round(df["tenure"].median())
)

# Fill missing InternetService
df["InternetService"] = df["InternetService"].fillna(
    df["InternetService"].mode()[0]
)

# Display final results
print("Cleaned DataFrame Shape:")
print(df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())
