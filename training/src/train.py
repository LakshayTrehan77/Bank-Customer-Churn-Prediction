from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df, target_col: str, test_size=0.2, random_state=42):
    """
    Train a RandomForest model.

    Args:
        df (pd.DataFrame): Preprocessed data
        target_col (str): Name of target column

    Returns:
        model: Trained model
        X_test, y_test: Test data for evaluation
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    print("Model training completed!")

    # Save model
    joblib.dump(model, "rf_model.pkl")
    print("Model saved as rf_model.pkl")

    return model, X_test, y_test
