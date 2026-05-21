# Clinomics Toolkit

A lightweight and modular toolkit for rapid preprocessing of clinical and molecular datasets.

`clinomics-toolkit` is designed as a collection of reusable utilities for cleaning, validating, transforming, and preparing biomedical tabular data for downstream machine learning, statistical analysis, and exploratory workflows.

The project aims to provide simple, composable, and analysis-oriented preprocessing functions that can be easily integrated into research pipelines, prototype analyses, and multi-omics workflows.


## Features

- Clinical data preprocessing
- Column name standardization
- Missing value imputation
- Categorical variable encoding
- Expression-like data transformation
- Z-score normalization
- Low-variance feature filtering
- Sample alignment checks
- Lightweight R utilities for expression-style normalization

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/clinomics-toolkit.git
cd clinomics-toolkit
```

## Install in editable mode:

```bash
pip install -e ".[dev]"
```

## Quick start

```python
import pandas as pd

from clinomics_toolkit.preprocessing import clean_column_names
from clinomics_toolkit.normalization import log_transform, zscore_normalize
from clinomics_toolkit.clinical import encode_categorical_variables

df = pd.DataFrame({
    "Patient ID": ["P1", "P2", "P3"],
    "Age at Onset": [12, 24, 31],
    "Sex": ["F", "M", "F"],
    "Gene A": [10, 25, 50],
})

df = clean_column_names(df)

clinical = encode_categorical_variables(
    df[["age_at_onset", "sex"]],
    columns=["sex"]
)

features = log_transform(df[["gene_a"]])
features = zscore_normalize(features)
```

## Running tests

```bash
pytest tests/
```
or:
```bash
bash scripts/run_tests.sh
```

## Roadmap

- Core preprocessing utilities
- Basic clinical variable encoding
- Basic normalization tools
- Validation checks
- Demo notebook
- Synthetic biomedical sample dataset
- Multi-omics feature integration utilities
- Documentation website
- CI with GitHub Actions

## License

MIT License.