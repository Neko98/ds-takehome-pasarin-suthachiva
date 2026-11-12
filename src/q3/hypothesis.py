from p_value import calculate_p_value

# Control
n1, x1 = 5000, 0.04
# Treatment
n2, x2 = 5000, 0.046

z_score, p_value = calculate_p_value(n1, x1, n2, x2)

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")
