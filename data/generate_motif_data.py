"""
Generate Synthetic Motif Finding Dataset

This script generates synthetic DNA sequences with embedded motifs,
following the format expected by the Latent Structural SVM motif finder.

The original paper used yeast ARS (autonomously replicating sequences)
data from Tom Finley and Uri Keich. Since that specific dataset is not
publicly available, this generates synthetic data for reproduction.

Motif Finding Task:
- Positive sequences contain a motif (repeated DNA pattern)
- Negative sequences are random background
- The latent variable is the position of the motif in positive sequences

Based on: Yu & Joachims (2009) "Learning Structural SVMs with Latent Variables"
"""

import numpy as np
from pathlib import Path


def generate_random_sequence(length, gc_content=0.5):
    """
    Generate a random DNA sequence.
    
    Args:
        length: sequence length
        gc_content: proportion of G+C (default 0.5)
    """
    bases = ['A', 'C', 'G', 'T']
    probs = [(1 - gc_content) / 2, gc_content / 2, gc_content / 2, (1 - gc_content) / 2]
    return ''.join(np.random.choice(bases, size=length, p=probs))


def generate_motif_instance(consensus, mutation_rate=0.15):
    """
    Generate a motif instance by mutating the consensus.
    
    Args:
        consensus: consensus motif sequence
        mutation_rate: probability of mutation per position
    """
    bases = ['A', 'C', 'G', 'T']
    motif = list(consensus)
    
    for i in range(len(motif)):
        if np.random.random() < mutation_rate:
            other_bases = [b for b in bases if b != motif[i]]
            motif[i] = np.random.choice(other_bases)
    
    return ''.join(motif)


def embed_motif(sequence, motif, position=None):
    """
    Embed a motif at a given position in the sequence.
    
    Args:
        sequence: background sequence
        motif: motif to embed
        position: position to embed (random if None)
        
    Returns:
        modified sequence, position where motif was embedded
    """
    if position is None:
        max_pos = len(sequence) - len(motif)
        position = np.random.randint(0, max_pos + 1)
    
    seq_list = list(sequence)
    for i, base in enumerate(motif):
        seq_list[position + i] = base
    
    return ''.join(seq_list), position


def generate_motif_dataset(
    n_positive=100,
    n_negative=100,
    seq_length=200,
    motif_consensus="ACGTACGTACG",  # 11bp motif (used in paper)
    mutation_rate=0.15,
    gc_content=0.5,
    seed=42
):
    """
    Generate a complete motif finding dataset.
    
    Args:
        n_positive: number of sequences containing the motif
        n_negative: number of background sequences
        seq_length: length of each sequence
        motif_consensus: consensus motif sequence
        mutation_rate: mutation rate for motif instances
        gc_content: GC content of background sequences
        seed: random seed
        
    Returns:
        list of (name, label, is_foreground, sequence, motif_position) tuples
    """
    np.random.seed(seed)
    
    data = []
    
    for i in range(n_positive):
        background = generate_random_sequence(seq_length, gc_content)
        motif = generate_motif_instance(motif_consensus, mutation_rate)
        seq, pos = embed_motif(background, motif)
        data.append((f"pos_{i}", 1, 1, seq, pos))
    
    for i in range(n_negative):
        seq = generate_random_sequence(seq_length, gc_content)
        data.append((f"neg_{i}", -1, 0, seq, -1))
    
    np.random.shuffle(data)
    
    return data


def write_latentmotif_format(data, filepath):
    """
    Write dataset in the format expected by svm_motif_learn.
    
    Format: seq_name:label:non_background:seq
    First line is the number of examples.
    """
    with open(filepath, 'w') as f:
        f.write(f"{len(data)}\n")
        for name, label, is_foreground, seq, _ in data:
            f.write(f"{name}:{label}:{is_foreground}:{seq}\n")


def write_fasta_format(data, filepath, include_positions=True):
    """Write dataset in FASTA format (for external tools)."""
    with open(filepath, 'w') as f:
        for name, label, _, seq, pos in data:
            header = f">{name} label={label}"
            if include_positions and pos >= 0:
                header += f" motif_pos={pos}"
            f.write(f"{header}\n{seq}\n")


def print_dataset_stats(data, motif_width):
    """Print dataset statistics."""
    n_positive = sum(1 for d in data if d[1] == 1)
    n_negative = sum(1 for d in data if d[1] == -1)
    seq_lengths = [len(d[3]) for d in data]
    
    print("=" * 50)
    print("Synthetic Motif Dataset Statistics")
    print("=" * 50)
    print(f"Total sequences: {len(data)}")
    print(f"Positive (contains motif): {n_positive}")
    print(f"Negative (background): {n_negative}")
    print(f"Sequence length: {seq_lengths[0]}")
    print(f"Motif width: {motif_width}")
    print("=" * 50)


def create_10fold_splits(data, output_dir, seed=42):
    """Create 10-fold cross-validation splits."""
    np.random.seed(seed)
    indices = np.random.permutation(len(data))
    fold_size = len(data) // 10
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for fold in range(10):
        test_start = fold * fold_size
        test_end = (fold + 1) * fold_size if fold < 9 else len(data)
        
        test_indices = indices[test_start:test_end]
        train_indices = np.concatenate([indices[:test_start], indices[test_end:]])
        
        train_data = [data[i] for i in train_indices]
        test_data = [data[i] for i in test_indices]
        
        write_latentmotif_format(train_data, output_dir / f"fold{fold+1}_train.txt")
        write_latentmotif_format(test_data, output_dir / f"fold{fold+1}_test.txt")
    
    print(f"Created 10-fold splits in {output_dir}")


if __name__ == "__main__":
    import os
    
    output_dir = Path(__file__).parent / 'motif'
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(output_dir)
    
    MOTIF_WIDTH = 11  # Same as used in paper
    CONSENSUS = "ACGTACGTACG"  # Example consensus
    
    print("Generating synthetic motif dataset...")
    data = generate_motif_dataset(
        n_positive=200,
        n_negative=200,
        seq_length=200,
        motif_consensus=CONSENSUS,
        mutation_rate=0.15,
        seed=42
    )
    
    print_dataset_stats(data, MOTIF_WIDTH)
    
    write_latentmotif_format(data, 'motif_all.txt')
    print(f"Wrote: motif_all.txt")
    
    write_fasta_format(data, 'motif_all.fasta')
    print(f"Wrote: motif_all.fasta")
    
    print("\nCreating 10-fold CV splits...")
    create_10fold_splits(data, output_dir)
    
    print("\nSample positive sequence:")
    pos_sample = next(d for d in data if d[1] == 1)
    print(f"  Name: {pos_sample[0]}")
    print(f"  Motif position: {pos_sample[4]}")
    print(f"  Sequence (first 50bp): {pos_sample[3][:50]}...")
    
    print("\nSample negative sequence:")
    neg_sample = next(d for d in data if d[1] == -1)
    print(f"  Name: {neg_sample[0]}")
    print(f"  Sequence (first 50bp): {neg_sample[3][:50]}...")
    
    print("\n✓ Motif dataset generation complete!")
