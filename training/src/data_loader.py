import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV.

    Args:
        path (str): Path to CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    df = pd.read_csv(path)
    print(f"Data loaded successfully with shape {df.shape}")
    return df
