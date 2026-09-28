import streamlit as st
import joblib
import pandas as pd

# Load models
linear_model = joblib.load('linear.sav')
logistic_model = joblib.load('logi.sav')


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="ABC Ltd Employee Decision Support",
    page_icon="👔",
    layout="centered"
)


# ---------------- CUSTOM UI ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef7ff, #f8f0ff);
}

.main-title {
    text-align: center;
    color: #4B2E83;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #555555;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    color: #2563EB;
    font-size: 24px;
    font-weight: 600;
    margin-top: 20px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.10);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">👔 ABC Ltd Employee Decision Support</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict employee retention and estimate monthly salary</div>',
    unsafe_allow_html=True
)


# ---------------- INPUTS ----------------

st.markdown(
    '<div class="section-title">👤 Employee Information</div>',
    unsafe_allow_html=True
)

JobLevel = st.number_input(
    'Job Level',
    min_value=1,
    max_value=5,
    value=2
)

TotalWorkingYears = st.number_input(
    'Total Working Years',
    min_value=0,
    max_value=40,
    value=5
)

Age = st.number_input(
    'Age',
    min_value=18,
    max_value=60,
    value=30
)

YearsAtCompany = st.number_input(
    'Years at Company',
    min_value=0,
    max_value=40,
    value=3
)

YearsInCurrentRole = st.number_input(
    'Years in Current Role',
    min_value=0,
    max_value=20,
    value=3
)

YearsWithCurrManager = st.number_input(
    'Years with Current Manager',
    min_value=0,
    max_value=20,
    value=3
)

JobInvolvement = st.number_input(
    'Job Involvement',
    min_value=1,
    max_value=4,
    value=3
)

JobSatisfaction = st.number_input(
    'Job Satisfaction',
    min_value=1,
    max_value=4,
    value=3
)

StockOptionLevel = st.number_input(
    'Stock Option Level',
    min_value=0,
    max_value=3,
    value=1
)

OverTime = st.selectbox(
    'Overtime',
    ['No', 'Yes']
)


# Convert Overtime to the same format used during model training
OverTime = 1 if OverTime == 'Yes' else 0


# ---------------- INPUT DATA ----------------

input_data = pd.DataFrame([{
    'JobLevel': JobLevel,
    'TotalWorkingYears': TotalWorkingYears,
    'Age': Age,
    'YearsAtCompany': YearsAtCompany,
    'YearsInCurrentRole': YearsInCurrentRole,
    'YearsWithCurrManager': YearsWithCurrManager,
    'JobInvolvement': JobInvolvement,
    'JobSatisfaction': JobSatisfaction,
    'StockOptionLevel': StockOptionLevel,
    'OverTime': OverTime
}])


# ---------------- PREDICTION ----------------

if st.button('🔍 Analyze Employee', use_container_width=True):

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

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    if attrition_prediction == 1:

        st.error(
            f"⚠️ The employee is predicted to **LEAVE**."
        )

    else:

        st.success(
            f"✅ The employee is predicted to **STAY**."
        )

    st.write(
        f"**Probability of Staying:** {attrition_probability[0]:.2%}"
    )

    st.write(
        f"**Probability of Leaving:** {attrition_probability[1]:.2%}"
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # ---------------- SALARY RESULT ----------------

    st.markdown(
        '<div class="section-title">💰 Estimated Monthly Salary</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.success(
        f"💰 **Estimated Monthly Salary to Offer: ₹{salary_prediction:,.0f}**"
    )

    st.markdown('</div>', unsafe_allow_html=True)
