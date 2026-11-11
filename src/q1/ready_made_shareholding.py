import networkx as nx

def networkx_circular_groups(n, edges):

  G = nx.DiGraph()
  G.add_nodes_from(range(n))
  G.add_edges_from(edges)
  
  sccs = nx.strongly_connected_components(G)
  
  circular_groups = []
  for scc in sccs:
    if len(scc) > 1:
      circular_groups.append(list(scc))

  return circular_groups