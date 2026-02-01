import pandas as pd

def encode_categorical(df: pd.DataFrame, categorical_cols: list) -> pd.DataFrame:
    """
    Encode categorical columns using one-hot encoding.

    Args:
        df (pd.DataFrame): Dataframe with categorical features
        categorical_cols (list): List of categorical column names

    Returns:
        pd.DataFrame: Dataframe with encoded categorical features
    """
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df
