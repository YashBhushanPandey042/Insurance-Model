import streamlit as st
import numpy as np
import joblib

lr=joblib.load("my_model.pk1")

st.title("💰 Insurance Premium Predictor")

# User Inputs with unique keys
age = st.number_input("Enter Age", min_value=18, max_value=100, step=1, key="age_input")
bmi = st.number_input("Enter BMI", min_value=21.0, max_value=50.0, step=0.1, key="bmi_input")
sex = st.radio("Sex", ["Female", "Male"], key="sex_input")
smoker = st.radio("Smoker", ["No", "Yes"], key="smoker_input")
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, key="children_input")

# Convert categorical inputs into encoded values
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

# Predict button
if st.button("Predict Premium", key="predict_button"):
    features = np.array([[age, bmi, sex_male, smoker_yes, children]])
    prediction = lr.predict(features)[0]
    st.success(f"Estimated Insurance Premium: ₹ {prediction:,.2f}")
