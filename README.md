# ds-takehome-pasarin-suthachiva

## Selected Problems
- **Compulsory:**
  - **Problem 1** - Discrete Mathematics: Shareholding Networks
  - **Problem 2** - Linear Algebra: Indirect Ownership and PCA
- **Elective Chosen:**
  - **Problem 3** - Probability & Statistics: Data-driven Decisions

## Repository Structure
```text
ds-takehome-pasarin-suthachiva/
├── README.md                              # Elective chosen, setup, reproduction steps, and summary of results
├── requirements.txt                       # Pinned Python package versions
├── AI_USAGE.md                            # Disclosure of AI tool usage and verification
├── report/
│   └── answer.ipynb                       # Full written answers, derivations, code, and outputs
└── src/
    ├── q1/
    │   ├── circular_shareholding_algorithm.py  # Kosaraju SCC implementation (no graph libraries)
    │   ├── ready_made_shareholding.py          # NetworkX SCC baseline for verification
    │   ├── test_shareholding.py                # 100,000-node random graph test & comparison
    │   └── combination.py                      # Entity resolution comparison counts
    ├── q2/
    │   └── compute_t.py                        # Total ownership matrix T = (I - M)^(-1) - I
    └── q3/
        ├── p_value.py                          # Two-proportion pooled z-test helper
        ├── hypothesis.py                       # A/B test z-score and p-value
        ├── find_sample.py                      # Per-group sample size calculation (80% power)
        └── aa_testing.py                       # 1,000-run daily-peeking A/A test simulation
```

## Setup
Tested with **Python 3.11.7**.
pip install -r requirements.txt

## How to Reproduce

### Run the Notebook Report
Open and execute all cells in `report/answer.ipynb`:
```bash
jupyter notebook report/answer.ipynb
```

### Run Standalone Source Scripts
From the repository root:

**Problem 1 — Shareholding Networks & Entity Resolution**
```bash
python src/q1/test_shareholding.py
python src/q1/combination.py
```

**Problem 2 — Indirect Ownership**
```bash
python src/q2/compute_t.py
```

**Problem 3 — A/B Testing & Sequential Peeking Simulation**
```bash
python src/q3/hypothesis.py
python src/q3/find_sample.py
python src/q3/aa_testing.py
```

> **Reproducibility note:** `src/q1/test_shareholding.py` and `src/q3/aa_testing.py` sets `np.random.seed(1)`.

## Summary of Results

| Problem | Part | Key Result |
| :--- | :--- | :--- |
| **Problem 1** | 1.1–1.2 Circular Shareholding | Equivalent to directed cycles; detected via Kosaraju's SCC algorithm in $O(\|V\|+\|E\|)$ time and verified against `networkx` on a 100,000-node, 250,000-edge random graph. |
| **Problem 1** | 1.3 Entity Resolution ($n=2,000,000$) | All-pairs: `1,999,999,000,000` comparisons. With $k=1,000$ equal blocks: `1,999,000,000` comparisons (optimal by convexity of $f(x)=\binom{x}{2}$). |
| **Problem 2** | Part A Indirect Ownership | Total ownership matrix computed via $T=(I-M)^{-1}-I$; A's total ownership of D is `0.2340` (`23.40%`), and diagonal entries $T_{AA}=T_{BB}=T_{CC}\approx 6.38\%$ reflect circular self-ownership. |
| **Problem 2** | Part B PCA & SVD | Maximum-variance direction is the top eigenvector of the covariance matrix; PCA via SVD ($X=U\Sigma V^T$) avoids squaring the condition number of $X^T X$. |
| **Problem 3** | Part A Fraud Detection | Positive predictive value $P(\text{Fraud}\mid\text{Alert}) \approx 32.42\%$; 1,000,000 monthly transactions produce `29,300` alerts (`9,500` TP + `19,800` FP), exceeding the `10,000`/month review capacity. |
| **Problem 3** | Part B A/B Testing | Two-proportion test gives $z = 1.4789$, $p = 0.1392$ (not significant at $\alpha=0.05$; 95% CI $[-0.20\%, +1.40\%]$). Required sample size for 80% power is `17,940` per group. Daily peeking over 7 days (1,000 A/A runs, seed=1) inflates false-positive rate to `18.3%`. |
| **Problem 3** | Part C Simpson's Paradox | Demonstrated reversal between subgroup and aggregated rates and criteria for choosing between stratified vs. aggregated views. |
