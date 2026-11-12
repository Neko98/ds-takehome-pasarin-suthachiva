# AI Usage Disclosure

In accordance with the assessment rules, below is a disclosure of the AI tools used, the parts they assisted with, and how all outputs were verified.

## 1. AI Tools Used
- **Gemini, GitHub Copilot, ChatGPT**: Used during initial problem study, formatting, and coding autocomplete.
- **Antigravity (AI coding assistant)**: Used for reviewing completed answers, checking code and numerical calculations, and drafting `README.md`, `requirements.txt`, and `AI_USAGE.md`.

## 2. Which Parts AI Was Used For
- **Formatting & Problem Setup**: Converting the assessment questions into Markdown cells inside `report/answer.ipynb`.
- **Concept Study & Guidance**: Explaining unfamiliar mathematical concepts and guiding how to structure the approach to questions, concepts were then summarized in my own words and studied further independently.
- **Coding Assistance**: Inline code autocomplete while implementing scripts in `src/q1/`, `src/q2/`, and `src/q3/`.
- **Final Review & Documentation**: Checking mathematical consistency, code correctness, and repository documentation (`README.md`, `requirements.txt`, `AI_USAGE.md`).

## 3. How Outputs Were Verified
- **Problem 1 (Algorithms & Combinatorics)**:
  - Verified the custom Kosaraju SCC implementation (`src/q1/circular_shareholding_algorithm.py`) against `networkx.strongly_connected_components` (`src/q1/ready_made_shareholding.py`) on a 100,000-node random graph (`src/q1/test_shareholding.py`).
  - Checked entity-resolution comparison counts using `math.comb` (`src/q1/combination.py`).
- **Problem 2 (Linear Algebra)**:
  - Verified the total ownership matrix calculation $T = (I - M)^{-1} - I$ using NumPy (`src/q2/compute_t.py`) and cross-checked against manual closed-form derivation.
- **Problem 3 (Probability & Statistics)**:
  - Verified Bayes' theorem calculations, hypothesis test z-score/p-value (`src/q3/hypothesis.py`), and sample-size formula (`src/q3/find_sample.py`) using `scipy.stats.norm` and `numpy`.
  - Verified false-positive rate inflation from sequential peeking via a seeded 1,000-run Monte Carlo A/A simulation (`src/q3/aa_testing.py`, `np.random.seed(1)`).
- **Environment & Reproducibility**:
  - Verified pinned library versions in `requirements.txt` against the local Python 3.11.7 environment and executed all scripts in `src/` to confirm outputs.
