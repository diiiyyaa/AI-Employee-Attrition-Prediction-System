import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# -----------------------------
# Check Missing Values
# -----------------------------
print("Missing Values:\n")
print(df.isnull().sum())

# -----------------------------
# Check Duplicate Rows
# -----------------------------
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

# -----------------------------
# Drop Unnecessary Columns
# -----------------------------
# EmployeeNumber is unique for every employee.
# It does not help in prediction.
df.drop("EmployeeNumber", axis=1, inplace=True)

# -----------------------------
# Label Encoding
# -----------------------------
# Machine Learning models cannot understand text.
# We convert text into numbers.

label_encoder = LabelEncoder()

# Find all object (text) columns
categorical_columns = df.select_dtypes(include=["object"]).columns

# Encode each categorical column
for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])

# -----------------------------
# Verify Data Types
# -----------------------------
print("\nData Types After Encoding:\n")
print(df.dtypes)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("data/cleaned_employee_attrition.csv", index=False)

print("\n✅ Clean dataset saved successfully!")