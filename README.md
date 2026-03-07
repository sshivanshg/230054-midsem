# Latent Structural SVM Reproduction

**Course**: Advanced Machine Learning  
**Paper**: "Learning Structural SVMs with Latent Variables" (ICML 2009)  
**Authors**: Chun-Nam Yu, Thorsten Joachims (Cornell University)

## Paper Summary

This paper extends Structural SVMs to handle latent variables using the Concave-Convex Procedure (CCCP). The method is demonstrated on three applications:

1. **Discriminative Motif Finding** - Finding DNA binding site motifs in yeast sequences
2. **Noun Phrase Coreference Resolution** - Clustering coreferent noun phrases in documents  
3. **Precision@k Optimization** - Learning to rank for information retrieval

## Project Structure

```
amlmidsem/
├── README.md
├── llm_usage_partA.json          # LLM usage documentation
├── MidSem_PartA.pdf              # Assignment specification
│
├── code/
│   ├── latentssvm_v0.12/         # Latent Structural SVM API (C)
│   ├── latentmotif_v0.12/        # Motif finding application (C)
│   └── latentnpcoref_v0.12/      # Coreference resolution (C)
│
├── data/
│   ├── letter.data               # Stanford OCR dataset (sequence labeling)
│   ├── load_ocr_data.py          # OCR data loader
│   ├── letor/                    # LETOR benchmark (ranking)
│   │   ├── OHSUMED/              # OHSUMED medical retrieval dataset
│   │   └── TREC/                 # TREC web datasets
│   ├── motif/                    # Yeast motif finding data (to be generated)
│   └── coreference/              # MUC6 coreference data (requires license)
│
└── venv/                         # Python virtual environment
```

## Datasets

### Part B (mandatory): Synthetic toy dataset only

Part B uses **only** the **synthetic toy dataset** generated in `partB/task_2_1.ipynb` (saved under `partB/data/`). Do not use the paper’s original dataset (e.g. LETOR OHSUMED) for any Part B training or evaluation. See `partB/data/README.md` for how the toy data is obtained and used.

### 2. Stanford OCR Dataset (Alternative for Structured Prediction)

- **Source**: Stanford AI Lab
- **Task**: Sequence labeling (handwritten letter recognition)
- **Location**: `data/letter.data`
- **Format**: Tab-separated (id, letter, next_id, word_id, position, 128 pixel features)
- **Size**: 52,152 letters, 6,877 words

### 3. Yeast Motif Dataset (Paper's motif finding data)

- **Original Source**: Tom Finley & Uri Keich (Cornell/UNSW)
- **Task**: Finding DNA binding site motifs in yeast ARS sequences
- **Note**: Original data from paper authors; synthetic data can be generated

### 4. MUC6 Coreference Dataset

- **Source**: Linguistic Data Consortium (LDC)
- **Task**: Noun phrase coreference resolution
- **Note**: Requires LDC license (not freely downloadable)

## Setup Instructions

### 1. Python Environment

```bash
cd /Users/shivanshgupta/amlmidsem
source venv/bin/activate

# Already installed packages:
# numpy, scipy, scikit-learn, matplotlib, cvxopt, pandas, jupyter
```

### 2. Compile C Code (optional - for original implementation)

```bash
cd code/latentmotif_v0.12
make

cd ../latentnpcoref_v0.12
make
```

## Completing the Project (Data, Training, Run)

**No additional data download is required** for Part B. For other experiments the repository may contain other datasets (e.g. Stanford OCR, Motif); **Part B does not use them**.

### Part B (Mid-Sem submission: toy dataset only)

Part B **must not** use the paper’s original dataset (e.g. LETOR OHSUMED). All work lives in **partB/** and uses only the **synthetic toy dataset** generated there.

1. **Generate toy data** (from repo root):  
   `jupyter nbconvert --to notebook --execute --inplace partB/task_2_1.ipynb`  
   or run the data-generation cells in `partB/task_2_1.ipynb`. This creates `partB/data/train_data.npy`, `partB/data/test_data.npy`, and `partB/data/scaler.npy`.
2. **Run Part B notebooks in order**: Execute `partB/task_1_1.ipynb` through `partB/task_3_2.ipynb` (all 8 task notebooks). Run `task_2_1.ipynb` first so data exists; then `task_2_2.ipynb`, `task_2_3.ipynb`, `task_3_1.ipynb`, `task_3_2.ipynb`. All use only `partB/data/` and write figures to `partB/results/`.
3. See **partB/README.md** for the full Part B checklist (8 notebooks, 10 LLM JSONs, report.pdf, requirements.txt, data/, results/).

## Reproduction Plan

### Part B (mandatory): Toy dataset only
- **Do not** use the paper’s original dataset (e.g. LETOR OHSUMED) for Part B.
- Generate synthetic data in `partB/task_2_1.ipynb` and use it in tasks 2.2, 2.3, 3.1, 3.2.
- Implement Latent Structural SVM for ranking and evaluate NDCG@5, P@5, MAP on the toy split.

### Option B: Sequence Labeling on OCR
- Use Stanford OCR dataset (fully available)
- Implement structured prediction with latent variables
- Compare to standard CRF/Structural SVM

### Option C: Motif Finding
- Generate synthetic motif data or use public yeast genomic data
- Implement discriminative motif finding
- Compare to GIMSAN (Gibbs sampler baseline)

## References

1. Yu, C.-N. & Joachims, T. (2009). Learning Structural SVMs with Latent Variables. ICML.
   - Paper PDF: https://www.cs.cornell.edu/people/tj/publications/yu_joachims_09a.pdf
   - Official Code: https://www.cs.cornell.edu/~cnyu/latentssvm/

2. LETOR Dataset: Qin, T. et al. (2010). LETOR: A Benchmark Collection for Research on Learning to Rank.
   - Download: https://www.microsoft.com/en-us/research/project/letor-learning-rank-information-retrieval/

3. Stanford OCR Dataset: Taskar, B. et al. (2004). Max-Margin Markov Networks.
   - Download: https://ai.stanford.edu/~btaskar/ocr/

---

## Part B submission (mandatory)

After pushing your code to GitHub, you **must** submit your repository URL via the official Part B Google Form:  
**https://forms.gle/yxfmRprmHDeAzx1C7**

**Deadline: 12 March 2026, 8:00 A.M.**  
Any commits made after this timestamp may not be considered and can lead to cancellation of Part B evaluation. Clean up the README, verify `partB/` contents (see `partB/PARTB_CHECKLIST.md`), then submit the form.
