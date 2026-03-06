#!/usr/bin/env python3
"""
Re-verify partB dataset structure and compatibility with Tasks 2.2, 3.1, 3.2.
Run from repo root: python partB/data/verify_data.py
Or from partB: python data/verify_data.py
"""
import numpy as np
from pathlib import Path

def main():
    # Resolve data dir (run from repo root or partB/)
    data_dir = Path('partB/data') if (Path('partB/data') / 'train_data.npy').exists() else Path('data')
    if not (data_dir / 'train_data.npy').exists():
        print("ERROR: train_data.npy not found. Run partB/task_2_1.ipynb first.")
        return 1

    train = np.load(data_dir / 'train_data.npy', allow_pickle=True)
    test = np.load(data_dir / 'test_data.npy', allow_pickle=True)
    scaler_load = np.load(data_dir / 'scaler.npy', allow_pickle=True)

    errors = []
    # Type: numpy array of dicts
    if not isinstance(train, np.ndarray) or len(train) != 16:
        errors.append(f"train_data: expected len 16, got {len(train)}")
    if not isinstance(test, np.ndarray) or len(test) != 4:
        errors.append(f"test_data: expected len 4, got {len(test)}")

    # Structure: each element is dict with query_id, X, y
    for i, (data, name, n_expected) in enumerate([
        (train, 'train', 16),
        (test, 'test', 4),
    ]):
        for j in range(len(data)):
            q = data[j]
            if not isinstance(q, dict):
                errors.append(f"{name}[{j}] is {type(q).__name__}, expected dict")
                continue
            for key in ('query_id', 'X', 'y'):
                if key not in q:
                    errors.append(f"{name}[{j}] missing key '{key}'")
            if 'X' in q and q['X'].shape != (50, 10):
                errors.append(f"{name}[{j}]['X'].shape = {q['X'].shape}, expected (50, 10)")
            if 'y' in q and q['y'].shape != (50,):
                errors.append(f"{name}[{j}]['y'].shape = {q['y'].shape}, expected (50,)")

    # Rubric: ≥100 samples, ≥2 features
    n_train_pairs = sum(train[i]['X'].shape[0] for i in range(len(train)))
    n_test_pairs = sum(test[i]['X'].shape[0] for i in range(len(test)))
    n_features = train[0]['X'].shape[1]
    if n_train_pairs + n_test_pairs < 100:
        errors.append(f"Total samples {n_train_pairs + n_test_pairs} < 100 (rubric requirement)")
    if n_features < 2:
        errors.append(f"Feature dim {n_features} < 2 (rubric requirement)")

    # Scaler
    try:
        scaler = scaler_load.item()
        if not hasattr(scaler, 'mean_') or scaler.mean_.shape[0] != 10:
            errors.append(f"Scaler .mean_.shape = {getattr(scaler, 'mean_', None)}")
    except Exception as e:
        errors.append(f"Scaler load: {e}")

    if errors:
        print("VERIFICATION FAILED:")
        for e in errors:
            print("  -", e)
        return 1

    print("Data verification PASSED")
    print(f"  train: {len(train)} queries, {n_train_pairs} pairs, X shape (50, 10), y (50,)")
    print(f"  test:  {len(test)} queries, {n_test_pairs} pairs")
    print(f"  features: {n_features} (rubric: ≥2)")
    print(f"  total samples: {n_train_pairs + n_test_pairs} (rubric: ≥100)")
    print(f"  scaler: StandardScaler with mean_.shape (10,)")
    print("  All keys per query: query_id, X, y — compatible with task_2_2, task_3_1, task_3_2")
    return 0

if __name__ == '__main__':
    exit(main())
