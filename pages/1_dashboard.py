import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
df = pd.read_csv(
    "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div class='header'>

<h1>🤖 AI Employee Attrition Analytics Dashboard</h1>

<p>
Monitor employee behaviour, identify attrition trends and
predict employee turnover using Machine Learning.
</p>

</div>
""", unsafe_allow_html=True)

# ===========================
# KPI CALCULATIONS
# ===========================

total_employees = len(df)

attrition = len(
    df[df["Attrition"]=="Yes"]
)

attrition_rate = round(
    attrition/total_employees*100,
    2
)

avg_income = int(
    df["MonthlyIncome"].mean()
)

avg_age = round(
    df["Age"].mean(),
    1
)

# ===========================
# KPI CARDS
# ===========================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card'>
        <h3>👨‍💼 Employees</h3>
        <h1>{total_employees}</h1>
        <p>Total Workforce</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card'>
        <h3>📉 Attrition</h3>
        <h1>{attrition}</h1>
        <p>{attrition_rate:.2f}% Employees Left</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card'>
        <h3>💰 Avg Salary</h3>
        <h1>₹ {avg_income:,}</h1>
        <p>Average Monthly Salary</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='card'>
        <h3>📊 Avg Age</h3>
        <h1>{avg_age:.1f}</h1>
        <p>Employee Age</p>
    </div>
    """, unsafe_allow_html=True)        

# ===========================
# FILTERS
# ===========================

left,right = st.columns(2)

with left:

    department = st.selectbox(
        "Department",
        ["All"] + list(df["Department"].unique())
    )

with right:

    overtime = st.selectbox(
        "OverTime",
        ["All"] + list(df["OverTime"].unique())
    )

filtered_df = df.copy()

if department!="All":
    filtered_df = filtered_df[
        filtered_df["Department"]==department
    ]

if overtime!="All":
    filtered_df = filtered_df[
        filtered_df["OverTime"]==overtime
    ]

st.markdown("---")

# ===========================
# ROW 1
# ===========================

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        filtered_df,
        names="Attrition",
        title="Employee Attrition",
        hole=0.55,
        color="Attrition",
        color_discrete_map={
            "Yes": "#EF4444",
            "No": "#10B981"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    dept = (
        filtered_df.groupby("Department")["Attrition"]
        .value_counts()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        dept,
        x="Department",
        y="Employees",
        color="Attrition",
        barmode="group",
        title="Department-wise Attrition"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================
# ROW 2
# ===========================

col1, col2 = st.columns(2)

with col1:

    overtime_df = (
        filtered_df.groupby("OverTime")["Attrition"]
        .value_counts()
        .reset_index(name="Employees")
    )

    fig = px.bar(
        overtime_df,
        x="OverTime",
        y="Employees",
        color="Attrition",
        title="OverTime Analysis"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.histogram(
        filtered_df,
        x="MonthlyIncome",
        nbins=30,
        title="Monthly Income Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===========================
# ROW 3
# ===========================

job = (
    filtered_df["JobRole"]
    .value_counts()
    .reset_index()
)

job.columns = ["JobRole", "Employees"]

fig = px.bar(
    job,
    x="JobRole",
    y="Employees",
    color="Employees",
    title="Employees by Job Role"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)

# ===========================
# HR SUMMARY
# ===========================

st.markdown("## 📌 HR Insights")

c1, c2, c3 = st.columns(3)

highest_department = df["Department"].value_counts().idxmax()
highest_job = df["JobRole"].value_counts().idxmax()

with c1:
    st.info(f"""
### 👨‍💼 Largest Department

**{highest_department}**
""")

with c2:
    st.warning(f"""
### 💼 Most Common Job Role

**{highest_job}**
""")

with c3:
    st.success(f"""
### 🤖 Machine Learning Model

**Random Forest**

Accuracy: **82.65%**
""")

st.markdown("---")

st.markdown(
    """
    <center>
    <h4 style='color:#94A3B8'>
    Built with ❤️ by Diya Diwakar
    </h4>
    <p style='color:gray'>
    AI Employee Attrition Prediction System • Streamlit • Plotly • Scikit-Learn
    </p>
    </center>
    """,
    unsafe_allow_html=True
)