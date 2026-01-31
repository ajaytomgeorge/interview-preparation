# Topological Sort - Complete Guide

## What is Topological Sort?

**Topological sort** is an ordering of nodes where:
- For every directed edge u → v, **u comes before v** in the ordering
- **Valid only for Directed Acyclic Graphs (DAGs)**
- Based purely on dependencies
- Ignores edge weights completely

---

## Key Characteristics

✅ **Applicable only to:** Directed Acyclic Graph (DAG)  
✅ **An ordering of:** Nodes based on dependencies  
✅ **Property:** For every directed edge u → v, u comes before v  
❌ **Ignores:** Edge weights completely  

---

## Is Topological Sort a Shortest Path Algorithm?

**Short answer:** ❌ No.

Topological sort is NOT a shortest path algorithm.

**But…** ✅ It is used inside a shortest path algorithm (for DAGs).

---

## DAG Shortest Path Algorithm

### Using Topological Sort

The actual DAG shortest path algorithm works in steps:

1. **Topological sort** the DAG
2. Set `dist[source] = 0`, others = `∞`
3. For each node u in topological order:
   - For each edge u → v:
     - `dist[v] = min(dist[v], dist[u] + weight(u, v))`

### Why This Works

In a DAG:
- Once you process a node in topological order, no future node can point back to it
- So its shortest distance is **final**
- This is similar in spirit to Dijkstra — but without heaps

### Advantages

✔️ Works even with **negative weights**  
✔️ Runs in **O(V + E)**  

---

## Comparison Table

| Algorithm | Uses weights | Finds shortest path | Requires DAG |
|-----------|--------------|-------------------|--------------|
| **Topological sort** | ❌ No | ❌ No | ✅ Yes |
| **DAG shortest path** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Dijkstra** | ✅ Yes | ✅ Yes | ❌ No |
| **Bellman–Ford** | ✅ Yes | ✅ Yes | ❌ No |

---

## Python Implementation: Topological Sort

### Using DFS (Kahn's Algorithm alternative)

```python
def topological_sort(graph, n):
    """
    Topological sort using DFS
    graph: adjacency list
    n: number of vertices
    returns: list of vertices in topological order
    """
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    # Visit all vertices
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    # Return reversed stack (topological order)
    return stack[::-1]

# Example
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

result = topological_sort(graph, 4)
print("Topological Order:", result)  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
```

### Using Kahn's Algorithm (BFS-based)

```python
from collections import deque

def topological_sort_kahn(graph, n):
    """
    Topological sort using Kahn's algorithm (BFS)
    graph: adjacency list
    n: number of vertices
    returns: list of vertices in topological order
    """
    # Calculate in-degree for each vertex
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Queue for vertices with in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree for neighbors
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices are included (no cycle)
    if len(result) != n:
        return []  # Cycle detected
    
    return result

# Example
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

result = topological_sort_kahn(graph, 4)
print("Topological Order:", result)  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

## DAG Shortest Path Implementation

```python
def dag_shortest_path(graph, weights, source, n):
    """
    Find shortest path in DAG using topological sort
    graph: adjacency list
    weights: dictionary with edge weights {(u,v): weight}
    source: starting node
    n: number of vertices
    returns: distance array
    """
    # Step 1: Topological sort
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    topo_order = stack[::-1]
    
    # Step 2: Initialize distances
    dist = [float('inf')] * n
    dist[source] = 0
    
    # Step 3: Relax edges in topological order
    for u in topo_order:
        if dist[u] != float('inf'):
            for v in graph.get(u, []):
                weight = weights.get((u, v), 0)
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    return dist

# Example
graph = {
    0: [1, 2],
    1: [3],
    2: [1, 3],
    3: []
}

weights = {
    (0, 1): 2,
    (0, 2): 4,
    (1, 3): 1,
    (2, 1): -5,
    (2, 3): 2
}

dist = dag_shortest_path(graph, weights, 0, 4)
print("Shortest distances from 0:", dist)  # Handles negative weights!
```

---

## Graph Types vs Shortest Path Algorithms

| Graph Type | Directed | Undirected | Cycles | Negative Edges | Negative Cycles | Dijkstra Applicable? | What to Use |
|-----------|----------|-----------|--------|----------------|------------------|----------------------|------------|
| Simple graph | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | Dijkstra |
| Directed graph | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | Dijkstra |
| Directed graph | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | Dijkstra |
| Undirected graph | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | Dijkstra |
| **DAG** | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | DAG shortest path (faster) |
| **DAG** | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | **Topological shortest path** |
| Graph with negative edges | ✅/❌ | ✅/❌ | ❌ | ✅ | ❌ | ❌ | Bellman–Ford |
| Graph with negative cycle | ✅/❌ | ✅/❌ | ✅ | ✅ | ✅ | ❌ | No shortest path exists |

---

## Complexity Analysis

| Algorithm | Time | Space | Requirements |
|-----------|------|-------|--------------|
| **DFS-based Topo Sort** | O(V + E) | O(V) | DAG |
| **Kahn's Algorithm** | O(V + E) | O(V) | DAG |
| **DAG Shortest Path** | O(V + E) | O(V) | DAG, no negative cycles |
| **Dijkstra** | O((V + E) log V) | O(V) | No negative edges |
| **Bellman–Ford** | O(V × E) | O(V) | Any graph, no negative cycles |

---

## Example: Job Scheduling with Dependencies

### Problem

You have tasks with dependencies. Find a valid execution order.

```
Tasks: A, B, C, D
Dependencies:
  A → B (B depends on A)
  A → C
  B → D
  C → D

Find valid execution order
```

### Solution using Topological Sort

```python
def schedule_tasks(tasks, dependencies):
    """
    tasks: list of task names
    dependencies: list of (before, after) tuples
    returns: valid execution order
    """
    graph = {task: [] for task in tasks}
    in_degree = {task: 0 for task in tasks}
    
    for before, after in dependencies:
        graph[before].append(after)
        in_degree[after] += 1
    
    # Kahn's algorithm
    queue = deque([task for task in tasks if in_degree[task] == 0])
    order = []
    
    while queue:
        task = queue.popleft()
        order.append(task)
        
        for dependent in graph[task]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    return order if len(order) == len(tasks) else None  # None if cycle

# Example
tasks = ['A', 'B', 'C', 'D']
dependencies = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]

order = schedule_tasks(tasks, dependencies)
print("Execution order:", order)  # Output: ['A', 'B', 'C', 'D'] or ['A', 'C', 'B', 'D']
```

---

## Key Interview Points

✅ **Topological sort is only for DAGs**  
✅ **Two main approaches:** DFS (recursion stack) and Kahn's (BFS with in-degree)  
✅ **Can be used for DAG shortest path** with negative weights  
✅ **O(V + E) time complexity**  
✅ **Detect cycles:** If not all vertices are in result, cycle exists  
✅ **Multiple valid orderings:** Any valid topological order works  

---

## One-Line Summary

Topological Sort is an algorithm that orders vertices of a DAG such that for every directed edge u → v, u comes before v in the ordering.
