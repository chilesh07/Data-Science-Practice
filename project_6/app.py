from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model = joblib.load("attrition_model.pkl")

# This must match training columns
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

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Fill missing columns with defaults
    full_data = {}
    for col in ALL_COLUMNS:
        full_data[col] = data.get(col, 0)

    df = pd.DataFrame([full_data])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    return jsonify({
        "prediction": pred,
        "probability": round(float(prob), 3)
    })

if __name__ == "__main__":
    app.run(debug=True)
