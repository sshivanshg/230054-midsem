# Part B Rubric Checklist (mapped to your notebooks)

Use this to verify each rubric item before submission.

---

## Question 1: Paper Understanding (No Code)

| Item | Where | Status |
|------|--------|--------|
| **Task 1.1** Step-by-step pipeline; cite **Algorithm 1**, **Eq. 6** (latent variable completion), **Eq. 7** (Structural SVM) | `task_1_1.ipynb` — pipeline with explicit refs to Algorithm 1, Eq. (6), Eq. (7) | ✓ |
| **Task 1.2** At least 3 assumptions; include **Δ must not depend on h*_i(w)**; **Violation scenario** + **Paper reference** for each | `task_1_2.ipynb` — three assumptions with violation scenario and paper ref each | ✓ |
| **Task 1.3** Explicitly name baseline (**Ranking SVM** or standard Structural SVM without latent variables) | `task_1_3.ipynb` — names Ranking SVM and standard Structural SVM without h | ✓ |

---

## Question 2: Toy Dataset & Reproduction

| Item | Where | Status |
|------|--------|--------|
| **Task 2.1** Markdown: why synthetic dataset is reasonable testbed for L2R / Precision@k in **3–5 sentences** | `task_2_1.ipynb` — “Why it is a reasonable testbed” + “Limitations” | ✓ |
| **Task 2.2** After **every major code block**: 2–3 sentence markdown + **cite paper** (e.g. Eq. 6, Eq. 7) | `task_2_2.ipynb` — markdown after data load, metrics, baseline, Latent SVM class, train/eval; Eq. 6 & 7 cited | ✓ |
| **Task 2.3** Compare toy metric (e.g. P@5) to **paper Table 3** (e.g. 0.567 Latent Structural SVM) | `task_2_3.ipynb` — “Comparison to paper (Table 3)” section | ✓ |
| **Task 2.3** Explain gap in **3–5 sentences** | Same section in `task_2_3.ipynb` | ✓ |
| **Task 2.3** **Last cell** = Markdown titled exactly **“Reproducibility Checklist”** (seeds, dependencies, execution) | `task_2_3.ipynb` — final cell “## Reproducibility Checklist” | ✓ |
| **Task 2.3** All plots saved to **partB/results/** | Checklist bullet + code uses `Path('results')` from partB/ | ✓ |

---

## Question 3: Ablations & Failure Modes

| Item | Where | Status |
|------|--------|--------|
| **Task 3.1** **Two distinct** ablations: (1) skip CCCP / fixed h, (2) **0-1 loss** instead of P@k loss; plots in **partB/results/** | `task_3_1.ipynb` — Ablation 1: fixed h; Ablation 2: 0-1 loss (Ridge); plot saved to results/ | ✓ |
| **Task 3.2** Demonstrate **failure** (e.g. poor init → trivial zero); **explain** linking to assumption; **1-sentence fix** | `task_3_2.ipynb` — intro cites paper; final markdown: failure explanation, link to assumption, one-sentence fix (warm start) | ✓ |

---

## Question 4: Reports & Logistics

| Item | Where | Status |
|------|--------|--------|
| **report.pdf** — 1 doc, max 4 pages; summary, reproduction gap, ablations, failure mode, reflection | `partB/report.pdf` — you provide | [ ] |
| **10 JSONs** — fields **task_tag**, **code_used_verbatim**, **student_modification**; **Top 5 prompts** task-specific | `llm_task_1_1.json` … `llm_task_4_2.json` — fill prompts and declaration | [ ] |
| **data/README** — how toy dataset was **generated** | `partB/data/README.md` — “How the dataset was obtained” | ✓ |
| **All 8 notebooks** fully executed, **outputs/plots visible** (cleared outputs = 20-mark penalty) | Run all cells; do not clear outputs before submit | [ ] |

---

*After edits, re-run notebooks 2.1 → 2.2 → 2.3 → 3.1 → 3.2 so outputs and plots are up to date.*
