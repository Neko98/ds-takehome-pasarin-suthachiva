import math

def combination(n, r):

  total_combinations = math.comb(n, r)
  
  return total_combinations

company = 2000000
pair = 2
k = 1000
a_comb = combination(company, pair)
print(f"1_3a number of comparisons: {a_comb:,}")

blocks = math.ceil(company / k)
b_comb = combination(blocks, pair)
print(f"1_3b number of comparisons in a group: {b_comb:,}")
print(f"1_3b total comparisons on block of {blocks:,} : {(b_comb * k):,}")

equal_blocks = 1000000
nonequal_blocks_1 = 1100000
nonequal_blocks_2 = 900000
c_equal_comb = combination(equal_blocks, pair) * 2
c_nonequal_comb = combination(nonequal_blocks_1, pair) + combination(nonequal_blocks_2, pair)
print(f"1_3c number of comparisons in a 2 equal group: {c_equal_comb:,}")
print(f"1_3c number of comparisons in a 2 nonequal group: {c_nonequal_comb:,}")