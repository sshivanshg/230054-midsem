"""
Script to load and preprocess the Stanford OCR dataset for Latent Structural SVM experiments.

Dataset: Stanford OCR Letters Dataset
Source: https://ai.stanford.edu/~btaskar/ocr/
Description: Handwritten letters (a-z) from MIT's Spoken Language Systems Group.
             Each letter is a 16x8 binary image.

The dataset contains sequences of letters forming words. This is ideal for
structured prediction (sequence labeling) tasks.
"""

import numpy as np
import pandas as pd
from pathlib import Path


def load_ocr_data(filepath='letter.data'):
    """
    Load the Stanford OCR dataset.
    
    Format of letter.data:
    - Column 0: id (position in sequence)
    - Column 1: letter (a-z)
    - Column 2: next_id (-1 if end of word)
    - Column 3: word_id
    - Column 4: position in word
    - Columns 5-132: 128 binary pixel values (16x8 image)
    
    Returns:
        X: list of numpy arrays, each array is (n_letters, 128) for a word
        y: list of numpy arrays, each array is (n_letters,) letter labels for a word
        letter_to_idx: dict mapping letters to indices
        idx_to_letter: dict mapping indices to letters
    """
    data_path = Path(filepath)
    if not data_path.exists():
        data_path = Path(__file__).parent / filepath
    
    words_X = []
    words_y = []
    
    current_word_id = None
    current_X = []
    current_y = []
    
    letter_to_idx = {chr(ord('a') + i): i for i in range(26)}
    idx_to_letter = {i: chr(ord('a') + i) for i in range(26)}
    
    with open(data_path, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 133:
                continue
                
            letter = parts[1]
            word_id = int(parts[3])
            pixels = np.array([int(p) for p in parts[5:133]], dtype=np.float32)
            
            if current_word_id is None:
                current_word_id = word_id
            
            if word_id != current_word_id:
                if len(current_X) > 0:
                    words_X.append(np.array(current_X))
                    words_y.append(np.array(current_y))
                current_X = []
                current_y = []
                current_word_id = word_id
            
            current_X.append(pixels)
            current_y.append(letter_to_idx[letter])
        
        if len(current_X) > 0:
            words_X.append(np.array(current_X))
            words_y.append(np.array(current_y))
    
    return words_X, words_y, letter_to_idx, idx_to_letter


def get_flat_data(words_X, words_y):
    """
    Flatten word sequences into individual letter samples.
    Useful for standard classification (ignoring sequence structure).
    
    Returns:
        X: numpy array (n_samples, 128)
        y: numpy array (n_samples,)
    """
    X = np.vstack(words_X)
    y = np.concatenate(words_y)
    return X, y


def train_test_split_by_fold(words_X, words_y, fold=0, n_folds=10):
    """
    Split data by fold number (the dataset comes with fold assignments).
    For simplicity, we do a random split here.
    """
    n = len(words_X)
    np.random.seed(42)
    indices = np.random.permutation(n)
    
    test_size = n // n_folds
    test_start = fold * test_size
    test_end = test_start + test_size
    
    test_indices = indices[test_start:test_end]
    train_indices = np.concatenate([indices[:test_start], indices[test_end:]])
    
    X_train = [words_X[i] for i in train_indices]
    y_train = [words_y[i] for i in train_indices]
    X_test = [words_X[i] for i in test_indices]
    y_test = [words_y[i] for i in test_indices]
    
    return X_train, y_train, X_test, y_test


def print_dataset_stats(words_X, words_y, idx_to_letter):
    """Print dataset statistics."""
    n_words = len(words_X)
    n_letters = sum(len(w) for w in words_X)
    word_lengths = [len(w) for w in words_X]
    
    print("=" * 50)
    print("Stanford OCR Dataset Statistics")
    print("=" * 50)
    print(f"Number of words: {n_words}")
    print(f"Total letters: {n_letters}")
    print(f"Average word length: {np.mean(word_lengths):.2f}")
    print(f"Min word length: {min(word_lengths)}")
    print(f"Max word length: {max(word_lengths)}")
    print(f"Feature dimension: 128 (16x8 binary pixels)")
    print(f"Number of classes: 26 (a-z)")
    print("=" * 50)


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).parent)
    
    print("Loading OCR data...")
    words_X, words_y, letter_to_idx, idx_to_letter = load_ocr_data()
    print_dataset_stats(words_X, words_y, idx_to_letter)
    
    print("\nSample word:")
    print(f"  Letters: {''.join([idx_to_letter[l] for l in words_y[0]])}")
    print(f"  Shape: {words_X[0].shape}")
    
    print("\nFlattening for standard classification...")
    X_flat, y_flat = get_flat_data(words_X, words_y)
    print(f"  X shape: {X_flat.shape}")
    print(f"  y shape: {y_flat.shape}")
    
    print("\nSplitting into train/test...")
    X_train, y_train, X_test, y_test = train_test_split_by_fold(words_X, words_y)
    print(f"  Train words: {len(X_train)}")
    print(f"  Test words: {len(X_test)}")
