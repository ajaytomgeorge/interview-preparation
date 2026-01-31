# Graph Problems

---

## Graph Representations in Memory — Exam Notes

Before diving into algorithms, understand how graphs live in memory. The representation you choose affects performance dramatically.

### 1. Objects & Pointers (Node-Based)

#### Structure
Each node is an object with pointers/references to neighbor nodes.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # List of Node references

# Example
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')

nodeA.neighbors = [nodeB, nodeC]
nodeB.neighbors = [nodeA, nodeC]
nodeC.neighbors = [nodeA, nodeB]
```

#### Memory Model
```
Memory Layout:
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Node A     │  ┌─→ │  Node B     │  ┌─→ │  Node C     │
├─────────────┤  │   ├─────────────┤  │   ├─────────────┤
│ value: 'A'  │  │   │ value: 'B'  │  │   │ value: 'C'  │
│ neighbors ──┼──┘   │ neighbors ──┼──┘   │ neighbors ──┼──┐
└─────────────┘      └─────────────┘      └─────────────┘  │
    ^                                           ^           │
    │                                           │           │
    └───────────────────────────────────────────┴───────────┘

Object overhead: Each node needs:
  - Memory for value
  - Memory for neighbors list
  - Pointer(s) to other nodes
  - Potential object metadata (12-40 bytes per object)
```

#### Characteristics
| Property | Value |
|----------|-------|
| **Memory** | Medium to High |
| **Edge Lookup** | O(degree) - must traverse neighbors list |
| **Neighbor Access** | O(1) per neighbor |
| **Dynamic Modifications** | Easy (add/remove nodes) |
| **Cache Locality** | Poor |

#### Pros ✅
- Intuitive and natural to implement
- Easy to add/remove nodes and edges dynamically
- Perfect for recursive DFS/BFS
- Works well with object-oriented design

#### Cons ❌
- Poor cache locality (objects scattered in memory)
- Extra object overhead (metadata, pointers)
- Harder to parallelize
- Memory fragmentation

#### Best For
- In-memory algorithms
- Dynamic graphs (frequent add/remove)
- Small to medium graphs
- Interview implementations

---

### 2. Adjacency Matrix

#### Structure
An N × N matrix where `matrix[i][j] = 1` if edge exists, `0` otherwise.

```python
# Adjacency Matrix for graph with 4 nodes
import numpy as np

# Nodes: 0, 1, 2, 3
adjacency_matrix = [
    [0, 1, 1, 0],  # Node 0: connects to 1, 2
    [1, 0, 1, 1],  # Node 1: connects to 0, 2, 3
    [1, 1, 0, 1],  # Node 2: connects to 0, 1, 3
    [0, 1, 1, 0],  # Node 3: connects to 1, 2
]

# Weighted version
weighted_matrix = [
    [0, 5, 3, 0],
    [5, 0, 2, 7],
    [3, 2, 0, 1],
    [0, 7, 1, 0],
]

# Check if edge exists: O(1)
if adjacency_matrix[0][1] == 1:
    print("Edge 0→1 exists")
```

#### Memory Model
```
Visual Representation:
    0   1   2   3
  ┌───┬───┬───┬───┐
0 │ 0 │ 1 │ 1 │ 0 │  Node 0
  ├───┼───┼───┼───┤
1 │ 1 │ 0 │ 1 │ 1 │  Node 1
  ├───┼───┼───┼───┤
2 │ 1 │ 1 │ 0 │ 1 │  Node 2
  ├───┼───┼───┼───┤
3 │ 0 │ 1 │ 1 │ 0 │  Node 3
  └───┴───┴───┴───┘

Memory Layout: Contiguous array
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 1 │ 0 │ 1 │ 0 │ 1 │ 1 │ 1 │ 1 │ 0 │ 1 │ 0 │ 1 │ 1 │ 0 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
 Row 0           Row 1           Row 2           Row 3

