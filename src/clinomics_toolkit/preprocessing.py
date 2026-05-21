import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names by converting them to lowercase,
    replacing spaces with underscores, and removing special characters.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df


def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame with duplicated rows removed."""
    return df.drop_duplicates().copy()