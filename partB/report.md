# Part B Report: Learning Structural SVMs with Latent Variables (Yu & Joachims, 2009)

**Maximum 4 pages.** Export this file to `partB/report.pdf` for submission.

---

## 1. Paper Summary

Yu and Joachims (2009) extend Structural SVMs to settings where the correct structured output depends on an unobserved **latent variable** *h*. Standard Structural SVMs assume the output and any structure in the joint feature map are fully observed; in many tasks (e.g. motif position, coreference links, or the ranking of documents within a query) the latent structure is not annotated. The authors formulate an objective that includes a latent variable *h* per example and show it can be written as a **difference of two convex functions** in the weight vector **w**. They solve it with the **Concave-Convex Procedure (CCCP)**: alternately (1) **latent variable completion** — for each training example, set *h* to the value that maximizes **w·Φ(x, y, h)** given the current **w** (corresponding to Equation 6 in the paper) — and (2) **weight update** — solve a convex Structural SVM subproblem in **w** with the completed *h* fixed (Equation 7). This process is repeated until convergence. The method is demonstrated on three applications: discriminative motif finding, noun phrase coreference, and **Precision@k optimization** for learning to rank, which we reproduce on a synthetic ranking task.

---

## 2. Reproduction Setup & Gap

The reproduction was carried out entirely on a **synthetic toy dataset** for a learning-to-rank (Precision@k) task. The data was generated in `partB/task_2_1.ipynb` using `sklearn.datasets.make_classification`, then grouped by synthetic query IDs so that each “query” has a set of document feature vectors and binary relevance labels. Train and test splits were made by query (e.g. 80% / 20% of queries) to avoid leakage. Features were normalized with a `StandardScaler` fitted on the training set only. The same pipeline (baseline linear ranker and Latent Structural SVM with CCCP) was run on this toy data, and evaluation metrics (NDCG@5, P@5, MAP) were computed per query and averaged.

The **gap** between our toy results and the paper’s reported results is expected and is discussed honestly here. The paper reports **P@5 = 0.567** for the Latent Structural SVM on the OHSUMED benchmark (Table 3, 5-fold cross-validation), with Ranking SVM at P@5 = 0.532. Our toy dataset is much smaller (e.g. ~20 queries, ~200 samples), uses random features and binary relevance only, and has no real retrieval semantics. On such data, the problem can be easier (or the heuristic used for the latent *h* may already align well with the latent structure), so we may see different — sometimes higher — P@5 values than the baseline, or similar performance. The numerical values are therefore **not directly comparable** to Table 3. The reproduction’s goal was to validate the **pipeline** (data → baseline and Latent SVM → metrics) and the **relative role** of the CCCP loop and the Precision@k loss, not to match the paper’s absolute numbers. A faithful reproduction on the original benchmark would require using the same dataset and protocol as the paper; Part B guidelines forbade using the paper’s exact dataset, hence the use of the synthetic toy dataset only.

---

## 3. Ablation Findings

In `task_3_1.ipynb` we performed a **two-component ablation** on the synthetic ranking task.

**Ablation 1 — Removing the CCCP loop (fixed heuristic for *h*):** We fixed the latent variable *h* (e.g. using a simple heuristic like *h* = 1 for all documents or *h* = *y*) and did not update it during training. This removes the latent variable completion step (Equation 6) and the alternating CCCP procedure. The model effectively becomes a standard linear ranker trained with the same loss surrogate. **What this reveals:** When we do not infer *h* from the data, we lose the benefit of the paper’s formulation. On the toy data, performance may be similar if the fixed heuristic is already a good proxy for the latent structure; on more complex data, we would expect the full CCCP procedure to do better because it adapts *h* to the current **w**.

**Ablation 2 — Replacing the custom Precision@k loss with a standard 0-1 loss:** We trained a model (e.g. Ridge regression) that minimizes a standard loss (e.g. mean squared error or 0-1 classification loss on relevance labels) instead of the paper’s Precision@k-based loss (cap − P@k). **What this reveals:** The task-specific loss is important for optimizing the right metric. A model trained only to predict relevance labels may not rank the top-k documents as well for P@k as a model that directly targets the ranking metric via the latent *h* and the P@k loss.

Together, the ablations show that both the **CCCP loop (latent completion)** and the **custom Precision@k loss** are central to the method; removing either simplifies the model and can change or weaken performance relative to the full Latent Structural SVM.

---

## 4. Failure Mode

In `task_3_2.ipynb` we summarized a central **failure mode** described in the paper (Section 5.3). The authors state that a **poor initialization of the latent variable *h*** — for example, **randomly picking k relevant documents** as the initial “top-k” — often leads to the **“trivial zero vector as solution”** for **w**. In other words, CCCP can converge to a degenerate or uninformative weight vector when the initial *h* is chosen arbitrarily. This connects directly to the assumption that latent completion (Equation 6) should provide a meaningful signal: if *h* is random or uninformative, the H-step does not guide the W-step usefully, and the algorithm can get stuck. The paper therefore recommends a **better initialization**: train a **weighted average classification** model on the training (and optionally validation) set to obtain an initial **w**, then run CCCP with this **w** as a warm start instead of initializing **w** to zero or *h* at random. **One-sentence fix:** Use a weighted average classification warm start for **w** as in Section 5.3 of the paper, then run CCCP with this initial **w** so that the first latent completion step produces a sensible *h* and avoids the trivial zero solution.

---

## 5. Reflection

