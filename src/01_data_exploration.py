import pandas as pd

# Load dataset
df = pd.read_csv("churnguard_data.csv")

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Target variable distribution
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

# Unique values in important categorical columns
print("\nContract Values:")
print(df["Contract"].unique())

print("\nInternet Service Values:")
print(df["InternetService"].unique())
