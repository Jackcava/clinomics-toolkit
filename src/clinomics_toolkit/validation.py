import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate that input is a non-empty pandas DataFrame
    with unique column names.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    if df.empty:
        raise ValueError("DataFrame is empty")

    if df.columns.duplicated().any():
        raise ValueError("Duplicate column names detected")


def check_sample_alignment(
    metadata: pd.DataFrame,
    features: pd.DataFrame
) -> None:
    """
    Check whether metadata and feature matrices have aligned sample IDs.
    """
    if not metadata.index.equals(features.index):
        raise ValueError("Metadata and feature matrix indices are not aligned")