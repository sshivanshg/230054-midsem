# Dataset Documentation

## Synthetic Ranking Dataset

### Overview
This folder contains a synthetic toy dataset specifically designed to evaluate the Latent Structural SVM (CCCP-based) method from Yu & Joachims (ICML 2009) on a learning-to-rank task.

### Files
- **train_data.npy** - Synthetic training dataset (queries, documents, features, relevance labels)
- **test_data.npy** - Synthetic test dataset (same structure as train_data)
- **scaler.npy** - StandardScaler object fitted on training features for preprocessing

### Dataset Characteristics

| Property | Value |
|----------|-------|
| Number of queries (train) | 16 |
| Number of queries (test) | 4 |
| Documents per query | 50 |
| Feature dimension | 10 |
| Problem type | Learning-to-rank (binary relevance) |
| Total training examples | ~800 query-document pairs |
| Total test examples | ~200 query-document pairs |
| Data split | 80% train (by query), 20% test (by query) |

### Data Format

Each dataset (train/test) is a **list of dicts** (one per query), each with:

```python
{
  'query_id': int,              # 1–20 (train: 1–16, test: 17–20)
  'X': ndarray (n_docs, 10),    # Feature matrix for documents in this query (normalized)
  'y': ndarray (n_docs,)        # Binary relevance: 0 or 1 per document
}
```

So `train_data[i]['X']` has shape `(50, 10)` and `train_data[i]['y']` has shape `(50,)`.

### Data Generation Process

The synthetic dataset was generated in **Task 2.1** (`task_2_1.ipynb`) using the following procedure:

1. **Sampling**: For each query, 50 documents were created with random feature vectors
2. **Relevance Labels**: Binary relevance was assigned using a sigmoid function based on feature sum:
   - P(relevant=1) = sigmoid(sum(features))
   - Approximately 40-50% of documents are marked as relevant
3. **Preprocessing**: 
   - StandardScaler fitted on training features (mean=0, std=1)
   - Same scaler applied to test data (prevents data leakage)
4. **Train-Test Split**: Split by query ID (not by individual pairs) to prevent leakage:
   - Training: query_id 1–16 (16 queries)
   - Test: query_id 17–20 (4 queries)

### Motivation for Toy Dataset

The original paper (Yu & Joachims 2009) used the OHSUMED medical retrieval dataset with 106 queries and thousands of features. The toy dataset was chosen because:

1. **Computational Efficiency**: Enables rapid iteration and experimentation
2. **Interpretability**: Small enough to visualize and debug algorithm steps
3. **Problem Type Match**: Binary relevance ranking mirrors the paper's learning-to-rank task
4. **Validation**: Demonstrates that the CCCP algorithm works on new domains, not just the paper's data

### Limitations Compared to the Paper

| Factor | Paper (OHSUMED) | Toy Dataset |
|--------|-----------------|-------------|
| Number of queries | 106 | 20 |
| Features per doc | 25 (LETOR) | 10 |
| Relevance labels | Graded (0-5 scale) | Binary |
| Domain | Medical retrieval | Synthetic |
| Dataset size | ~16,000 pairs | ~1,000 pairs |

These differences explain modest performance improvements in the toy dataset compared to large-scale benchmarks in the paper.

### How the Dataset is Used

The dataset flows through the following tasks:

1. **Task 2.1** - Generated and saved to disk
2. **Task 2.2** - Loaded and used to train the full LatentStructuralSVM model
3. **Task 2.3** - Results are reported and compared against the paper
4. **Task 3.1** - Same data used to test the ablated (no H-step) variant
5. **Task 3.2** - Same data used to test the ablated (no regularization) variant

### Reproducibility

To regenerate the dataset:
```bash
jupyter notebook task_2_1.ipynb
```

The notebook uses `np.random.seed(42)` to ensure reproducibility. All data files are deterministically generated and can be recreated from scratch.

### Loading the Data

```python
import numpy as np
from pathlib import Path

# Path: use 'partB/data' when run from repo root, 'data' when run from partB/
data_dir = Path('partB/data') if Path('partB/data').exists() else Path('data')
train_data = np.load(data_dir / 'train_data.npy', allow_pickle=True)
test_data = np.load(data_dir / 'test_data.npy', allow_pickle=True)
scaler_load = np.load(data_dir / 'scaler.npy', allow_pickle=True)
scaler = scaler_load.item()  # np.save stores object as 0-d array; .item() recovers StandardScaler

# train_data / test_data: numpy array of dicts (len 16 and 4). Each dict has 'query_id', 'X', 'y'
# train_data[i]['X'].shape == (50, 10), train_data[i]['y'].shape == (50,)
X_q0 = train_data[0]['X']
y_q0 = train_data[0]['y']
```

### Verified Structure (as on disk)

| Check | Expected | Verified |
|-------|----------|----------|
| `len(train_data)` | 16 | ✓ |
| `len(test_data)` | 4 | ✓ |
| `train_data[i]['X'].shape` | (50, 10) | ✓ |
| `train_data[i]['y'].shape` | (50,) | ✓ |
| Keys per query | `query_id`, `X`, `y` | ✓ |
| Total train pairs | 16×50 = 800 | ✓ |
| Total test pairs | 4×50 = 200 | ✓ |
| `scaler` after `.item()` | `StandardScaler` with `mean_.shape (10,)` | ✓ |

Tasks 2.2, 2.3, 3.1, 3.2 all load from `partB/data/` (or `data/` when cwd is partB) and use `query['X']`, `query['y']` only; they do not use `scaler` (normalization is already applied in Task 2.1 before save).

### References

- Original task in paper: Section 5, pp. 8-9 (Ranking Application)
- Dataset generation code: Task 2.1, Code Cell 3
- Evaluation metrics: Task 2.2, Code Cells 5-6 (Precision@5, NDCG@5)
