def circular_shareholding(n, edges):
  # Build the graph and the reversed graph
  adj = [[] for _ in range(n)]
  rev_adj = [[] for _ in range(n)]
    
  for u, v in edges:
    adj[u].append(v)
    rev_adj[v].append(u)
        
  # DFS to find last order traversal
  visited = [False] * n
  finished = [False] * n
  order = []
    
  for i in range(n):
    if not visited[i]:
      stack = [i]
      while stack:
        curr = stack[-1]
        if not visited[curr]:
          visited[curr] = True
          # Push unvisited neighbors to stack
          for neighbor in adj[curr]:
            if not visited[neighbor]:
              stack.append(neighbor)
        else:
          curr = stack.pop()
          # Only append to order when finished with all children
          if not finished[curr]:
            finished[curr] = True
            order.append(curr)
                        
  # Find circular groups using the reversed graph
  visited_rev = [False] * n
  circular_groups = []

  # Process in reverse of finishing times
  for i in reversed(order):
    if not visited_rev[i]:
      stack = [i]
      visited_rev[i] = True
      current_scc = []
      
      while stack:
        curr = stack.pop()
        current_scc.append(curr)
        
        for neighbor in rev_adj[curr]:
          if not visited_rev[neighbor]:
            visited_rev[neighbor] = True
            stack.append(neighbor)
        
      # > 1 companies in the SCC
      if len(current_scc) > 1:
        circular_groups.append(current_scc)

  return circular_groups