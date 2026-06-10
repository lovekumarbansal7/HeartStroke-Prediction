import streamlit as st
import pandas as pd
import joblib


model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title('Heart Stroke Prediction Zone')
st.markdown('Enter the following details to predict the likelihood of a heart stroke:')

age = st.slider('Age',18, 100, 40)
sex = st.selectbox('Sex', ['M', 'F'])
chest_pain = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
cholesterol = st.number_input('Cholesterol (mg/dl)', min_value=100, max_value=600, value=200) #100 600 200 direct bhi likh skte
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0,1])
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
max_hr = st.slider('Max Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise-Induced Angina', ['Y', 'N'])
oldpeak = st.number_input('Oldpeak (ST Depression)', min_value=0.0, max_value=6.0, value=1.0)
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

if st.button('Predict'):
    raw_input = {
        'age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0] 

    if prediction == 1:
        st.error('High risk of heart stroke. Please consult a doctor immediately.')
    else:
        st.success('Low risk of heart stroke. Maintain a healthy lifestyle and regular check-ups.')
        






