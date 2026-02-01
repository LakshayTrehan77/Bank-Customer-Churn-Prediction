# main.py

from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.feature_engineering import encode_categorical
from src.train import train_model
from src.evaluate import evaluate_model
import json

def main():

    # Loading data
    df = load_data("data/Bank Customer Churn Prediction.csv")

    # Preprocessing data
    drop_cols = ['customer_id']
    scale_cols = ['credit_score', 'balance', 'estimated_salary', 'age']
    df = preprocess_data(df, drop_cols=drop_cols, scale_cols=scale_cols)

    # Feature engineering (encode categorical)
    categorical_cols = ['gender', 'country']
    df = encode_categorical(df, categorical_cols=categorical_cols)

    # Training model
    model, X_test, y_test = train_model(df, target_col='churn')

    # Metrics to JSON
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }

    
    metrics_path = "artifacts/metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrics saved at {metrics_path}")

  
    print("Trained model saved at artifacts/model_v1.pkl")

if __name__ == "__main__":
    main()
