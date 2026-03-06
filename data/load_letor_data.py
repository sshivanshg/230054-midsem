"""
LETOR Dataset Loader for Latent Structural SVM Experiments

Dataset: Microsoft LETOR 1.0 (OHSUMED medical information retrieval)
Source: https://www.microsoft.com/en-us/research/project/letor-learning-rank-information-retrieval/

This dataset is used for the "Optimizing Precision@k" experiment in:
Yu & Joachims (2009) "Learning Structural SVMs with Latent Variables", ICML.

Format (SVM-light style):
    label qid:query_id feature_id:value feature_id:value ... #docid = doc_id

Features (25 total for OHSUMED):
    1-4: Term Frequency features (body, anchor, title, URL)
    5-8: IDF features
    9-12: TF-IDF features  
    13-16: Document Length features
    17-20: BM25 features
    21-25: Language Model features (LMIR)
"""

import numpy as np
from pathlib import Path
from collections import defaultdict


def parse_letor_line(line):
    """
    Parse a single line from LETOR format.
    
    Returns:
        label: int (relevance label, 0/1/2 for OHSUMED)
        qid: int (query ID)
        features: dict (feature_id -> value)
        docid: str (document ID from comment)
    """
    parts = line.strip().split()
    if len(parts) < 3:
        return None
    
    label = int(parts[0])
    
    qid = None
    features = {}
    docid = None
    
    in_comment = False
    for part in parts[1:]:
        if part == '#':
            in_comment = True
            continue
        if in_comment:
            if part.startswith('docid'):
                continue
            elif part == '=':
                continue
            else:
                docid = part
        elif part.startswith('qid:'):
            qid = int(part.split(':')[1])
        elif ':' in part:
            fid, val = part.split(':')
            features[int(fid)] = float(val)
    
    return label, qid, features, docid


def load_letor_file(filepath):
    """
    Load a LETOR format file.
    
    Returns:
        X: numpy array (n_samples, n_features)
        y: numpy array (n_samples,) - relevance labels
        qids: numpy array (n_samples,) - query IDs
        docids: list of document IDs
    """
    samples = []
    labels = []
    qids = []
    docids = []
    
    n_features = 25  # OHSUMED has 25 features
    
    with open(filepath, 'r') as f:
        for line in f:
            result = parse_letor_line(line)
            if result is None:
                continue
            
            label, qid, features, docid = result
            
            feature_vec = np.zeros(n_features)
            for fid, val in features.items():
                if 1 <= fid <= n_features:
                    feature_vec[fid - 1] = val
            
            samples.append(feature_vec)
            labels.append(label)
            qids.append(qid)
            docids.append(docid)
    
    return (np.array(samples), np.array(labels), 
            np.array(qids), docids)


def load_ohsumed_fold(fold=1, data_dir=None):
    """
    Load OHSUMED data for a specific fold (1-5).
    
    Args:
        fold: int, fold number (1-5)
        data_dir: path to LETOR data directory
        
    Returns:
        X_train, y_train, qid_train: training data
        X_val, y_val, qid_val: validation data
        X_test, y_test, qid_test: test data
    """
    if data_dir is None:
        data_dir = Path(__file__).parent / 'letor' / 'OHSUMED' / 'Data'
    else:
        data_dir = Path(data_dir)
    
    fold_dir = data_dir / f'Fold{fold}'
    
    train_file = fold_dir / 'trainingset.txt'
    if not train_file.exists():
        train_file = fold_dir / 'trainingset.TXT'
    
    val_file = fold_dir / 'validationset.txt'
    test_file = fold_dir / 'testset.txt'
    
    X_train, y_train, qid_train, _ = load_letor_file(train_file)
    X_val, y_val, qid_val, _ = load_letor_file(val_file)
    X_test, y_test, qid_test, _ = load_letor_file(test_file)
    
    return (X_train, y_train, qid_train,
            X_val, y_val, qid_val, 
            X_test, y_test, qid_test)


def load_ohsumed_all(data_dir=None):
    """Load all OHSUMED data (not split by fold)."""
    if data_dir is None:
        data_dir = Path(__file__).parent / 'letor' / 'OHSUMED' / 'Data'
    else:
        data_dir = Path(data_dir)
    
    all_file = data_dir / 'All' / 'OHSUMED.txt'
    return load_letor_file(all_file)


