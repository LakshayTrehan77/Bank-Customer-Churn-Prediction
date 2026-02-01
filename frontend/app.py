import streamlit as st
import requests

# ⚠️ VERY IMPORTANT
# When using Docker Compose → use service name, NOT localhost
API_URL = "http://backend:8000/predict"

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict churn probability.")

# ---- Input Fields ----

credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure (years)", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
products_number = st.selectbox("Number of Products", [1, 2, 3, 4])
credit_card = st.selectbox("Has Credit Card?", [1, 0])
active_member = st.selectbox("Is Active Member?", [1, 0])
estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 70000.0)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
country = st.selectbox("Country", ["France", "Germany", "Spain"])

# ---- Predict Button ----

if st.button("Predict Churn 🚀"):

    payload = {
        "credit_score": credit_score,
        "age": age,
        "gender": gender,
        "country": country,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            churn = result.get("churn_prediction")

            if churn == 1:
                st.error("⚠️ Customer is likely to CHURN!")
            else:
                st.success("✅ Customer is likely to STAY!")

            st.json(result)

        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error("🚨 Could not connect to backend. Is FastAPI running?")
        st.write(str(e))
