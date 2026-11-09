import math

def combination(n, r):

  total_combinations = math.comb(n, r)
  
  return total_combinations

company = 2000000
pair = 2
k = 1000
a_comb = combination(company, pair)
print(f"3a number of comparisons: {a_comb:,}")

blocks = math.ceil(company / k)
b_comb = combination(blocks, pair)
print(f"3a number of comparisons in a group: {b_comb:,}")
print(f"3a total comparisons on block of {blocks:,} : {(b_comb * k):,}")