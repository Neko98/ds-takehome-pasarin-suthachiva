import numpy as np
from p_value import calculate_p_value

simulations = 1000
days = 7
users = 5000
users_per_day = users // days
x = 0.04
alpha = 0.05
false_positives = 0

np.random.seed(1)

for _ in range(simulations):

  control_users = np.random.binomial(1, x, users)
  treatment_users = np.random.binomial(1, x, users)

  for day in range(1, days + 1):
    sum_user = day * users_per_day

    x1 = control_users[:sum_user].sum()
    x2 = treatment_users[:sum_user].sum()

    n1, x1 = sum_user, x1/sum_user
    n2, x2 = sum_user, x2/sum_user
    z_score, p_value = calculate_p_value(n1, x1, n2, x2)
          
    if p_value < alpha:
        false_positives += 1
        break

actual_fpr = (false_positives / simulations) * 100
print(f"False Positive Rate: {actual_fpr:.1f}%")