def group_by_query(X, y, qids):
    """
    Group samples by query ID.
    
    Returns:
        dict: qid -> (X_query, y_query) for each query
    """
    queries = defaultdict(lambda: {'X': [], 'y': []})
    
    for i in range(len(qids)):
        qid = qids[i]
        queries[qid]['X'].append(X[i])
        queries[qid]['y'].append(y[i])
    
    result = {}
    for qid, data in queries.items():
        result[qid] = (np.array(data['X']), np.array(data['y']))
    
    return result


def compute_precision_at_k(y_true, scores, k):
    """
    Compute Precision@k for a single query.
    
    Args:
        y_true: array of relevance labels (0/1/2, where >0 is relevant)
        scores: array of predicted scores
        k: number of top documents to consider
        
    Returns:
        precision@k value
    """
    n_relevant = np.sum(y_true > 0)
    if n_relevant == 0:
        return 0.0
    
    k = min(k, len(y_true))
    top_k_indices = np.argsort(scores)[::-1][:k]
    relevant_in_top_k = np.sum(y_true[top_k_indices] > 0)
    
    return relevant_in_top_k / k


def evaluate_precision_at_k(queries, model, k_values=[1, 3, 5, 10]):
    """
    Evaluate Precision@k across all queries.
    
    Args:
        queries: dict from group_by_query
        model: sklearn model with predict method
        k_values: list of k values to evaluate
        
    Returns:
        dict: k -> mean precision@k
    """
    results = {k: [] for k in k_values}
    
    for qid, (X_q, y_q) in queries.items():
        scores = model.predict(X_q) if hasattr(model, 'predict') else model @ X_q.T
        
        for k in k_values:
            p_at_k = compute_precision_at_k(y_q, scores, k)
            results[k].append(p_at_k)
    
    return {k: np.mean(vals) for k, vals in results.items()}


def print_dataset_stats(X, y, qids, name="Dataset"):
    """Print dataset statistics."""
    unique_queries = np.unique(qids)
    
    print("=" * 50)
    print(f"{name} Statistics")
    print("=" * 50)
    print(f"Total samples: {len(y)}")
    print(f"Number of queries: {len(unique_queries)}")
    print(f"Feature dimension: {X.shape[1]}")
    print(f"Relevance distribution:")
    for label in sorted(np.unique(y)):
        count = np.sum(y == label)
        print(f"  Label {label}: {count} ({100*count/len(y):.1f}%)")
    print(f"Avg documents per query: {len(y) / len(unique_queries):.1f}")
    print("=" * 50)


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).parent)
    
    print("Loading OHSUMED dataset (all data)...")
    X, y, qids, docids = load_ohsumed_all()
    print_dataset_stats(X, y, qids, "OHSUMED (All)")
    
    print("\nLoading OHSUMED Fold 1...")
    (X_train, y_train, qid_train,
     X_val, y_val, qid_val,
     X_test, y_test, qid_test) = load_ohsumed_fold(1)
    
    print_dataset_stats(X_train, y_train, qid_train, "Training Set (Fold 1)")
    print_dataset_stats(X_test, y_test, qid_test, "Test Set (Fold 1)")
    
    print("\nGrouping test data by query...")
    test_queries = group_by_query(X_test, y_test, qid_test)
    print(f"Number of test queries: {len(test_queries)}")
    
    print("\nSample query:")
    sample_qid = list(test_queries.keys())[0]
    X_q, y_q = test_queries[sample_qid]
    print(f"  Query ID: {sample_qid}")
    print(f"  Documents: {len(y_q)}")
    print(f"  Relevant (label>0): {np.sum(y_q > 0)}")
    
    print("\nBaseline: Random ranking Precision@k")
    np.random.seed(42)
    dummy_results = {}
    for k in [1, 3, 5, 10]:
        p_at_k_list = []
        for qid, (X_q, y_q) in test_queries.items():
            random_scores = np.random.rand(len(y_q))
            p_at_k_list.append(compute_precision_at_k(y_q, random_scores, k))
        dummy_results[k] = np.mean(p_at_k_list)
    
    print(f"  P@1: {dummy_results[1]:.3f}")
    print(f"  P@3: {dummy_results[3]:.3f}")
    print(f"  P@5: {dummy_results[5]:.3f}")
    print(f"  P@10: {dummy_results[10]:.3f}")
