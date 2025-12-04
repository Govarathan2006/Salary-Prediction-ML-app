import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load Model

import os

model_path = r"C:\Users\govar\OneDrive\Desktop\ML Projects\streamlit\Salary_model.pkl"
model = pickle.load(open(model_path, "rb"))

def predict_salary(age, gender, education, job_title, experience):
    input_data = np.array([[age, gender, education, job_title, experience]])
    prediction = model.predict(input_data)
    return round(prediction[0], 2)

def main():
    st.title("💰 Salary Prediction ML App")

    st.markdown("""
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Salary Prediction App</h2>
        </div>
    """, unsafe_allow_html=True)

    age = st.number_input("Age", min_value=18, max_value=70, step=1)
    gender = st.number_input("Gender (0 = Female, 1 = Male)", min_value=0, max_value=1, step=1)
    education = st.number_input("Education Level (ex: 1–PhD, 2–Masters, 3–Bachelor, etc.)", step=1)
    job_title = st.number_input("Job Title (Encode as number)", step=1)
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)

    result = ""
    if st.button("Predict Salary"):
        result = predict_salary(age, gender, education, job_title, experience)
        st.success(f"💡 Predicted Salary: ₹ {result}")

    if st.button("About"):
        st.text("Developed by Govarathan")
        st.text("Machine Learning Salary Prediction App")

if __name__ == "__main__":
    main()
