import streamlit as st
import joblib
import pandas as pd

model = joblib.load("attrition_model.pkl")

ALL_COLUMNS = [
    'Age', 'BusinessTravel', 'DailyRate', 'Department',
    'DistanceFromHome', 'Education', 'EducationField',
    'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
    'JobInvolvement', 'JobLevel', 'JobRole',
    'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'OverTime',
    'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StockOptionLevel',
    'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany',
    'YearsInCurrentRole', 'YearsSinceLastPromotion',
    'YearsWithCurrManager'
]

st.title("Employee Attrition Predictor")

age = st.number_input("Age", 18, 60, 30)
income = st.number_input("Monthly Income", 1000, 20000, 4000)
overtime = st.selectbox("OverTime", ["Yes", "No"])
years = st.number_input("Years at Company", 0, 40, 3)

if st.button("Predict"):
    user_data = {
        "Age": age,
        "MonthlyIncome": income,
        "OverTime": overtime,
        "YearsAtCompany": years
    }

    full_data = {}
    for col in ALL_COLUMNS:
        full_data[col] = user_data.get(col, 0)

    df = pd.DataFrame([full_data])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    st.success(f"Prediction: {pred}")
    st.info(f"Risk: {round(prob,2)}")
