import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold


def log_transform(df: pd.DataFrame, offset: float = 1.0) -> pd.DataFrame:
    """
    Apply natural log transformation to numeric data.
    """
    if offset <= 0:
        raise ValueError("offset must be greater than 0")

    return np.log(df + offset)


def zscore_normalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply z-score normalization column-wise.
    """
    std = df.std(ddof=0)

    if (std == 0).any():
        raise ValueError("Cannot z-score normalize columns with zero variance")

    return (df - df.mean()) / std


def filter_low_variance_features(
    df: pd.DataFrame,
    threshold: float = 0.0
) -> pd.DataFrame:
    """
    Remove features with variance below or equal to the selected threshold.
    """
    selector = VarianceThreshold(threshold=threshold)
    filtered = selector.fit_transform(df)

    selected_columns = df.columns[selector.get_support()]

    return pd.DataFrame(
        filtered,
        columns=selected_columns,
        index=df.index
    )