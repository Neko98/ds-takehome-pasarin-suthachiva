import numpy as np

def compute_t(m, holder, company):
  T = 0
  for i in range(m.shape[1]):
    if i == company:
      T += m[holder, i]
    else:
      M = m[holder, i]
      for j in range(m.shape[1]):
        if j == company:
          T += M * m[i, j]
        else:
          T += m[holder, i]
  return T

ownership = np.array([[0, 0.6, 0, 0.1], 
                      [0, 0, 0.5, 0], 
                      [0.2, 0, 0, 0.4], 
                      [0, 0, 0, 0]])
T = compute_t(ownership, holder=0, company=3)
T_percentage = T * 100
print(f"A's total percentage ownership of D: {T_percentage}%")