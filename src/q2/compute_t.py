import numpy as np

def compute_t(m):
  I = np.linalg.matrix_power(m, 0)
  M_inv = np.linalg.inv(I - m)
  T = M_inv - I
  return T

ownership_matrix = np.array([[0, 0.6, 0, 0.1],
                            [0, 0, 0.5, 0],
                            [0.2, 0, 0, 0.4],
                            [0, 0, 0, 0]])
T = compute_t(ownership_matrix)
print("A ownership D: ", T[0, 3])
print("In percentage: ", T[0, 3] * 100, "%")