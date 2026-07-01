import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HR Insights",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class='header'>
<h1>📈 HR Analytics & Business Insights</h1>
<p>
Understand workforce trends and identify factors affecting employee attrition.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Workforce Insights")

# -----------------------------
# ROW 1
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    fig = px.box(
        df,
        x="Attrition",
        y="MonthlyIncome",
        color="Attrition",
        title="Monthly Income vs Attrition"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.scatter(
        df,
        x="Age",
        y="MonthlyIncome",
        color="Attrition",
        size="YearsAtCompany",
        hover_data=["JobRole"],
        title="Age vs Monthly Income"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROW 2
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    edu = (
        df.groupby("Education")["Attrition"]
        .value_counts()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        edu,
        x="Education",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Education vs Attrition"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    travel = (
        df.groupby("BusinessTravel")["Attrition"]
        .value_counts()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        travel,
        x="BusinessTravel",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Business Travel vs Attrition"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)
    # -----------------------------
# ROW 3
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    numeric_df = df.select_dtypes(include="number")

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=650
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    gender = (
        df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = ["Gender", "Employees"]

    fig = px.pie(
        gender,
        names="Gender",
        values="Employees",
        hole=0.55,
        title="Gender Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# TOP PAID EMPLOYEES
# -----------------------------

top_salary = df.nlargest(
    10,
    "MonthlyIncome"
)

fig = px.bar(
    top_salary,
    x="EmployeeNumber",
    y="MonthlyIncome",
    color="Department",
    title="Top 10 Highest Paid Employees"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# HR BUSINESS INSIGHTS
# -----------------------------

st.markdown("## 💡 AI Generated HR Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
### 📌 Key Findings

• Total Employees : **{len(df)}**

• Attrition Rate : **{round((df['Attrition']=='Yes').mean()*100,2)}%**

• Average Monthly Income : **₹{int(df['MonthlyIncome'].mean())}**

• Average Age : **{round(df['Age'].mean(),1)} Years**
""")

with col2:

    st.info("""
### 🎯 HR Recommendations

✔ Improve employee engagement.

✔ Review overtime policies.

✔ Conduct retention interviews.

✔ Reward high-performing employees.

✔ Invest in career growth programs.
""")

# -----------------------------
# ATTRITION BY MARITAL STATUS
# -----------------------------

marital = (
    df.groupby("MaritalStatus")["Attrition"]
    .value_counts()
    .reset_index(name="Employees")
)

fig = px.bar(
    marital,
    x="MaritalStatus",
    y="Employees",
    color="Attrition",
    barmode="group",
    title="Marital Status vs Attrition"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
"""
<center>

<h3 style='color:white'>
🤖 AI Employee Attrition Prediction System
</h3>

<p style='color:gray'>
Developed by <b>Diya Diwakar</b><br>
Python • Streamlit • Plotly • Scikit-Learn • Machine Learning
</p>

</center>
""",
unsafe_allow_html=True
)