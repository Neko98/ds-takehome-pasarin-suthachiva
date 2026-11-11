import random
from circular_shareholding_algorithm import circular_shareholding
from ready_made_shareholding import networkx_circular_groups

V = 100000
E = 250000

print("Generating graph")
edges = [(random.randint(0, V - 1), random.randint(0, V - 1)) for _ in range(E)]

new_algorithm = circular_shareholding(V, edges)
print(f"New algorithm")
print(f"Found {len(new_algorithm)} distinct circular shareholding groups.")

baseline_algorithm = networkx_circular_groups(V, edges)
print(f"Baseline algorithm")
print(f"Found {len(baseline_algorithm)} distinct circular shareholding groups.")

