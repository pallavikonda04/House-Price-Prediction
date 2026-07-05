# 🏠 House Price Prediction using Decision Tree Regressor

## 📌 Project Description

This project predicts house prices using a **Decision Tree Regressor** based on different property features such as area, bedrooms, bathrooms, house age, location score, distance to the city, and house type.

A Streamlit web application is developed to provide a simple and interactive interface where users can enter house details and get the predicted house price instantly.

---

## 🎯 Objectives

- Predict house prices using Machine Learning.
- Understand the concepts of underfitting, overfitting, and balanced models.
- Build and deploy a simple Streamlit web application.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📊 Dataset

The dataset used in this project is synthetically generated using NumPy. It contains **1,000 records** and is designed to demonstrate the complete machine learning workflow.

### Input Features

- Area (sqft)
- Bedrooms
- Bathrooms
- Age of House
- Location Score
- Distance to City
- House Type

### Target Variable

- House Price

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Decision Tree Regressor

### Models Compared

- Underfitting Model
- Overfitting Model
- Balanced Model (Selected)

---

## 📈 Model Performance

- R² Score: **0.927**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The balanced model achieved the best performance and was selected for prediction.

---

## 💻 Streamlit Application

The application allows users to:

- Enter house details
- Select the house type
- Predict house prices instantly
- View the predicted house price

---

## 📂 Project Structure

```text
House_Price_Prediction/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

### 2. Move to the project folder

```bash
cd House-Price-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🚀 Future Improvements

- Use a real-world housing dataset.
- Compare multiple machine learning algorithms.
- Improve the user interface.
- Add more data visualizations.
- Deploy the application on Streamlit Cloud.



