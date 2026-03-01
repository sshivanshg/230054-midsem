# AML Midsem - Research Paper Recommendations

**Requirements Recap:**
- Published 2008-2013 (preferably 2010-2012)
- Top-tier A* conferences: NeurIPS, ICML, AISTATS, KDD
- Classical methods: SVM, GMM, or Time Series
- Must introduce/explain a core method (not just apply existing techniques)
- NO deep learning, surveys, or pure benchmarking papers

---

## TOP RECOMMENDATIONS (Easiest to Reproduce)

### 1. ⭐ Support Vector Machines as Probabilistic Models
**Conference:** ICML 2011  
**Authors:** Alex Smola et al.  
**Topic:** SVM  
**Link:** https://icml.cc/Conferences/2011/papers/386_icmlpaper.pdf

**Why it's good:**
- Shows how SVMs can be viewed as maximum likelihood estimates of probabilistic models
- Theoretical paper with clear mathematical derivations
- Rederives established SVM algorithms from a probabilistic perspective
- Experiments are conceptual and easy to reproduce

**Reproducibility:** ⭐⭐⭐⭐⭐ (mostly theoretical derivations + simple experiments)

---

### 2. ⭐ Convergence of the EM Algorithm for Gaussian Mixtures with Unbalanced Mixing Coefficients
**Conference:** ICML 2012  
**Authors:** Iftekhar Naim, Daniel Gildea  
**Topic:** GMM / EM Algorithm  
**Link:** https://icml.cc/2012/papers/814.pdf

**Why it's good:**
- Studies how mixing coefficients affect EM convergence for GMM
- Proposes a deterministic anti-annealing algorithm
- Clear theoretical contribution with reproducible experiments
- Compares against standard EM, BFGS, Conjugate Gradient

**Reproducibility:** ⭐⭐⭐⭐⭐ (standard GMM + simple modifications)

---

### 3. ⭐ Beating SGD: Learning SVMs in Sublinear Time
**Conference:** NeurIPS 2011  
**Authors:** Elad Hazan, Tomer Koren, Nati Srebro  
**Topic:** SVM Optimization  
**Link:** https://papers.nips.cc/paper/4359-beating-sgd-learning-svms-in-sublinear-time

**Why it's good:**
- Novel stochastic primal-dual optimization for linear SVMs
- First method with runtime sublinear in training set size
- Clear algorithmic contribution
- Straightforward to implement and benchmark

**Reproducibility:** ⭐⭐⭐⭐ (algorithm is well-defined, experiments on standard datasets)

---

### 4. ⭐ Multiple Kernel Learning and the SMO Algorithm
**Conference:** NeurIPS 2010  
**Authors:** Vishwanathan et al.  
**Topic:** SVM / Kernel Methods  
**Link:** https://papers.nips.cc/paper_files/paper/2010/hash/a01a0380ca3c61428c26a231f0e49a09-Abstract.html

**Why it's good:**
- Extends SMO algorithm to p-norm MKL with Bregman divergence
- Clear optimization framework
- Can train on many kernels efficiently
- Well-documented algorithm

**Reproducibility:** ⭐⭐⭐⭐ (extends existing SMO, clear pseudocode)

---

### 5. ⭐ Learning Non-Linear Combinations of Kernels
**Conference:** NeurIPS 2009  
**Authors:** Corinna Cortes, Mehryar Mohri, Afshin Rostamizadeh  
**Topic:** Kernel Methods / SVM  
**Link:** https://papers.nips.cc/paper/3692-learning-non-linear-combinations-of-kernels

**Why it's good:**
- Studies polynomial combinations of base kernels
- Reduces minimax problem to simpler minimization
- Projection-based gradient descent algorithm
- Clear theoretical analysis

**Reproducibility:** ⭐⭐⭐⭐ (well-defined algorithm, UCI datasets)

---

### 6. ⭐ The Kernelized Stochastic Batch Perceptron
**Conference:** ICML 2012  
**Authors:** Andrew Cotter, Shai Shalev-Shwartz, et al.  
**Topic:** Kernel SVM  
**Link:** https://icml.cc/2012/papers/493.pdf

**Why it's good:**
- Novel stochastic gradient method for kernel SVM
- Better runtime guarantees than Pegasos for approximations
- Clear algorithm description
- Comparable to existing methods

**Reproducibility:** ⭐⭐⭐⭐ (builds on well-known methods)

---

### 7. ⭐ Auto-Regressive HMM Inference with Incomplete Data for Short-Horizon Wind Forecasting
**Conference:** NeurIPS 2010  
**Authors:** David Barber, Joseph Bockhorst, Paul Roebber  
**Topic:** Time Series / AR-HMM  
**Link:** https://papers.nips.cc/paper_files/paper/2010/hash/242c100dc94f871b6d7215b868a875f8-Abstract.html

**Why it's good:**
- Introduces auto-regressive HMM for time series
- Handles missing observations
- Clear probabilistic model
- Real-world application (wind forecasting)

**Reproducibility:** ⭐⭐⭐⭐ (model is well-specified, synthetic + real data)

---

### 8. ⭐ Learning Auto-regressive Models from Sequence and Non-sequence Data
**Conference:** NeurIPS 2011  
**Authors:** Tzu-Kuo Huang, Jeff Schneider  
**Topic:** Time Series / VAR Models  
**Link:** https://papers.nips.cc/paper/2011/hash/6c3cf77d52820cd0fe646d38bc2145ca-Abstract.html

