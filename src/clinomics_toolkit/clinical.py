import pandas as pd


def encode_categorical_variables(
    df: pd.DataFrame,
    columns: list[str],
    drop_first: bool = True
) -> pd.DataFrame:
    """
    One-hot encode selected categorical clinical variables.
    """
    missing = [col for col in columns if col not in df.columns]

    if missing:
        raise ValueError(f"Columns not found in DataFrame: {missing}")

    return pd.get_dummies(df, columns=columns, drop_first=drop_first)


def impute_missing_values(
    df: pd.DataFrame,
    strategy: str = "median"
) -> pd.DataFrame:
    """
    Impute missing values using a simple column-wise strategy.
    Supported strategies: median, mean, mode.
    """
    df = df.copy()

    if strategy not in {"median", "mean", "mode"}:
        raise ValueError("strategy must be one of: median, mean, mode")

    for col in df.columns:
        if strategy == "median":
            value = df[col].median()
        elif strategy == "mean":
            value = df[col].mean()
        else:
            value = df[col].mode().iloc[0]

        df[col] = df[col].fillna(value)

    return df