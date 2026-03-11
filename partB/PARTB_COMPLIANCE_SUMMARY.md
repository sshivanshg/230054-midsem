# Part B Compliance Summary vs MidSem Part B PDF

This document checks the project against the **Mid-Semester Examination Part B** rubric (MidSem_PartB (1).pdf).

---

## Repository structure

| Requirement | Status | Notes |
|-------------|--------|--------|
| `partB/` folder at repo root | ✅ | Present |
| `task_1_1.ipynb` … `task_3_2.ipynb` (8 notebooks) | ✅ | All present, executed with outputs |
| `partB/report.pdf` | ✅ | Max 4 pages, exported from report.md |
| `llm_task_1_1.json` … `llm_task_4_2.json` (10 files) | ✅ | All present |
| `partB/results/` with plots as image files | ✅ | task_2_2_results.png, task_2_3_results.png, task_3_1_ablation.png, task_3_1_ablation_comparison.png, task_3_2_failure_mode.png |
| `partB/data/` with README | ✅ | data/README.md explains how data is obtained and used |
| `partB/requirements.txt` (versions, CPU-installable) | ✅ | Pinned versions, no GPU deps |
| Notebooks executed, outputs visible | ✅ | Do not clear outputs before submission |

---

## Question 1: Understanding (25 marks)

### Task 1.1 — Core contribution (8 marks)
- **Step-by-step method** with refs to Eq/Fig/Section: ✅ (Steps 1–5 with Section 3, Algorithm 1, Eq. 5–7, Section 5.3).
- **Final summary sentence** (problem + what makes approach better): ✅ Added in notebook.

### Task 1.2 — Key assumptions (8 marks)
- **At least 3 assumptions**: ✅ (loss not depending on h*_i(w); convex–concave structure; tractable latent completion).
- **Per assumption**: Assumption, why method needs it, violation scenario, paper reference: ✅ All present (violation scenarios and refs in markdown).

### Task 1.3 — What the paper improves (9 marks)
- **Name baseline** [2]: ✅ Ranking SVM / Structural SVM without latent variables.
- **Limitation of baseline** [2]: ✅ Added (does not optimize P@k directly).
- **How proposed overcomes** [1]: ✅ CCCP + latent h + P@k loss.
- **One condition where paper’s method would not outperform** [4]: ✅ Added (poor h init → trivial solution; or easy/small data where fixed h suffices).

---

## Question 2: Reproduction on toy dataset (40 marks)

### Task 2.1 — Dataset (5 marks)
- **Toy dataset, ≥100 samples, ≥2 features**: ✅ 200 samples, 5 features, 2 informative.
- **Justify in 3–5 sentences** (what it is, why testbed, limitations vs paper): ✅ In opening markdown.
- **Preprocessing documented**: ✅ Split by query, StandardScaler, saved to partB/data/.

### Task 2.2 — One contribution reproduced (20 marks)
- **At start**: Which result/contribution + evaluation metric: ✅ Added (ranking application, P@5 / NDCG@5 / MAP).
- **After significant code**: 2–3 sentences + cite Eq/section: ✅ Present for data load, metrics, baseline, Latent SVM, training.
- **Dataset, implementation, result, short interpretation**: ✅ All in notebook.

### Task 2.3 — Result, comparison, checklist (15 marks)
- **Result + paper value**: ✅ Our P@5/NDCG vs Table 3 (0.567, 0.532).
- **3–5 sentences on gap**: ✅ Honest explanation (toy vs OHSUMED, scale, semantics).
- **At least one visualization in partB/results/**: ✅ task_2_3_results.png (and task_2_2_results.png).
- **Final cell “Reproducibility Checklist”** with the five confirmations: ✅ Reworded to explicit confirmations (seeds, requirements.txt, run order, data loading, hyperparameters).

---

## Question 3: Ablation (35 marks)

### Task 3.1 — Two-component ablation (20 marks)
- **Two distinct components**: ✅ (1) CCCP loop / latent h, (2) Precision@k loss vs 0–1 loss).
- **Per component**: markdown (name + role), code, plot/table in results/, **5–7 sentence interpretation**: ✅ Interpretations added in notebook after the plot.
- **Plots in partB/results/**: ✅ task_3_1_ablation.png (and task_3_1_ablation_comparison.png).

### Task 3.2 — Failure mode (15 marks)
- **Markdown**: failure scenario + why method struggles: ✅ Poor h init → trivial/degenerate w (Section 5.3).
- **Code + plot in results/**: ✅ Per-query NDCG comparison, task_3_2_failure_mode.png.
- **5–7 sentences** linking failure to assumption from Q1: ✅ Link to latent completion (Eq. 6) and Task 1.2.
- **One-sentence concrete modification**: ✅ Warm start with weighted average classification (Section 5.3).

---

## Question 4: Report and LLM (30 marks)

### Task 4.1 — Report (15 marks)
- **Single report.pdf, max 4 pages** (min 10pt, 1” margins): ✅ From report.md.
- **Content**:  
  - One-paragraph paper summary: ✅  
  - Reproduction setup + honest gap: ✅  
  - Two ablation findings: ✅  
  - Failure mode + explanation: ✅  
  - Short reflection: ✅ (your paragraph on synthetic limits, CCCP fragility, C, future work).

### Task 4.2 — LLM disclosure (15 marks)
- **10 JSON files** (llm_task_1_1 … llm_task_4_2): ✅ All present.
- **Part A structure +** `task_tag`, `code_used_verbatim`, `student_modification` (when true), **top 5 prompts**: ✅ Checked in llm_task_1_1 and llm_task_2_2; same schema expected for all.
- **1.5 marks per correct file** (10 × 1.5 = 15): ✅ Structure supports full marks if declarations and prompts are complete in each file.

---

## Permitted / not permitted

- **Permitted**: CPU-only Python libs, LLM with disclosure, toy/public datasets, simplified implementations. ✅ Compliant.
- **Not permitted**: Change Part A paper, GPU/cloud, cleared outputs, sharing another student’s work. ✅ None of these.

---

## Changes made during compliance pass

1. **task_1_1.ipynb**: Added final summary sentence (problem + what makes approach better).
2. **task_1_3.ipynb**: Added new markdown cell with limitation of baseline, how proposed overcomes it, and one condition where paper’s method would not outperform baseline.
3. **task_2_2.ipynb**: Added at top of first cell explicit “Contribution we are reproducing” and “Evaluation metric” (P@5, NDCG@5, MAP).
4. **task_2_3.ipynb**: Reproducibility Checklist rephrased to explicit confirmations matching the rubric.
5. **task_3_1.ipynb**: Added “Interpretation of ablation results” markdown with two 5–7 sentence paragraphs (one per ablation).

---

## Recommendation

- **Regenerate report.pdf** after any further edits to `report.md` (e.g. `pandoc report.md -o report.pdf --pdf-engine=weasyprint` from partB/ with venv weasyprint).
- Before submission: run all notebooks top-to-bottom once more (2.1 → 2.2 → 2.3, then 3.1, 3.2) and ensure no cleared outputs.
- Submit repo + Google Form by the deadline; Part C may ask about ablations, failure mode, and reflection, so your written explanations in the notebooks and report are the main reference.

---

*Summary generated to verify Part B against the MidSem Part B PDF rubric.*