Total memory: N² integers
```

#### Characteristics
| Property | Value |
|----------|-------|
| **Memory** | O(N²) - always, regardless of edge count |
| **Edge Lookup** | O(1) - direct array access |
| **Neighbor Access** | O(N) - must scan entire row |
| **Dynamic Modifications** | Hard (must resize matrix) |
| **Cache Locality** | Excellent (contiguous memory) |

#### Pros ✅
- **Ultra-fast edge queries**: O(1) lookup
- Excellent cache locality (contiguous memory)
- Simple implementation
- Good for dense graphs
- Great for algorithms needing frequent edge checks
- Supports weighted edges easily

#### Cons ❌
- **Wastes space**: O(N²) memory even for sparse graphs
- **Slow neighbor traversal**: O(N) to find all neighbors
- Hard to resize (must allocate new matrix)
- Space explosion for large sparse graphs
- Poor for graphs with millions of nodes

#### Best For
- Dense graphs (many edges)
- Small fixed-size graphs
- Algorithms needing fast edge lookups (Floyd-Warshall, etc.)
- Complete or near-complete graphs
- Interview problems with small N

#### When to Use / When NOT to Use
```
USE Adjacency Matrix when:
  ✓ N ≤ 1000 (and N² is acceptable)
  ✓ Graph is dense (edges ≈ N²/2)
  ✓ You need fast edge lookups
  ✓ Graph size is fixed
  ✗ Don't use if N > 10,000 (memory explosion)
  ✗ Don't use for sparse graphs
  ✗ Don't use if frequent add/remove needed
```

---

### 3. Adjacency List

#### Structure
An array/dictionary where each node stores a list of its neighbors.

```python
# Most common representation
adjacency_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Alternative: array of lists
adjacency_list_array = [
    [1, 2],      # Node 0
    [0, 2, 3],   # Node 1
    [0, 1, 3],   # Node 2
    [1, 2]       # Node 3
]

# Weighted version
weighted_adjacency_list = {
    0: [(1, 5), (2, 3)],
    1: [(0, 5), (2, 2), (3, 7)],
    2: [(0, 3), (1, 2), (3, 1)],
    3: [(1, 7), (2, 1)]
}

# Find all neighbors: O(degree)
neighbors_of_0 = adjacency_list[0]  # [1, 2]
```

#### Memory Model
```
Memory Layout:
┌─────────────────────────────────────────────┐
│ Node 0 → [1, 2]                             │
├─────────────────────────────────────────────┤
│ Node 1 → [0, 2, 3]                          │
├─────────────────────────────────────────────┤
│ Node 2 → [0, 1, 3]                          │
├─────────────────────────────────────────────┤
│ Node 3 → [1, 2]                             │
└─────────────────────────────────────────────┘

Total memory: O(V + E)
  V = number of nodes (for the array)
  E = number of edges (total entries across all lists)

Example: 4 nodes, 5 edges
  Memory = 4 + 5 = 9 entries (vs 16 for matrix)
