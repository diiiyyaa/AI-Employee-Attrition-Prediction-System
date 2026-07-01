import pandas as pd 

#read the dataset
df = pd.read_csv(r"data\WA_Fn-UseC_-HR-Employee-Attrition.csv")


#First 5 rows of the dataset
print("\n First 5 rows of the dataset: \n")
print(df.head())

#Print information about the dataset
print( "\n Dataset Information: \n")
print(df.info())


## Shape
print("\n========== SHAPE ==========")
print(df.shape)

#Columns
# Column names
print("\n========== COLUMNS ==========")
print(df.columns)

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DESCRIBE ==========")
print(df.describe())

print("\n========== DESCRIBE ==========")
print(df.describe())