import numpy as np
from scipy.stats import norm

def calculate_p_value(n1, x1, n2, x2):

  if n1 <= 0 or n2 <= 0:
    print("No users")
    return None, None
  
  p_pool = (n1 * x1 + n2 * x2) / (n1 + n2)

  se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

  z_score = (x2 - x1) / se

  p_value = 2 * (1 - norm.cdf(abs(z_score)))
    
  return z_score, p_value