```

#### Characteristics
| Property | Value |
|----------|-------|
| **Memory** | O(V + E) - only for actual edges |
| **Edge Lookup** | O(degree) - must scan neighbor list |
| **Neighbor Access** | O(degree) - direct list access |
| **Dynamic Modifications** | Easy (add/remove from list) |
| **Cache Locality** | Good (sequential list traversal) |

#### Pros ✅
- **Memory efficient**: O(V + E) vs O(V²)
- Fast neighbor traversal (direct access)
- Scales well for large sparse graphs
- Easy to add/remove edges
- Standard for real-world applications
- Works with both weighted and unweighted graphs

#### Cons ❌
- Slower edge lookup than matrix O(degree)
- Requires more pointers/references
- Slightly more complex implementation
- Cache miss potential (lists can be scattered)

#### Best For
- Sparse graphs (few edges)
- Large graphs (millions of nodes)
- Real-world networks (social, transportation, etc.)
- Dynamic graphs (frequent updates)
- BFS/DFS traversal
- **Most practical use cases**

---

### Quick Comparison Table

| Aspect | Objects & Pointers | Adjacency Matrix | Adjacency List |
|--------|-------------------|------------------|----------------|
| **Memory** | O(V + E) + overhead | O(V²) | O(V + E) |
| **Edge Lookup** | O(degree) | **O(1)** | O(degree) |
| **All Neighbors** | O(degree) | O(V) | **O(degree)** |
| **Add Edge** | O(1) | O(1) | **O(1)** |
| **Add Node** | **O(1)** | O(V²) | **O(1)** |
| **Remove Edge** | O(degree) | O(1) | O(degree) |
| **Remove Node** | O(degree) | O(V²) | O(degree) |
| **Space (sparse graph)** | O(V + E) | **Wasteful** | **Best** |
| **Space (dense graph)** | O(V + E) ≈ O(V²) | **Compact** | ≈ Same |
| **Cache Locality** | Poor | **Excellent** | Good |
| **Implementation** | Medium | Simple | **Most used** |
| **Dynamic Updates** | **Easy** | Hard | **Easy** |
| **Sparse or Dense?** | Either | Dense | **Sparse** |

---

### Decision Tree: Which Representation to Use?

```
START: Choosing graph representation
    │
    ├─ Is N small (≤ 1000)?
    │   ├─ Yes AND need fast edge lookup?
    │   │   └─→ Use ADJACENCY MATRIX ✓
    │   │       (Dense graphs, small fixed size)
    │   │
    │   └─ Yes but traversal-heavy?
    │       └─→ Use ADJACENCY LIST ✓
    │           (Most flexible choice)
    │
    ├─ Is N very large (> 10,000)?
    │   └─→ Use ADJACENCY LIST ✓✓
    │       (Only viable option for memory)
    │
    ├─ Do you add/remove nodes frequently?
    │   └─→ Use OBJECTS & POINTERS or ADJACENCY LIST ✓
    │       (Avoid matrix - hard to resize)
    │
    └─ Is graph sparse (E << V²)?
        └─→ Use ADJACENCY LIST ✓✓ 
            (Most efficient)
        
    Is graph dense (E ≈ V²)?
        └─→ Use ADJACENCY MATRIX ✓
            (Compact representation)

BOTTOM LINE:
  🎯 Default choice: ADJACENCY LIST
  🎯 Interview: Start with adjacency list, mention others
  🎯 If explicitly dense + small: Matrix
```

---

### Memory Examples

#### Example: Social Network with 1 Million Users, 5 Edges Average

```
Objects & Pointers:
  ≈ 1M nodes × 100 bytes + 5M edge pointers
  ≈ 100MB + 40MB = ~140MB ✓

Adjacency Matrix:
  1M × 1M × 1 byte = 1 TB 🤯
  (Not even an option!)

Adjacency List:
  1M entries + 5M entries = ~6M entries
  ≈ 24-50MB ✓✓ (Best choice)
```

#### Example: 100-node Complete Graph (All 5,050 Edges)

```
Objects & Pointers:
  100 nodes × 100 bytes + 5,050 pointers
  ≈ 10KB + 40KB = ~50KB

Adjacency Matrix:
  100 × 100 × 1 byte = 10KB ✓ (Compact!)

Adjacency List:
  100 + 5,050 = ~5,150 entries
  ≈ 20-40KB
```

---

## 1. Breadth-First Search (BFS)

### Problem Statement

Traverse a graph level-by-level using a queue data structure. BFS is used to explore neighbors at the current depth before moving to nodes at the next depth.

### Algorithm

1. Start from a source node
2. Add it to a queue
3. While queue is not empty:
   - Dequeue a node
   - Explore all unvisited neighbors
   - Mark them as visited
   - Enqueue them
4. Continue until queue is empty

### Python Solution

```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                print("found")
                return
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs('A', 'F')  # Output: found
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) where V = vertices, E = edges |
| **Space** | O(V) for queue and visited set |

### Use Cases

