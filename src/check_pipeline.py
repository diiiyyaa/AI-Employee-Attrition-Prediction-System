import joblib

pipeline = joblib.load("models/attrition_pipeline.pkl")

print("Features expected by the pipeline:")
print(pipeline.feature_names_in_)