from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(df: pd.DataFrame, drop_cols=None, scale_cols=None) -> pd.DataFrame:
    """
    Preprocess dataset: drop unnecessary columns and scale numeric features.

    Args:
        df (pd.DataFrame): Raw data
        drop_cols (list, optional): Columns to drop
        scale_cols (list, optional): Columns to scale

    Returns:
        pd.DataFrame: Preprocessed data
    """
    if drop_cols:
        df = df.drop(columns=drop_cols)
    
    if scale_cols:
        scaler = StandardScaler()
        df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    return df
