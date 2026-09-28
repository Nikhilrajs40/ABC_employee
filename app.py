import streamlit as st
import joblib
import pandas as pd

# =========================================================
# LOAD MODELS
# =========================================================

linear_model = joblib.load("linear.sav")
logistic_model = joblib.load("logi.sav")


# =========================================================
# PAGE CONFIG
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

/* ---------------- PAGE ---------------- */

.stApp {
    background: #F5F7FB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}


/* ---------------- HEADER ---------------- */

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 16px;
    color: #667085;
    margin-bottom: 30px;
}


/* ---------------- SECTION TITLES ---------------- */

.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #172033;
    margin-bottom: 18px;
}


/* ---------------- INPUT CARD ---------------- */

.input-card {
    background: white;
    border-radius: 18px;
    padding: 28px 30px;
    border: 1px solid #E4E7EC;
    box-shadow: 0px 5px 18px rgba(16,24,40,0.06);
}


/* ---------------- LABELS ---------------- */

.stNumberInput label,
.stSelectbox label {
    color: #344054 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}


/* ---------------- NUMBER INPUT ---------------- */

.stNumberInput input {
    color: #172033 !important;
    background-color: white !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

.stNumberInput > div > div {
    background: white !important;
    border: 1px solid #D0D5DD !important;
    border-radius: 10px !important;
}


/* ---------------- SELECTBOX ---------------- */

/* Main selectbox */
.stSelectbox [data-baseweb="select"] {
    background-color: white !important;
    border-radius: 10px !important;
}

/* Selected value */
.stSelectbox [data-baseweb="select"] * {
    color: #172033 !important;
}

/* Dropdown menu */
[data-baseweb="menu"] {
    background-color: white !important;
    border: 1px solid #D0D5DD !important;
}

/* Dropdown options */
[data-baseweb="menu"] * {
    color: #172033 !important;
}

/* Hovered option */
[data-baseweb="menu"] [role="option"]:hover {
    background-color: #EEF2FF !important;
    color: #172033 !important;
}


/* ---------------- BUTTON ---------------- */

.stButton > button {
    width: 100%;
    height: 52px;
    margin-top: 18px;

    background: linear-gradient(
        90deg,
        #4F46E5,
        #6366F1
    );

    color: white !important;
    border: none;
    border-radius: 11px;

    font-size: 17px;
    font-weight: 700;

    box-shadow: 0px 5px 12px rgba(79,70,229,0.25);
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #4338CA,
        #4F46E5
    );

    color: white !important;
}


/* ---------------- RIGHT RESULT CARD ---------------- */

.result-card {
    background: white;
    border-radius: 18px;
    padding: 28px 30px;
    border: 1px solid #E4E7EC;
    box-shadow: 0px 5px 18px rgba(16,24,40,0.06);
    margin-bottom: 20px;
}


/* Result title */

.result-title {
    font-size: 15px;
    font-weight: 700;
    color: #667085;
    margin-bottom: 10px;
}


/* Main prediction */

.prediction-stay {
    font-size: 27px;
    font-weight: 800;
    color: #16803C;
    margin-bottom: 15px;
}

.prediction-leave {
    font-size: 27px;
    font-weight: 800;
    color: #D92D20;
    margin-bottom: 15px;
}


/* Probability */

.probability-label {
    font-size: 14px;
    color: #667085;
    margin-top: 8px;
}

.probability-value {
    font-size: 17px;
    font-weight: 700;
    color: #172033;
}


/* Salary */

.salary-label {
    font-size: 15px;
    font-weight: 700;
    color: #667085;
}

.salary-value {
    font-size: 36px;
    font-weight: 850;
    color: #172033;
    margin-top: 5px;
}

.salary-description {
    font-size: 14px;
    color: #667085;
    margin-top: 8px;
}


/* ---------------- EMPTY OUTPUT ---------------- */

.empty-card {
    background: white;
    border: 1px dashed #D0D5DD;
    border-radius: 18px;
    padding: 55px 30px;
    text-align: center;
    color: #667085;
}

.empty-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

.empty-title {
    font-size: 19px;
    font-weight: 700;
    color: #344054;
}

.empty-text {
    font-size: 14px;
    margin-top: 5px;
}


/* ---------------- HORIZONTAL LINE ---------------- */

.divider {
    height: 1px;
    background: #EAECF0;
    margin: 20px 0;
}


/* Hide Streamlit menu/footer */

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
# LEFT + RIGHT LAYOUT
# =========================================================

left, right = st.columns(
    [1.05, 0.95],
    gap="large"
)


# =========================================================
# LEFT SIDE — INPUTS
# =========================================================

with left:

    st.markdown(
        '<div class="section-title">👤 Employee Information</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    # Row 1
    c1, c2 = st.columns(2)

    with c1:
        JobLevel = st.number_input(
            "Job Level",
            min_value=1,
            max_value=5,
            value=2
        )

    with c2:
        Age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=30
        )

    # Row 2
    c1, c2 = st.columns(2)

    with c1:
        TotalWorkingYears = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=5
        )

    with c2:
        YearsAtCompany = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=3
        )

    # Row 3
    c1, c2 = st.columns(2)

    with c1:
        YearsInCurrentRole = st.number_input(
            "Years in Current Role",
            min_value=0,
            max_value=20,
            value=3
        )

    with c2:
        YearsWithCurrManager = st.number_input(
            "Years with Current Manager",
            min_value=0,
            max_value=20,
            value=3
        )

    # Row 4
    c1, c2 = st.columns(2)

    with c1:
        JobInvolvement = st.number_input(
            "Job Involvement",
            min_value=1,
            max_value=4,
            value=3
        )

    with c2:
        JobSatisfaction = st.number_input(
            "Job Satisfaction",
            min_value=1,
            max_value=4,
            value=3
        )

    # Row 5
    c1, c2 = st.columns(2)

    with c1:
        StockOptionLevel = st.number_input(
            "Stock Option Level",
            min_value=0,
            max_value=3,
            value=1
        )

    with c2:
        OverTimeChoice = st.selectbox(
            "Overtime",
            ["No", "Yes"],
            index=0
        )

    st.markdown('</div>', unsafe_allow_html=True)


    # Convert Yes/No to model value
    OverTime = 1 if OverTimeChoice == "Yes" else 0


    # =====================================================
    # INPUT DATA
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
# RIGHT SIDE — OUTPUT
# =========================================================

