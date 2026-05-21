import pandas as pd


def load_csv(path: str, index_col: str | int | None = None) -> pd.DataFrame:
    """Load a CSV file as a pandas DataFrame."""
    return pd.read_csv(path, index_col=index_col)


def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save a pandas DataFrame to CSV."""
    df.to_csv(path)