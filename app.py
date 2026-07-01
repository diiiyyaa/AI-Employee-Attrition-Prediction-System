import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI Employee Attrition Prediction System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# LOAD CSS
# -------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:

    st.markdown("""
    <h1 style='text-align:center;color:#8B5CF6;'>
    🤖 HR AI
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("Employee Attrition Prediction")

    st.markdown("""
    ### 📌 Pages

    📊 Dashboard

    🤖 Prediction

    📈 Insights
    """)

    st.markdown("---")

    st.info("""
    **Tech Stack**

    • Python

    • Scikit-Learn

    • Streamlit

    • Plotly

    • Pandas
    """)

# -------------------------
# HEADER
# -------------------------

st.markdown("""
<div class='header'>

<h1>🤖 AI Employee Attrition Prediction System</h1>

<p>
Analyze employee data,
predict attrition,
and gain business insights.
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------
# KPI CARDS
# -------------------------

col1,col2,col3,col4=st.columns(4)

with col1:

    st.markdown("""
    <div class='card'>

    <h3>👨‍💼 Employees</h3>

    <h1>1470</h1>

    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='card'>

    <h3>📉 Attrition</h3>

    <h1>237</h1>

    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='card'>

    <h3>💰 Avg Income</h3>

    <h1>₹6503</h1>

    </div>
    """,unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class='card'>

    <h3>📊 Avg Age</h3>

    <h1>36.9</h1>

    </div>
    """,unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

st.info("👈 Use the sidebar to navigate to Dashboard, Prediction and Insights pages.")