with right:

    st.markdown(
        '<div class="section-title">📊 Prediction Results</div>',
        unsafe_allow_html=True
    )

    if analyze:

        # ---------------------------------------------
        # LOGISTIC REGRESSION
        # ---------------------------------------------

        attrition_prediction = logistic_model.predict(
            input_data
        )[0]

        attrition_probability = logistic_model.predict_proba(
            input_data
        )[0]


        # ---------------------------------------------
        # LINEAR REGRESSION
        # ---------------------------------------------

        salary_prediction = linear_model.predict(
            input_data
        )[0]


        # ---------------------------------------------
        # RETENTION RESULT
        # ---------------------------------------------

        if attrition_prediction == 1:

            st.markdown(
                f"""
                <div class="result-card">

                    <div class="result-title">
                        EMPLOYEE RETENTION
                    </div>

                    <div class="prediction-leave">
                        ⚠️ Employee Likely to Leave
                    </div>

                    <div class="divider"></div>

                    <div class="probability-label">
                        Probability of Staying
                    </div>

                    <div class="probability-value">
                        {attrition_probability[0]:.2%}
                    </div>

                    <div class="probability-label">
                        Probability of Leaving
                    </div>

                    <div class="probability-value">
                        {attrition_probability[1]:.2%}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="result-card">

                    <div class="result-title">
                        EMPLOYEE RETENTION
                    </div>

                    <div class="prediction-stay">
                        ✅ Employee Likely to Stay
                    </div>

                    <div class="divider"></div>

                    <div class="probability-label">
                        Probability of Staying
                    </div>

                    <div class="probability-value">
                        {attrition_probability[0]:.2%}
                    </div>

                    <div class="probability-label">
                        Probability of Leaving
                    </div>

                    <div class="probability-value">
                        {attrition_probability[1]:.2%}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ---------------------------------------------
        # SALARY RESULT
        # ---------------------------------------------

        st.markdown(
            f"""
            <div class="result-card">

                <div class="result-title">
                    💰 ESTIMATED MONTHLY SALARY
                </div>

                <div class="salary-value">
                    ₹{salary_prediction:,.0f}
                </div>

                <div class="salary-description">
                    Estimated monthly salary based on employee characteristics.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    else:

        # ---------------------------------------------
        # BEFORE ANALYSIS
        # ---------------------------------------------

        st.markdown(
            """
            <div class="empty-card">

                <div class="empty-icon">
                    📊
                </div>

                <div class="empty-title">
                    No Prediction Yet
                </div>

                <div class="empty-text">
                    Enter employee information on the left
                    and click <b>Analyze Employee</b>.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )
