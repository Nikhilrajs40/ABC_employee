import streamlit as st
import joblib
import pandas as pd

# =========================================================
# LOAD MODELS
# =========================================================

linear_model = joblib.load("linear.sav")
logistic_model = joblib.load("logi.sav")


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="ABC Ltd Employee Decision Support",
    page_icon="👔",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ================= PAGE ================= */

.stApp {
    background-color: #F5F7FB;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ================= HEADER ================= */

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 4px;
}

.subtitle {
    font-size: 16px;
    color: #667085;
    margin-bottom: 30px;
}


/* ================= SECTION TITLES ================= */

.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #172033;
    margin-bottom: 16px;
}


/* ================= INPUT CARD ================= */

.input-card {
    background: #FFFFFF;
    border: 1px solid #E4E7EC;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(16, 24, 40, 0.06);
}


/* ================= LABELS ================= */

.stNumberInput label,
.stSelectbox label {
    color: #344054 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}


/* ================= NUMBER INPUT ================= */

.stNumberInput input {
    color: #172033 !important;
    background-color: #FFFFFF !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

.stNumberInput > div > div {
    background-color: #FFFFFF !important;
    border: 1px solid #D0D5DD !important;
    border-radius: 10px !important;
}


/* ================= SELECTBOX ================= */

.stSelectbox [data-baseweb="select"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D0D5DD !important;
    border-radius: 10px !important;
}

.stSelectbox [data-baseweb="select"] span {
    color: #172033 !important;
}

.stSelectbox [data-baseweb="select"] input {
    color: #172033 !important;
}


/* Dropdown */

[data-baseweb="popover"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] [role="option"] {
    color: #172033 !important;
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] [role="option"]:hover {
    background-color: #EEF2FF !important;
}


/* ================= BUTTON ================= */

.stButton > button {
    width: 100%;
    height: 52px;
    margin-top: 20px;

    background: linear-gradient(
        90deg,
        #4F46E5,
        #6366F1
    );

    color: #FFFFFF !important;

    border: none;
    border-radius: 11px;

    font-size: 17px;
    font-weight: 700;

    box-shadow: 0 5px 14px rgba(79, 70, 229, 0.25);
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #4338CA,
        #4F46E5
    );

    color: #FFFFFF !important;
}


/* ================= RESULT CARD ================= */

.result-card {
    background: #FFFFFF;
    border: 1px solid #E4E7EC;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 18px;

    box-shadow: 0 4px 15px rgba(16, 24, 40, 0.06);
}


/* ================= RESULT TEXT ================= */

.result-label {
    color: #667085;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
}

.stay-result {
    color: #16803C;
    font-size: 27px;
    font-weight: 800;
}

.leave-result {
    color: #D92D20;
    font-size: 27px;
    font-weight: 800;
}


/* ================= PROBABILITY ================= */

.probability-row {
    display: flex;
    justify-content: space-between;
    padding: 9px 0;
    border-bottom: 1px solid #EAECF0;
}

.probability-name {
    color: #667085;
    font-size: 14px;
}

.probability-number {
    color: #172033;
    font-size: 15px;
    font-weight: 700;
}


/* ================= SALARY ================= */

.salary-label {
    color: #667085;
    font-size: 14px;
    font-weight: 700;
}

.salary-value {
    color: #172033;
    font-size: 38px;
    font-weight: 850;
    margin-top: 8px;
}

.salary-description {
    color: #667085;
    font-size: 14px;
    margin-top: 8px;
}


/* ================= EMPTY RESULT ================= */

.empty-result {
    background: #FFFFFF;
    border: 1px dashed #D0D5DD;
    border-radius: 18px;
    padding: 65px 25px;
    text-align: center;
}

.empty-icon {
    font-size: 42px;
}

.empty-heading {
    color: #344054;
    font-size: 19px;
    font-weight: 700;
    margin-top: 10px;
}

.empty-text {
    color: #667085;
    font-size: 14px;
    margin-top: 5px;
}


/* ================= HIDE STREAMLIT DEFAULTS ================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">👔 ABC Ltd Employee Decision Support</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Employee retention prediction & monthly salary estimation</div>',
    unsafe_allow_html=True
)


# =========================================================
# MAIN LAYOUT
# =========================================================

left_column, right_column = st.columns(
    [1, 1],
    gap="large"
)


# =========================================================
# LEFT SIDE - EMPLOYEE INPUT
# =========================================================

with left_column:

    st.markdown(
        '<div class="section-title">👤 Employee Information</div>',
        unsafe_allow_html=True
    )

    # -------- JOB LEVEL + AGE --------

    col1, col2 = st.columns(2)

    with col1:
        JobLevel = st.number_input(
            "Job Level",
            min_value=1,
            max_value=5,
            value=2,
            step=1
        )

    with col2:
        Age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=30,
            step=1
        )


    # -------- WORKING YEARS + COMPANY --------

    col1, col2 = st.columns(2)

    with col1:
        TotalWorkingYears = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=5,
            step=1
        )

    with col2:
        YearsAtCompany = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=3,
            step=1
        )


    # -------- CURRENT ROLE + MANAGER --------

    col1, col2 = st.columns(2)

    with col1:
        YearsInCurrentRole = st.number_input(
            "Years in Current Role",
            min_value=0,
            max_value=20,
            value=3,
            step=1
        )

    with col2:
        YearsWithCurrManager = st.number_input(
            "Years with Current Manager",
            min_value=0,
            max_value=20,
            value=3,
            step=1
        )


    # -------- INVOLVEMENT + SATISFACTION --------

    col1, col2 = st.columns(2)

    with col1:
        JobInvolvement = st.number_input(
            "Job Involvement",
            min_value=1,
            max_value=4,
            value=3,
            step=1
        )

    with col2:
        JobSatisfaction = st.number_input(
            "Job Satisfaction",
            min_value=1,
            max_value=4,
            value=3,
            step=1
        )


    # -------- STOCK + OVERTIME --------

    col1, col2 = st.columns(2)

    with col1:
        StockOptionLevel = st.number_input(
            "Stock Option Level",
            min_value=0,
            max_value=3,
            value=1,
            step=1
        )

    with col2:
        OverTimeChoice = st.selectbox(
            "Overtime",
            ["No", "Yes"],
            index=0
        )


    # =====================================================
    # CONVERT OVERTIME
    # =====================================================

    if OverTimeChoice == "Yes":
        OverTime = 1
    else:
        OverTime = 0


    # =====================================================
    # CREATE INPUT DATA
    # =====================================================

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


    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    analyze = st.button(
        "🔍  Analyze Employee",
        use_container_width=True
    )


# =========================================================
# RIGHT SIDE - RESULTS
# =========================================================

with right_column:

    st.markdown(
        '<div class="section-title">📊 Prediction Results</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # BEFORE ANALYSIS
    # =====================================================

    if not analyze:

        st.markdown(
            '<div class="empty-result">'
            '<div class="empty-icon">📊</div>'
            '<div class="empty-heading">No Prediction Yet</div>'
            '<div class="empty-text">'
            'Enter employee information on the left and click '
            '<b>Analyze Employee</b>.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # =====================================================
    # AFTER ANALYSIS
    # =====================================================

    else:

        # -------------------------------------------------
        # LOGISTIC REGRESSION
        # -------------------------------------------------

        attrition_prediction = logistic_model.predict(
            input_data
        )[0]

        attrition_probability = logistic_model.predict_proba(
            input_data
        )[0]


        # -------------------------------------------------
        # LINEAR REGRESSION
        # -------------------------------------------------

        salary_prediction = linear_model.predict(
            input_data
        )[0]


        # =================================================
        # RETENTION RESULT
        # =================================================

        if attrition_prediction == 1:

            st.markdown(
                '<div class="result-card">'
                '<div class="result-label">EMPLOYEE RETENTION</div>'
                '<div class="leave-result">'
                '⚠️ Employee Likely to Leave'
                '</div>'
                '<br>'
                '<div class="probability-row">'
                '<span class="probability-name">'
                'Probability of Staying'
                '</span>'
                '<span class="probability-number">'
                f'{attrition_probability[0]:.2%}'
                '</span>'
                '</div>'
                '<div class="probability-row">'
                '<span class="probability-name">'
                'Probability of Leaving'
                '</span>'
                '<span class="probability-number">'
                f'{attrition_probability[1]:.2%}'
                '</span>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="result-card">'
                '<div class="result-label">EMPLOYEE RETENTION</div>'
                '<div class="stay-result">'
                '✅ Employee Likely to Stay'
                '</div>'
                '<br>'
                '<div class="probability-row">'
                '<span class="probability-name">'
                'Probability of Staying'
                '</span>'
                '<span class="probability-number">'
                f'{attrition_probability[0]:.2%}'
                '</span>'
                '</div>'
                '<div class="probability-row">'
                '<span class="probability-name">'
                'Probability of Leaving'
                '</span>'
                '<span class="probability-number">'
                f'{attrition_probability[1]:.2%}'
                '</span>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )


        # =================================================
        # SALARY RESULT
        # =================================================

        st.markdown(
            '<div class="result-card">'
            '<div class="salary-label">'
            '💰 ESTIMATED MONTHLY SALARY'
            '</div>'
            '<div class="salary-value">'
            f'₹{salary_prediction:,.0f}'
            '</div>'
            '<div class="salary-description">'
            'Estimated monthly salary based on employee characteristics.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