- Shortest path in unweighted graphs
- Level-order traversal
- Connected components
- Bipartite graph checking
- Social network traversal

### Example Graph Visualization

```
    A
   / \
  B   C
 / \   \
D   E   F
 \ /
  (connected)

BFS from A: A → B, C → D, E, F → (all visited)
```

---

## 2. Depth-First Search (DFS)

### Problem Statement

Traverse a graph by going as deep as possible before backtracking. Uses a stack (or recursion) to explore nodes.

### Algorithm (Iterative with Stack)

1. Start from source node
2. Push it to a stack
3. While stack is not empty:
   - Pop a node
   - Explore all unvisited neighbors
   - Mark them as visited
   - Push them to stack
4. Continue until stack is empty

### Python Solution (Iterative)

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(start, end):
    stack = [start]
    visited = {start}
    
    while stack:
        node = stack.pop()
        
        for neighbor in graph[node]:
            if neighbor == end:
                print("found")
            
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs('A', 'F')  # Output: found
```

### Python Solution (Recursive)

```python
def dfs_recursive(node, end, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor == end:
            print("found")
            return
        
        if neighbor not in visited:
            dfs_recursive(neighbor, end, visited)
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(V + E) |
| **Space** | O(V) for recursion stack or explicit stack |

### Use Cases

- Topological sorting
- Cycle detection
- Strongly connected components
- Backtracking problems
- Path finding
- Maze solving

### DFS vs BFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue | Stack |
| **Shortest Path** | ✓ Yes (unweighted) | ✗ No |
| **Memory** | More for wide graphs | More for deep graphs |
| **Order** | Level-by-level | Deep-first |
| **Use Case** | Shortest path, levels | Topological sort, cycles |

---

## 3. Graph Representation

### Adjacency List (Used in Examples)

```python
graph = {
    'A': ['B', 'C'],     # A connects to B, C
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

**Advantages:**
- Space efficient for sparse graphs
- Easy to iterate over neighbors
- Simple to implement

### Adjacency Matrix

```python
# 0 = no edge, 1 = edge
graph = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0],  # F
]
```

**Advantages:**
- O(1) edge lookup
- Suitable for dense graphs
- Good for dynamic graphs

---

## Key Concepts

### Visited Set
Prevents revisiting nodes and infinite loops in cyclic graphs.

### Neighbors/Adjacent Nodes
All nodes directly connected to current node.

### Path Finding
BFS finds shortest path in unweighted graphs; DFS finds any path.

### Connected Components
Groups of nodes where any node can reach another.

---

## Problems in This Folder

### Core Algorithm Files

1. **bfs.py** - Standard BFS implementation for graph traversal
2. **dfs.py** - Iterative DFS using stack-based approach
3. **dfs_recurssive.py** - Recursive DFS implementation
4. **backtreacking_explore_multiple_paths.py** - Backtracking to explore all possible paths in a graph

### Application Problems

1. **build_package_graphs.py** - Build dependency graphs and handle package ordering (topological sorting)
2. **currency_conversion.py** - Graph-based currency conversion using one traversal method
3. **currency_conversiondfsvsbfs.py** - Currency conversion comparing DFS vs BFS approaches

### Specialized Problem Categories

1. **Largest component in a graph/**
   - **Number of Islands** - Count disconnected regions using graph traversal
   - **Smallest Island** - Find smallest connected component

2. **Shortest path -simple bfs/** - BFS-based shortest path algorithms in unweighted graphs

---

---

## Problem Solutions

### 1. Number of Islands

#### Problem Statement
Given a 2D grid containing '1' (land) and '0' (water), count the number of distinct islands. An island is formed by connecting adjacent lands horizontally or vertically.

#### Example
```
Input:
1 1 0 0 0
1 0 0 1 0
0 0 1 0 1
1 0 0 1 1

