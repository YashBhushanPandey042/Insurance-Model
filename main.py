import streamlit as st
import joblib 
import numpy as np

lr=joblib.load("my_model.pk1")
st.title("💰 Insurance Premium Predictor")

# User Inputs
age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
bmi = st.number_input("Enter BMI", min_value=21.0, max_value=50.0, step=0.1)
sex = st.radio("Sex", ["Female", "Male"])
smoker = st.radio("Smoker", ["No", "Yes"])
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)

# Convert categorical inputs into encoded values
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

# Predict button
if st.button("Predict Premium"):
    features = np.array([[age, bmi, sex_male, smoker_yes, children]])
    prediction = lr.predict(features)[0]
    st.success(f"Estimated Insurance Premium: ₹ {prediction:,.2f}")