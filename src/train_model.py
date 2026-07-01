import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# ---------------------------------------
# Select Features
# ---------------------------------------

features = [

    "Age",

    "BusinessTravel",

    "Department",

    "DistanceFromHome",

    "Education",

    "EducationField",

    "Gender",

    "JobRole",

    "MonthlyIncome",

    "OverTime",

    "TotalWorkingYears",

    "YearsAtCompany"

]

X = df[features]

y = df["Attrition"]

# ---------------------------------------
# Numerical Columns
# ---------------------------------------

numerical_features = [

    "Age",

    "DistanceFromHome",

    "Education",

    "MonthlyIncome",

    "TotalWorkingYears",

    "YearsAtCompany"

]

# ---------------------------------------
# Categorical Columns
# ---------------------------------------

categorical_features = [

    "BusinessTravel",

    "Department",

    "EducationField",

    "Gender",

    "JobRole",

    "OverTime"

]

# ---------------------------------------
# Preprocessor
# ---------------------------------------

preprocessor = ColumnTransformer(

    transformers=[

        (

            "num",

            StandardScaler(),

            numerical_features

        ),

        (

            "cat",

            OneHotEncoder(handle_unknown="ignore"),

            categorical_features

        )

    ]

)

# ---------------------------------------
# Pipeline
# ---------------------------------------

pipeline = Pipeline(

    steps=[

        ("preprocessor", preprocessor),

        ("model",

         RandomForestClassifier(

             n_estimators=200,

             random_state=42

         ))

    ]

)

# ---------------------------------------
# Split Dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)

# ---------------------------------------
# Train
# ---------------------------------------

pipeline.fit(

    X_train,

    y_train

)

# ---------------------------------------
# Predict
# ---------------------------------------

y_pred = pipeline.predict(

    X_test

)

# ---------------------------------------
# Accuracy
# ---------------------------------------

accuracy = accuracy_score(

    y_test,

    y_pred

)

print("="*50)
print("Random Forest Accuracy")
print("="*50)
print(f"Accuracy : {accuracy:.4f}")

print("\nClassification Report\n")

print(

    classification_report(

        y_test,

        y_pred

    )

)

# ---------------------------------------
# Save Pipeline
# ---------------------------------------

joblib.dump(

    pipeline,

    "models/attrition_pipeline.pkl"

)

print("\n✅ Pipeline Saved Successfully!")