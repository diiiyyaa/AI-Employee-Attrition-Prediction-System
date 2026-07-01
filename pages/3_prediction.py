import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
pipeline = joblib.load("models/attrition_pipeline.pkl")

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div class='header'>
<h1>🤖 AI Employee Attrition Predictor</h1>
<p>
Predict employee turnover using Machine Learning
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 👤 Employee Information")

left, right = st.columns(2)

# -----------------------------
# LEFT COLUMN
# -----------------------------

with left:

    age = st.slider(
        "Age",
        18,
        60,
        30
    )

    business = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    distance = st.slider(
        "Distance From Home",
        1,
        30,
        5
    )

    education = st.slider(
        "Education",
        1,
        5,
        3
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

    # -----------------------------
# RIGHT COLUMN
# -----------------------------

with right:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    jobrole = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=5000,
        step=500
    )

    overtime = st.selectbox(
        "OverTime",
        [
            "Yes",
            "No"
        ]
    )

    total_years = st.slider(
        "Total Working Years",
        0,
        40,
        10
    )

    years_company = st.slider(
        "Years At Company",
        0,
        40,
        5
    )

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Employee Attrition",
    use_container_width=True
)

# -----------------------------
# PREDICTION
# -----------------------------

if predict:

    input_df = pd.DataFrame({

        "Age":[age],

        "BusinessTravel":[business],

        "Department":[department],

        "DistanceFromHome":[distance],

        "Education":[education],

        "EducationField":[education_field],

        "Gender":[gender],

        "JobRole":[jobrole],

        "MonthlyIncome":[income],

        "OverTime":[overtime],

        "TotalWorkingYears":[total_years],

        "YearsAtCompany":[years_company]

    })

    prediction = pipeline.predict(input_df)[0]

    probability = pipeline.predict_proba(input_df)

    stay_prob = probability[0][
        list(pipeline.classes_).index("No")
    ]

    leave_prob = probability[0][
        list(pipeline.classes_).index("Yes")
    ]
        # -----------------------------
    # RESULT CARD
    # -----------------------------

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:

        if prediction == "Yes":

            st.error("## 🔴 HIGH ATTRITION RISK")

            st.markdown(f"""
**Confidence :** **{leave_prob*100:.2f}%**

This employee is likely to leave the company.
""")

        else:

            st.success("## 🟢 LOW ATTRITION RISK")

            st.markdown(f"""
**Confidence :** **{stay_prob*100:.2f}%**

This employee is likely to stay in the company.
""")

    with col2:

        confidence = max(stay_prob, leave_prob) * 100

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=confidence,

            number={'suffix': "%"},

            title={'text': "Confidence"},

            gauge={

                'axis': {'range': [0, 100]},

                'bar': {'color': "#7C3AED"},

                'steps': [

                    {'range': [0, 50], 'color': "#EF4444"},

                    {'range': [50, 80], 'color': "#F59E0B"},

                    {'range': [80, 100], 'color': "#10B981"}

                ]

            }

        ))

        fig.update_layout(

            height=320,

            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white")

        )

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # HR RECOMMENDATIONS
    # -----------------------------

    st.markdown("## 💡 HR Recommendations")

    recommendations = []

    if overtime == "Yes":
        recommendations.append("✔ Reduce overtime or balance workload.")

    if income < 4000:
        recommendations.append("✔ Consider salary review.")

    if years_company > 8:
        recommendations.append("✔ Discuss career growth opportunities.")

    if total_years > 10:
        recommendations.append("✔ Offer leadership or mentoring roles.")

    if prediction == "Yes":
        recommendations.append("✔ Schedule a retention discussion with the employee.")

    if not recommendations:
        recommendations.append("✔ Employee profile appears healthy. Continue regular engagement.")

    for rec in recommendations:
        st.info(rec)

    # -----------------------------
    # DOWNLOAD REPORT
    # -----------------------------

    report = pd.DataFrame({

        "Prediction":[prediction],

        "Stay Probability":[round(stay_prob*100,2)],

        "Leave Probability":[round(leave_prob*100,2)],

        "Age":[age],

        "Department":[department],

        "Job Role":[jobrole],

        "Monthly Income":[income],

        "OverTime":[overtime]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        "📥 Download Prediction Report",

        data=csv,

        file_name="employee_prediction_report.csv",

        mime="text/csv",

        use_container_width=True

    )

st.markdown("---")

st.markdown(
"""
<center>

### 🤖 AI Employee Attrition Prediction System

Built with ❤️ using Streamlit | Plotly | Scikit-Learn

</center>
""",
unsafe_allow_html=True
)