**Why it's good:**
- Vector Auto-regressive (VAR) model learning
- Uses discrete-time Lyapunov equation
- Penalized least-square estimation
- Clear mathematical framework

**Reproducibility:** ⭐⭐⭐⭐ (standard optimization, clear equations)

---

### 9. ⭐ Primal-Dual Message-Passing Algorithm for Large Scale Structured Prediction
**Conference:** NeurIPS 2010  
**Authors:** Various  
**Topic:** Structured SVM  
**Link:** https://papers.nips.cc/paper/2010/hash/dc912a253d1e9ba40e2c597ed2376640-Abstract.html

**Why it's good:**
- Relates CRFs and structured SVMs theoretically
- Shows soft-max approximates hinge loss
- Message-passing algorithm
- Graphical models connection

**Reproducibility:** ⭐⭐⭐ (more complex but well-defined)

---

### 10. ⭐ Universal Consistency of Multi-Class Support Vector Classification
**Conference:** NeurIPS 2010  
**Authors:** Ambuj Tewari, Peter Bartlett  
**Topic:** SVM Theory  
**Link:** https://papers.nips.cc/paper/2010/hash/182be0c5cdcd5072bb1864cdee4d3d6e-Abstract.html

**Why it's good:**
- Proves universal consistency of multi-class SVM
- Extends Steinwart's work on binary SVM
- Theoretical paper with clear proofs
- Can reproduce theoretical analysis + simple validation

**Reproducibility:** ⭐⭐⭐⭐ (mostly theoretical, simple experiments)

---

### 11. ⭐ Fast Large-scale Mixture Modeling with Component-specific Data Partitions
**Conference:** NeurIPS 2010  
**Authors:** Bo Thiesson, Chong Wang  
**Topic:** GMM / Variational EM  
**Link:** https://papers.nips.cc/paper/2010/hash/6cdd60ea0045eb7a6ec44c54d29ed402-Abstract.html

**Why it's good:**
- Variational EM framework for large-scale GMM
- Sub-linear E-step complexity
- Provable convergence
- Scalable mixture modeling

**Reproducibility:** ⭐⭐⭐⭐ (extends standard EM with partitioning)

---

### 12. ⭐ Nonparametric Variational Inference (Mixture of Gaussians Variational Family)
**Conference:** ICML 2012  
**Authors:** Samuel Gershman, Matthew Hoffman, David Blei  
**Topic:** GMM / Variational Inference  
**Link:** https://icml.cc/2012/papers/360.pdf

**Why it's good:**
- Uses GMM as variational family
- Captures multimodal posteriors
- Clear variational framework
- Extends beyond mean-field

**Reproducibility:** ⭐⭐⭐ (more advanced but well-documented)

---

### 13. ⭐ ℓp-Norm Multiple Kernel Learning
**Conference:** JMLR 2011 (presented at ICML 2010)  
**Authors:** Marius Kloft et al.  
**Topic:** SVM / Multiple Kernel Learning  
**Link:** https://jmlr.csail.mit.edu/papers/volume12/kloft11a/kloft11a.pdf

**Why it's good:**
- Extends MKL to arbitrary ℓp-norms
- Efficient interleaved optimization
- Code and data available!
- Non-sparse outperforms sparse

**Reproducibility:** ⭐⭐⭐⭐⭐ (code provided at http://doc.ml.tu-berlin.de/nonsparse_mkl/)

---

## BACKUP OPTIONS

### 14. SimpleMKL
**Conference:** JMLR 2008  
**Topic:** SVM / Multiple Kernel Learning  
**Link:** https://www.jmlr.org/papers/v9/rakotomamonjy08a.html

Foundational MKL paper. Easy to implement and reproduce.

---

### 15. Factorized Asymptotic Bayesian Inference for Mixture Modeling
**Conference:** AISTATS 2012  
**Authors:** Ryohei Fujimaki, Satoshi Morinaga  
**Topic:** GMM / Bayesian Inference

Addresses model selection for mixture models.

---

## SELECTION STRATEGY

**For maximum ease of reproduction, I recommend these TOP 5:**

1. **Convergence of EM for GMM** (ICML 2012) - Simple GMM experiments
2. **SVM as Probabilistic Models** (ICML 2011) - Theoretical + simple validation
3. **ℓp-Norm MKL** (JMLR 2011) - Has code provided!
4. **Beating SGD for SVM** (NeurIPS 2011) - Clear algorithm
5. **Auto-Regressive HMM** (NeurIPS 2010) - Time series, well-defined model

**For GMM focus:** Options 2, 11, 12, 15
**For SVM focus:** Options 1, 3, 4, 5, 6, 10, 13, 14
**For Time Series focus:** Options 7, 8

---

## IMPORTANT NOTES

1. **Verify conference tier**: All listed are from A* venues (NeurIPS, ICML, AISTATS, KDD, JMLR)
2. **Verify year**: All are within 2008-2013, most in 2010-2012
3. **No deep learning**: All are classical ML methods
4. **Core contribution**: All introduce new methods/theory (not just applications)
5. **Download PDFs early**: Verify you can access the full paper
6. **Check for code**: Some papers have official implementations available

Good luck! 🎯
