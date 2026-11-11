import numpy as np
from scipy.stats import norm

alpha = 0.05
power = 0.8
p_1 = 0.04
p_2 = 0.046

z_alpha = norm.ppf(1 - alpha/2)
z_beta = norm.ppf(power)

n = ((z_alpha + z_beta)**2 * (p_1 * (1 - p_1) + p_2 * (1 - p_2))) / ((p_2 - p_1)**2)

print(f"sample size: {n:.0f}")
