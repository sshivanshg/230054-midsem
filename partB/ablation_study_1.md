
# Ablation Study 1: Remove Latent Inference (H-step)

## Technical Change
**Full CCCP Algorithm**:
  1. Repeat for each CCCP iteration:
     - H-step: h_i* = argmax_h w^T Ψ(x_i, y_i, h)  [INFER latent structure]
     - W-step: w = argmin_w loss(w, h*)            [OPTIMIZE weights given h]

**Ablated Version (This Study)**:
  1. SKIP H-step entirely
  2. Fix h = y (use observed labels, no latent inference)
  3. Single W-step: w = argmin_w loss(w, y)

Result: Reverts to standard Structured SVM (Section 2, no latent modeling).

## Why This Matters
The paper's **main innovation** is the CCCP procedure that alternates H-step and W-step.
Removing H-step isolates the contribution of latent variable discovery.

- H-step allows model to discover hidden structure h from features and observed y
- W-step uses discovered h to train better ranking weights w
- Together (CCCP): joint learning of w and inference of h
- Separated (this ablation): just train w on y, ignore potential h

## Expected Results
Performance drop indicates CCCP's H-step (latent inference) was helping.
Comparable performance indicates toy dataset lacks latent structure, or 5 CCCP iterations insufficient.

## Assumptions Being Tested
This ablation directly tests **Assumption 2** from Task 1.2:
  "Loss function decomposes over latent values, supporting CCCP decomposition."

If Assumption 2 holds and real latent structure exists, removing H-step should hurt.
If not, performance stays flat.
