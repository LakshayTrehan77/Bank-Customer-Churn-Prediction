import joblib
import pandas as pd
import os
from app.schemas import CustomerData


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")


try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
   
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

def predict_churn(data: CustomerData) -> int:
   
    df = pd.DataFrame([data.model_dump()])  
    
   
    df = pd.get_dummies(df, columns=['gender', 'country'], drop_first=True)
    
   
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
            
    df = df[model_features]
    prediction = model.predict(df)
    return int(prediction[0])