Output: 5 islands
```

#### Solution Explanation
Use DFS or BFS to explore each unvisited land cell. When you find a '1', start a traversal and mark all connected '1's as visited. Each time you start a new traversal, increment island count.

#### Implementation
```python
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        # Base case: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Mark as visited
        grid[r][c] = '0'
        
        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left
    
    # Traverse entire grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)
    
    return islands

# Example
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '0', '0', '1', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '0', '1', '1']
]
print(numIslands(grid))  # Output: 5
```

#### Complexity Analysis
- **Time:** O(rows × cols) - visit each cell once
- **Space:** O(rows × cols) - recursion depth in worst case

---

### 2. Smallest Island

#### Problem Statement
Find the size (number of cells) of the smallest island in a grid of land and water.

#### Example
```
Input:
1 1 0 0 1
1 0 0 1 1
0 0 1 0 1

Output: 1 (smallest island has 1 cell)
```

#### Solution Explanation
Similar to Number of Islands, but instead of just counting islands, track the size of each island during DFS/BFS. Return the minimum size found.

#### Implementation
```python
def smallestIsland(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    min_size = float('inf')
    
    def dfs(r, c):
        # Out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return 0
        
        # Mark as visited
        grid[r][c] = '0'
        
        # Count this cell + all connected cells
        size = 1
        size += dfs(r + 1, c)  # down
        size += dfs(r - 1, c)  # up
        size += dfs(r, c + 1)  # right
        size += dfs(r, c - 1)  # left
        
        return size
    
    # Traverse entire grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                island_size = dfs(i, j)
                min_size = min(min_size, island_size)
    
    return min_size if min_size != float('inf') else 0

# Example
grid = [
    ['1', '1', '0', '0', '1'],
    ['1', '0', '0', '1', '1'],
    ['0', '0', '1', '0', '1']
]
print(smallestIsland(grid))  # Output: 1
```

#### Complexity Analysis
- **Time:** O(rows × cols)
- **Space:** O(rows × cols)

---

### 3. Shortest Path (BFS)

#### Problem Statement
Find the shortest path between two nodes in an unweighted graph.

#### Example
```
Graph: A-B-D
       |   |
       C-E-F

Shortest path from A to F: A → B → D → F or A → B → E → F (length: 3)
```

#### Solution Explanation
Use BFS starting from source node. BFS explores level-by-level, guaranteeing shortest path in unweighted graphs. Track parent pointers to reconstruct the path.

#### Implementation
```python
from collections import deque

def shortestPath(graph, start, end):
    """
    graph: adjacency list representation
    start: starting node
    end: target node
    returns: shortest path as list of nodes
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            # Reconstruct path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    
    return []  # No path found

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['C', 'D', 'E']
}

print(shortestPath(graph, 'A', 'F'))  # Output: ['A', 'C', 'F'] or ['A', 'B', 'D', 'F']
```

#### Complexity Analysis
- **Time:** O(V + E)
- **Space:** O(V)

---

### 4. Currency Conversion

#### Problem Statement
Given exchange rates between currencies, find if you can convert from one currency to another and calculate the exchange rate.

#### Example
```
Rates: USD→EUR: 0.92, EUR→GBP: 0.87, GBP→JPY: 150

Convert USD to JPY: 1 USD = 0.92 EUR = 0.80 GBP = 120 JPY
```

#### Solution Explanation
Model currencies as nodes and rates as edges. Use DFS or BFS to find path from source to target currency, multiplying rates along the way.

#### Implementation (DFS)
```python
def currencyConversion(rates, source, target):
    """
    rates: list of [from, to, rate]
    returns: exchange rate or -1 if conversion not possible
    """
    # Build graph
    graph = {}
    for src, dst, rate in rates:
        if src not in graph:
            graph[src] = []
        if dst not in graph:
            graph[dst] = []
        graph[src].append((dst, rate))
        graph[dst].append((src, 1 / rate))
    
    visited = set()
    
    def dfs(curr, target, rate):
        if curr == target:
            return rate
        
        visited.add(curr)
        
        for neighbor, exchange_rate in graph.get(curr, []):
            if neighbor not in visited:
                result = dfs(neighbor, target, rate * exchange_rate)
                if result != -1:
                    return result
        
        return -1
    
    return dfs(source, target, 1.0)

# Example
rates = [["USD", "EUR", 0.92], ["EUR", "GBP", 0.87], ["GBP", "JPY", 150]]
print(currencyConversion(rates, "USD", "JPY"))  # Output: 120.18
```

#### Complexity Analysis
- **Time:** O(V + E) for DFS
- **Space:** O(V)

---

### 5. Backtracking - Explore Multiple Paths

#### Problem Statement
Find all possible paths from source to target in a graph, or explore all solutions to a problem.

#### Example
```
Graph: 1→2→4
       ↓ ↓ ↓
       3→5

All paths from 1 to 5:
1→2→4→5
1→2→5
1→3→5
```

#### Solution Explanation
Use DFS with backtracking. Explore each neighbor recursively, and backtrack (remove from path) before exploring other neighbors.

#### Implementation
```python
def allPathsSourceToTarget(graph, source, target, path=[]):
    """
    graph: adjacency list
    source: starting node
    target: ending node
    returns: list of all paths from source to target
    """
    path = path + [source]
    
    if source == target:
        return [path]
    
    paths = []
    for neighbor in graph.get(source, []):
        newpaths = allPathsSourceToTarget(graph, neighbor, target, path)
        paths.extend(newpaths)
    
    return paths

# Example
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5],
    4: [5],
    5: []
}

print(allPathsSourceToTarget(graph, 1, 5))
# Output: [[1, 2, 4, 5], [1, 2, 5], [1, 3, 5]]
```

#### Complexity Analysis
- **Time:** O(2^V) - exponential in worst case (all possible paths)
- **Space:** O(V) - recursion depth

---

### 6. Topological Sort (Package Dependencies)

#### Problem Statement
Given dependencies between packages, find a valid order to install them where each package's dependencies are installed first.

#### Example
```
Dependencies: B depends on A, D depends on B and C

Valid order: A → C → B → D
```

#### Solution Explanation
Use DFS with a visited set and finishing stack. When all neighbors of a node are visited, add it to stack. The reverse of finish order is topological order.

#### Implementation
```python
def topologicalSort(graph):
    """
    graph: adjacency list of dependencies
    returns: list in topological order
    """
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)
    
    # Visit all nodes
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]  # Reverse to get topological order

# Example: B depends on A, D depends on B and C
graph = {
    'A': [],
    'B': ['A'],
    'C': [],
    'D': ['B', 'C']
}

print(topologicalSort(graph))  # Output: ['A', 'C', 'B', 'D']
```

#### Complexity Analysis
- **Time:** O(V + E)
- **Space:** O(V)

---

### 7. Cycle Detection

#### Problem Statement
Determine if a graph contains a cycle.

#### Example
```
Graph: 1→2→3
       ↓   ↑
       4←──┘

Contains cycle: 2→3→4→2
```

#### Solution Explanation
Use DFS with three states: unvisited, visiting, visited. If we encounter a node in "visiting" state, we found a cycle.

#### Implementation
```python
def hasCycle(graph):
    """
    Returns True if graph has cycle, False otherwise
    """
    # States: 0=unvisited, 1=visiting, 2=visited
    state = {node: 0 for node in graph}
    
    def dfs(node):
        if state[node] == 1:  # Currently visiting - found cycle
            return True
        if state[node] == 2:  # Already visited
            return False
        
        state[node] = 1  # Mark as visiting
        
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        
        state[node] = 2  # Mark as visited
        return False
    
    # Check each node
    for node in graph:
        if state[node] == 0:
            if dfs(node):
                return True
    
    return False

# Example
graph = {
    1: [2],
    2: [3, 4],
    3: [4],
    4: [2]
}

print(hasCycle(graph))  # Output: True
```

#### Complexity Analysis
- **Time:** O(V + E)
- **Space:** O(V)
