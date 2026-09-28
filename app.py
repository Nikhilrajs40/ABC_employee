import streamlit as st
import joblib
import pandas as pd

# Load models
linear_model = joblib.load("linear.sav")
logistic_model = joblib.load("logi.sav")

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="ABC Ltd Employee Decision Support",
    page_icon="👔",
    layout="centered"
)

# ---------------- CUSTOM UI ----------------

st.markdown("""
<style>

/* Overall page */
.stApp {
    background: #F5F7FB;
}

/* Remove default top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 900px;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #667085;
    margin-bottom: 30px;
}

/* Section heading */
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #172033;
    margin-top: 25px;
    margin-bottom: 18px;
}

/* Input labels */
label,
.stNumberInput label,
.stSelectbox label {
    color: #344054 !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Input containers */
.stNumberInput > div > div,
.stSelectbox > div > div {
    background: white !important;
    border: 1px solid #D0D5DD !important;
    border-radius: 10px !important;
}

/* Input text */
.stNumberInput input {
    color: #172033 !important;
    background: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* Selectbox text */
.stSelectbox div[data-baseweb="select"] {
    background: white !important;
}

.stSelectbox div[data-baseweb="select"] * {
    color: #172033 !important;
}

/* Focus effect */
.stNumberInput > div > div:focus-within,
.stSelectbox > div > div:focus-within {
    border-color: #4F46E5 !important;
    box-shadow: 0 0 0 2px rgba(79,70,229,0.12) !important;
}

/* Input card */
.input-card {
    background: white;
    padding: 25px 30px;
    border-radius: 18px;
    border: 1px solid #E4E7EC;
    box-shadow: 0 4px 15px rgba(16,24,40,0.05);
    margin-bottom: 25px;
}

/* Analyze button */
.stButton > button {
    width: 100%;
    height: 52px;
    background: linear-gradient(90deg, #4F46E5, #6366F1);
    color: white !important;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 5px 12px rgba(79,70,229,0.25);
    margin-top: 15px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #4338CA, #4F46E5);
    color: white !important;
}

/* Result cards */
.result-card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    border: 1px solid #E4E7EC;
    box-shadow: 0 4px 15px rgba(16,24,40,0.06);
    margin-top: 15px;
}

/* Result headings */
.result-heading {
    font-size: 17px;
    font-weight: 700;
    color: #344054;
    margin-bottom: 12px;
}

/* Big result */
.big-result {
    font-size: 28px;
    font-weight: 800;
    color: #172033;
}

/* Probability */
.probability {
    font-size: 15px;
    color: #667085;
    margin-top: 8px;
}

/* Divider */
.divider {
    height: 1px;
    background: #EAECF0;
    margin: 18px 0;
}

/* Hide unnecessary Streamlit elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">👔 ABC Ltd Employee Decision Support</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict employee retention and estimate monthly salary</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT CARD ----------------

st.markdown(
    '<div class="section-title">👤 Employee Information</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-card">', unsafe_allow_html=True)


# First row
col1, col2 = st.columns(2)

with col1:
    JobLevel = st.number_input(
        "Job Level",
        min_value=1,
        max_value=5,
        value=2
    )

with col2:
    Age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )


# Second row
col1, col2 = st.columns(2)

with col1:
    TotalWorkingYears = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=5
    )

with col2:
    YearsAtCompany = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=40,
        value=3
    )


# Third row
col1, col2 = st.columns(2)

with col1:
    YearsInCurrentRole = st.number_input(
        "Years in Current Role",
        min_value=0,
        max_value=20,
        value=3
    )

with col2:
    YearsWithCurrManager = st.number_input(
        "Years with Current Manager",
        min_value=0,
        max_value=20,
        value=3
    )


# Fourth row
col1, col2 = st.columns(2)

with col1:
    JobInvolvement = st.number_input(
        "Job Involvement",
        min_value=1,
        max_value=4,
        value=3
    )

with col2:
    JobSatisfaction = st.number_input(
        "Job Satisfaction",
        min_value=1,
        max_value=4,
        value=3
    )


# Fifth row
col1, col2 = st.columns(2)

with col1:
    StockOptionLevel = st.number_input(
        "Stock Option Level",
        min_value=0,
        max_value=3,
        value=1
    )

with col2:
    OverTime = st.selectbox(
        "Overtime",
        ["No", "Yes"]
    )


st.markdown('</div>', unsafe_allow_html=True)


# ---------------- CONVERT OVERTIME ----------------

OverTime = 1 if OverTime == "Yes" else 0


# ---------------- INPUT DATA ----------------

input_data = pd.DataFrame([{
    "JobLevel": JobLevel,
    "TotalWorkingYears": TotalWorkingYears,
    "Age": Age,
    "YearsAtCompany": YearsAtCompany,
    "YearsInCurrentRole": YearsInCurrentRole,
    "YearsWithCurrManager": YearsWithCurrManager,
    "JobInvolvement": JobInvolvement,
    "JobSatisfaction": JobSatisfaction,
    "StockOptionLevel": StockOptionLevel,
    "OverTime": OverTime
}])


# ---------------- BUTTON ----------------

if st.button("🔍 Analyze Employee", use_container_width=True):

    # Logistic Regression
    attrition_prediction = logistic_model.predict(input_data)[0]
    attrition_probability = logistic_model.predict_proba(input_data)[0]

    # Linear Regression
    salary_prediction = linear_model.predict(input_data)[0]


    # ---------------- RETENTION RESULT ----------------

    st.markdown(
        '<div class="section-title">📊 Employee Retention Prediction</div>',
        unsafe_allow_html=True
    )

    if attrition_prediction == 1:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-heading">Retention Prediction</div>
                <div class="big-result">⚠️ Employee Likely to Leave</div>
                <div class="divider"></div>
                <div class="probability">
                    Probability of Staying: 
                    <b>{attrition_probability[0]:.2%}</b>
                </div>
                <div class="probability">
                    Probability of Leaving: 
                    <b>{attrition_probability[1]:.2%}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-heading">Retention Prediction</div>
                <div class="big-result">✅ Employee Likely to Stay</div>
                <div class="divider"></div>
                <div class="probability">
                    Probability of Staying: 
                    <b>{attrition_probability[0]:.2%}</b>
                </div>
                <div class="probability">
                    Probability of Leaving: 
                    <b>{attrition_probability[1]:.2%}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ---------------- SALARY RESULT ----------------

    st.markdown(
        '<div class="section-title">💰 Estimated Monthly Salary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-heading">Recommended Salary Estimate</div>
            <div class="big-result">
                ₹{salary_prediction:,.0f}
            </div>
            <div class="probability">
                Estimated monthly salary based on employee characteristics.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
