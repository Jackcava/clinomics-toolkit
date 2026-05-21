import pandas as pd
import pytest

from clinomics_toolkit.normalization import zscore_normalize, log_transform


def test_zscore_normalize():
    df = pd.DataFrame({
        "gene_a": [1, 2, 3],
        "gene_b": [4, 5, 6],
    })

    result = zscore_normalize(df)

    assert round(result["gene_a"].mean(), 6) == 0
    assert round(result["gene_b"].mean(), 6) == 0


def test_zscore_raises_on_zero_variance():
    df = pd.DataFrame({
        "gene_a": [1, 1, 1],
    })

    with pytest.raises(ValueError):
        zscore_normalize(df)


def test_log_transform():
    df = pd.DataFrame({
        "gene_a": [0, 1, 2],
    })

    result = log_transform(df)

    assert result.shape == df.shape