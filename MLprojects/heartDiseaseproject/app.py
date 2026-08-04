import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("Logistic_Regression_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("heart strokes prediction")
st.markdown("provide the following details")
Age =st.slider("Age",18,100,40) 
Sex = st.selectbox("Sex",["M","F"])
chest_pain = st.selectbox("Chest pain type",["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting Blood pressure(mm Hg)",80,200,120)
cholestrol = st.number_input("cholestrol (mg/DL )",100,600,200)
Fasting_bs = st.selectbox("Fasting blood sugar > 120 mg/DL",[0,1])
Resting_ECG = st.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate",60 ,220 ,150)
exercise_angina = st.selectbox("Exercise-induced-angina",["Y","N"])
oldPeak = st.slider("oldpeak (ST Depression)",0.0 ,6.0,1.0)
st_slope = st.selectbox("ST slope",["Up","Flat","Down"])

if st.button("predict"):
    # Create a raw input dictionary
    raw_input = {
        'Age': Age,
        'RestingBP': resting_bp,
        'Cholesterol': cholestrol,
        'FastingBS': Fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldPeak,
        'Sex_' + Sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + Resting_ECG: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")