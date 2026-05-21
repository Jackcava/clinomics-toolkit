import pandas as pd
import pytest

from clinomics_toolkit.validation import validate_dataframe, check_sample_alignment


def test_validate_dataframe_accepts_valid_df():
    df = pd.DataFrame({"a": [1, 2]})
    validate_dataframe(df)


def test_validate_dataframe_rejects_empty_df():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_dataframe(df)


def test_check_sample_alignment():
    metadata = pd.DataFrame(index=["S1", "S2"])
    features = pd.DataFrame(index=["S1", "S2"])

    check_sample_alignment(metadata, features)


def test_check_sample_alignment_raises():
    metadata = pd.DataFrame(index=["S1", "S2"])
    features = pd.DataFrame(index=["S2", "S1"])

    with pytest.raises(ValueError):
        check_sample_alignment(metadata, features)