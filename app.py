import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Streamlit page configuration
st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the house price.")

# User Inputs
area = st.number_input("Area (sqft)", min_value=500, max_value=5000, value=2500)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3])
age = st.slider("Age of House (Years)", 0, 30, 10)
location = st.slider("Location Score", 1, 9, 5)
distance = st.slider("Distance to City (km)", 1, 50, 10)

house_type = st.selectbox(
    "House Type",
    ["Apartment", "Independent", "Villa"]
)

# Label Encoding
house_mapping = {
    "Apartment": 0,
    "Independent": 1,
    "Villa": 2
}

house_type = house_mapping[house_type]

# Prediction
if st.button("Predict House Price"):

    sample = pd.DataFrame({

        "Area_sqft": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Age_of_House": [age],
        "Location_Score": [location],
        "Distance_to_City": [distance],
        "House_Type": [house_type]

    })

    prediction = model.predict(sample)[0]

    st.success(f"🏡 Predicted House Price: ₹ {prediction:,.2f}")