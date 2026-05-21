import pandas as pd

from clinomics_toolkit.preprocessing import clean_column_names
from clinomics_toolkit.clinical import encode_categorical_variables
from clinomics_toolkit.normalization import log_transform, zscore_normalize
from clinomics_toolkit.validation import check_sample_alignment


metadata = pd.read_csv("data/sample/clinical_metadata.csv").set_index("sample_id")
expression = pd.read_csv("data/sample/expression_matrix.csv").set_index("sample_id")

metadata = clean_column_names(metadata)
expression = clean_column_names(expression)

check_sample_alignment(metadata, expression)

clinical_encoded = encode_categorical_variables(
    metadata,
    columns=["sex", "disease_status"],
)

expression_log = log_transform(expression)
expression_scaled = zscore_normalize(expression_log)

final_matrix = pd.concat([clinical_encoded, expression_scaled], axis=1)

print("Clinical metadata shape:", metadata.shape)
print("Expression matrix shape:", expression.shape)
print("Final ML-ready matrix shape:", final_matrix.shape)
print(final_matrix.head())
