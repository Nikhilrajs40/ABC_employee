import streamlit as st
import joblib
import pandas as pd

linear_model = joblib.load('linear.sav')
logistic_model = joblib.load('logi.sav')

st.title('ABC Ltd Employee Prediction App')

st.write('Enter employee details to predict Monthly Income and Attrition.')

JobLevel = st.number_input('Job Level', min_value=1, max_value=5, value=2)
TotalWorkingYears = st.number_input('Total Working Years', min_value=0, max_value=40, value=5)
Age = st.number_input('Age', min_value=18, max_value=60, value=30)
YearsAtCompany = st.number_input('Years at Company', min_value=0, max_value=40, value=3)
YearsInCurrentRole = st.number_input('Years in Current Role', min_value=0, max_value=20, value=3)
YearsWithCurrManager = st.number_input('Years with Current Manager', min_value=0, max_value=20, value=3)
JobInvolvement = st.number_input('Job Involvement', min_value=1, max_value=4, value=3)
JobSatisfaction = st.number_input('Job Satisfaction', min_value=1, max_value=4, value=3)
StockOptionLevel = st.number_input('Stock Option Level', min_value=0, max_value=3, value=1)
OverTime = st.selectbox('OverTime', ['No', 'Yes'])

OverTime = 1 if OverTime == 'Yes' else 0

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

if st.button('Predict'):

    income_prediction = linear_model.predict(input_data)[0]

    attrition_prediction = logistic_model.predict(input_data)[0]
    attrition_probability = logistic_model.predict_proba(input_data)[0]

    st.subheader('Prediction Results')

    st.write(f'Predicted Monthly Income: ₹{income_prediction:,.0f}')

    if attrition_prediction == 1:
        st.error('Predicted Attrition: YES (Employee may leave)')
    else:
        st.success('Predicted Attrition: NO (Employee may stay)')

    st.write(f'Probability of Leaving: {attrition_probability[1]:.2%}')
    st.write(f'Probability of Staying: {attrition_probability[0]:.2%}')
