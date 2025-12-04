# Salary-Prediction-ML-app
The Salary Prediction ML App is an interactive web application built using Streamlit and Machine Learning (Random Forest Regressor).
The Salary Prediction ML App is an interactive web application built using Streamlit and Machine Learning. It predicts the expected salary of an individual based on their age, gender, education level, job title, and years of experience. The app provides an easy-to-use interface and gives instant salary predictions in Indian Rupees (₹).

Features:
   User-Friendly Interface: Enter personal and professional details using number inputs and dropdown menus.
   Accurate Predictions: Uses a pre-trained machine learning model to predict salary based on multiple features.
   Categorical Inputs Encoded: Gender, education level, and job title are automatically encoded for model compatibility.
Steps:
  1)import the salary dataset.
  2)Data Preprocessing(convert categorical data into numerical value and clean missing values).
  3)Split independent feature and dependent feature.
  4)Use train_test_split to split data.
  5)Train the model using Random Forest Regressor Algorithm .
  6)Model predict using test data.
  7)Use Evalution Metrics.(Mean_Squared_Error,r2_score).
  8)I get accuracy 94%.
  9)After i installed my trained model using pickle.
  10)Create a Streamlit user interface.
Input Features:
  Age: 18–70 years
  Gender: Female / Male
  Education Level: PhD, Masters, Bachelor, Diploma, Other
  Job Title: Data Scientist, ML Engineer, Software Engineer, Analyst, Other
  Years of Experience: 0–50 years
  
