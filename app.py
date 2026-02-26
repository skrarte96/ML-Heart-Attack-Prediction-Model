# Creates a small Streamlit app to insert data for patients and calculate their risk of Heart Attack

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Title
st.title('Heart Attack Risk Prediction')

# Downloads the best model selected
model = joblib.load('ML_Heart_Attack_Best_Model.pkl')

# Shows that the patient should enter its information
st.write('Enter patient information')

# User inputs

age = st.number_input("Age (years)", min_value=1, max_value=120)
sex = st.selectbox("Sex: 1 = male, 0 = female", [0, 1])
cp = st.selectbox("Chest Pain Type (1-4): 1: typical angina, 2: atypical angina, 3: non-anginal pain 4: asymptomatic", [1,2,3,4])
trestbps = st.number_input("Resting Blood Pressure (in mmHg)")
chol = st.number_input("Cholesterol (in mg/dl)")
fbs = st.selectbox("Fasting Blood Sugar >120 (1=True, 0=False)", [0,1])
restecg = st.selectbox("Resting electrocardiographic results (0-2): 0: normal, 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), 2: showing probable or definite left ventricular hypertrophy by Estes' criteria", [0,1,2])
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina: 1 = Yes, 0 = No", [0,1])
oldpeak = st.number_input("Oldpeak (ST depression induced by exercise relative to rest)")
slope = st.selectbox("Slope (1-3): the slope of the peak exercise ST segment. 1: upsloping, 2: flat, 3: downsloping", [1,2,3])
ca = st.selectbox("Number of major vessels coverered by fluoroscopy (0-3)", [0,1,2,3])
thal = st.selectbox("Thal (3,6,7). 3: normal, 6: fixed defect, 7: reversable defect", [3,6,7])

# Create dictionary with the inputs
input_dict = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

# Create a DataFrame row from the dictionary

input_df = pd.DataFrame([input_dict])

# Creates the predict Button
if st.button('Predict'):
    
    # Predicts the probability based on the input
    probability = model.predict_proba(input_df)[0][1]
    
    # Writes the predicted probability
    st.write(f'Predicted probability of heart disease: {probability: .2f}')
    
    # Emphasizes if it is a High, Moderate or Low Risk
    if probability > 0.7:
        st.warning("High Risk")
    elif probability > 0.4:
        st.info("Moderate Risk")
    else:
        st.success("Low Risk")