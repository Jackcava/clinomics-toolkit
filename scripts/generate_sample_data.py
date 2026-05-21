import numpy as np
import pandas as pd


np.random.seed(42)

n_samples = 40
n_genes = 20

sample_ids = [f"S{i:03d}" for i in range(1, n_samples + 1)]

metadata = pd.DataFrame({
    "sample_id": sample_ids,
    "age_at_onset": np.random.randint(1, 60, n_samples),
    "sex": np.random.choice(["F", "M"], n_samples),
    "disease_status": np.random.choice(["case", "control"], n_samples),
})

expression = pd.DataFrame(
    np.random.poisson(lam=50, size=(n_samples, n_genes)),
    columns=[f"gene_{i:03d}" for i in range(1, n_genes + 1)],
)

expression.insert(0, "sample_id", sample_ids)

metadata.to_csv("data/sample/clinical_metadata.csv", index=False)
expression.to_csv("data/sample/expression_matrix.csv", index=False)

print("Sample data generated in data/sample/")
