import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Create figure with 2 plots
plt.figure(figsize=(14,5))

# -------- First Graph --------
plt.subplot(1,2,1)

sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

# -------- Second Graph --------
plt.subplot(1,2,2)

sns.countplot(x="OverTime", hue="Attrition", data=df)
plt.title("Overtime vs Attrition")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()