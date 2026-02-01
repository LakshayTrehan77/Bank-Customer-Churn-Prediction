from fastapi import FastAPI
from app.schemas import CustomerData , PredictionResponse
from app.predict import predict_churn

app = FastAPI(title = "Bank Customer Churn Prediction")

@app.get("/")
def home():
    return {"message" : "Churn API Prediction Running"}

@app.post("/predict" , response_model=PredictionResponse)
def predict(data : CustomerData):
    churn = predict_churn(data)
    return {"churn" : churn}