import pandas as pd

from clinomics_toolkit.preprocessing import clean_column_names


def test_clean_column_names():
    df = pd.DataFrame({
        " Patient ID ": [1, 2],
        "Age at Onset": [10, 20],
        "CRP (mg/L)": [5.2, 8.1],
    })

    cleaned = clean_column_names(df)

    assert list(cleaned.columns) == [
        "patient_id",
        "age_at_onset",
        "crp_mgl",
    ]