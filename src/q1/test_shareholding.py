import numpy as np
from circular_shareholding_algorithm import circular_shareholding
from ready_made_shareholding import networkx_circular_groups

V = 100000
E = 250000

np.random.seed(1)
print("Generating graph")
edges = [(np.random.randint(0, V - 1), np.random.randint(0, V - 1)) for _ in range(E)]

new_algorithm = circular_shareholding(V, edges)
print(f"New algorithm")
print(f"Found {len(new_algorithm)} distinct circular shareholding groups.")

baseline_algorithm = networkx_circular_groups(V, edges)
print(f"Baseline algorithm")
print(f"Found {len(baseline_algorithm)} distinct circular shareholding groups.")

check = frozenset(frozenset(s) for s in new_algorithm) == frozenset(frozenset(s) for s in baseline_algorithm)
print(f"Is answer same? {check} ")
