import streamlit as st

st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

# Get user inputs
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 30, 200, 70)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Display BMI value
st.write(f"Your BMI is: {bmi:.2f}")

# BMI Categories
st.write("### BMI Categories ###")
st.write("- Underweight: BMI < 18.5") 
st.write("- Normal weight: 18.5 ≤ BMI < 24.9")
st.write("- Overweight: 25 ≤ BMI < 29.9") 
st.write("- Obesity: BMI ≥ 30")

# Interpretation of BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

st.write(f"Based on your BMI, you are classified as: {category}")
