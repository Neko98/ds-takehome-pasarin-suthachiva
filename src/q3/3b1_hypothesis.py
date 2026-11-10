import numpy as np
from scipy.stats import norm

# Control
n1, x1 = 5000, 0.04
# Treatment
n2, x2 = 5000, 0.046

p_pool = (n1 * x1 + n2 * x2) / (n1 + n2)

se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

z_score = (x2 - x1) / se

p_value = 2 * (1 - norm.cdf(abs(z_score)))

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")
