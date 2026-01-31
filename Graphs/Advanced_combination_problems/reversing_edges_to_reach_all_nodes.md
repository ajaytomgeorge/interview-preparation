# Minimum Edge Reversals So Every Node Is Reachable

**Difficulty:** Hard  
**Companies:** Microsoft

## Problem Statement

There is a simple directed graph with `n` nodes labeled from `0` to `n - 1`. The graph would form a tree if its edges were bi-directional.

You are given an integer `n` and a 2D integer array `edges`, where `edges[i] = [ui, vi]` represents a directed edge going from node `ui` to node `vi`.

An **edge reversal** changes the direction of an edge, i.e., a directed edge going from node `ui` to node `vi` becomes a directed edge going from node `vi` to node `ui`.

For every node `i` in the range `[0, n - 1]`, your task is to independently calculate the minimum number of edge reversals required so it is possible to reach any other node starting from node `i` through a sequence of directed edges.

**Return** an integer array `answer`, where `answer[i]` is the minimum number of edge reversals required so it is possible to reach any other node starting from node `i` through a sequence of directed edges.

### Clarifying Questions

When you get asked this question in a real-life environment, it will often be ambiguous. Make sure to ask these questions:

- What is the range of values for the node IDs, and how many nodes can there be at most?
- Are the edge lists guaranteed to be valid, meaning will there be edges pointing to non-existent nodes or self-loops?
- If it is impossible to make all nodes reachable from node 0, what should the function return? (e.g., -1, null, throw an exception)
- Can there be multiple edges between the same two nodes, and if so, how should they be handled?
- Is the graph guaranteed to be connected, or could there be disconnected components that are impossible to reach regardless of edge reversals?

### Examples

#### Example 1

**Input:**
```
n = 4
edges = [[2,0],[2,1],[1,3]]
```

**Output:**
```
[1,1,0,2]
```

**Explanation:**

For node 0: after reversing the edge `[2,0]`, it is possible to reach any other node starting from node 0. So `answer[0] = 1`.

For node 1: after reversing the edge `[2,1]`, it is possible to reach any other node starting from node 1. So `answer[1] = 1`.

For node 2: it is already possible to reach any other node starting from node 2. So `answer[2] = 0`.

For node 3: after reversing the edges `[1,3]` and `[2,1]`, it is possible to reach any other node starting from node 3. So `answer[3] = 2`.

#### Example 2

**Input:**
```
n = 3
edges = [[1,2],[2,0]]
```

**Output:**
```
[2,0,1]
```

**Explanation:**

For node 0: after reversing the edges `[2,0]` and `[1,2]`, it is possible to reach any other node starting from node 0. So `answer[0] = 2`.

For node 1: it is already possible to reach any other node starting from node 1. So `answer[1] = 0`.

For node 2: after reversing the edge `[1,2]`, it is possible to reach any other node starting from node 2. So `answer[2] = 1`.

### Constraints

- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ui == edges[i][0] < n`
- `0 <= vi == edges[i][1] < n`
- `ui != vi`
- The input is generated such that if the edges were bi-directional, the graph would be a tree.

---

## Solution Approaches

### Approach 1: Brute Force

#### Intuition

The core idea is to try every possible combination of reversing edges in the graph. For each combination, we check if starting from a specific node, we can reach all other nodes. We choose the combination that requires the fewest edge reversals to achieve this reachability.

#### Algorithm

1. Consider every possible set of edges that we could reverse.
2. For each of these sets of reversed edges, create a modified version of the graph where those edges are actually reversed.
3. Choose a starting node in the modified graph.
4. Explore the modified graph to see if it is possible to reach every other node from the chosen starting node, following the direction of the edges.
5. If every node is reachable from the starting node, count how many edges were reversed to create this version of the graph.
6. Repeat steps 2-5 for all possible sets of reversed edges, keeping track of the minimum number of reversals needed to make all nodes reachable from the start node.
7. The smallest number of reversals among all the possibilities represents the solution.

#### Code Implementation

```python
def min_edge_reversals_brute_force(num_nodes, edges):
    min_reversals = float('inf')

    # Iterate through all possible combinations of edge reversals.
    for i in range(2**len(edges)):
        reversed_edges_indices = []
        for j in range(len(edges)):
            if (i >> j) & 1:
                reversed_edges_indices.append(j)

        # Create a modified graph with the reversed edges.
        modified_edges = []
        for index, (source_node, dest_node) in enumerate(edges):
            if index in reversed_edges_indices:
                modified_edges.append((dest_node, source_node))
            else:
                modified_edges.append((source_node, dest_node))

        # Check reachability from each node.
        for start_node in range(num_nodes):
            # Check if all nodes are reachable from the start node.
            reachable_nodes = set()
            queue = [start_node]
            reachable_nodes.add(start_node)

            while queue:
                current_node = queue.pop(0)
                for source_node, dest_node in modified_edges:
                    if source_node == current_node and dest_node not in reachable_nodes:
                        reachable_nodes.add(dest_node)
                        queue.append(dest_node)

            # If all nodes are reachable, update the minimum reversals.
            if len(reachable_nodes) == num_nodes:
                # Calculate the number of reversals for this combination.
                num_reversals = len(reversed_edges_indices)
                min_reversals = min(min_reversals, num_reversals)

    if min_reversals == float('inf'):
        return -1  # Indicate no solution if no configuration makes all nodes reachable.
    return min_reversals
```

#### Complexity Analysis

**Time Complexity:** `O(2^E * (V + E))`

The algorithm considers all possible combinations of reversing edges. With E edges, there are 2^E possible subsets. For each combination, we perform a reachability check using BFS/DFS which takes O(V + E) time.

**Space Complexity:** `O(2^E + V + E)`

The algorithm explores every possible combination of reversed edges, resulting in 2^E possible graph configurations. For each combination, space is required to store the modified graph representation and the visited set during traversal.

---

### Approach 2: Optimal Solution with BFS from Every Node

#### Intuition

This approach leverages the structure of trees to efficiently compute edge reversals. Instead of trying all combinations, we use a bidirectional graph where:
- Forward edges have a cost of 0 (already pointing in the right direction)
- Backward edges have a cost of 1 (need to be reversed)

We then perform BFS from each node and count the reversals needed.

#### Algorithm

1. Build a bidirectional graph where each edge `(u, v)` creates:
   - Forward connection `(u → v)` with cost 0
   - Backward connection `(v → u)` with cost 1
2. For each potential starting node:
   - Perform BFS traversal
   - Accumulate the costs of edges followed in the backward direction
   - Track visited nodes to avoid revisiting
3. Return the minimum total reversals across all starting nodes.

#### Code Implementation

```python
def min_edge_reversals(number_of_nodes, edges):
    graph = [[] for _ in range(number_of_nodes)]
    for start_node, end_node in edges:
        graph[start_node].append((end_node, 0))
        graph[end_node].append((start_node, 1))

    minimum_reversals = float('inf')

    for start_node in range(number_of_nodes):
        reversals_needed = 0
        visited = [False] * number_of_nodes
        queue = [(start_node, 0)]
        visited[start_node] = True

        # Traverse the graph from the current start node.
        while queue:
            current_node, current_reversals = queue.pop(0)
            reversals_needed += current_reversals

            for neighbor, edge_direction in graph[current_node]:
                if not visited[neighbor]:
                    # Add neighbors to queue; mark visited.
                    visited[neighbor] = True
                    queue.append((neighbor, edge_direction))

        # We take the minimum reversals across all nodes
        minimum_reversals = min(minimum_reversals, reversals_needed)

    return minimum_reversals
```

#### Complexity Analysis

**Time Complexity:** `O(N^2)`

For each of the N nodes, we perform a BFS that visits all N nodes and processes all N-1 edges.

**Space Complexity:** `O(N)`

Space for the graph representation and visited array.

---

### Approach 3: Optimal Solution with Re-rooting (Most Efficient)

#### Intuition

This is the most elegant and efficient solution. The key insight is that we don't need to perform BFS from every node independently. Instead:

1. Compute the answer for one arbitrary root node using DFS
2. Use a **re-rooting technique** to compute answers for all other nodes by updating the cost based on the edge direction

The re-rooting technique works because in a tree, moving the root to an adjacent node only affects the edge connecting them.

#### Algorithm

1. Build a bidirectional graph with costs (0 for forward, 1 for backward)
2. Pick an arbitrary node as the initial root (typically node 0 or the first node in edges)
3. **First DFS:** Count how many edges need to be reversed when rooted at the initial node
4. **Second DFS:** For each other node, compute its cost by updating based on the parent-child relationship:
   - If the edge from parent to child is forward (cost 0): `cost[child] = cost[parent] + 1`
   - If the edge from parent to child is backward (cost 1): `cost[child] = cost[parent] - 1`
5. Return the result array with minimum reversals for each node.

#### Code Implementation

```python
from collections import defaultdict

def min_edge_reversals(n, edges):
    graph = defaultdict(list)

    # Build graph with direction cost
    for u, v in edges:
        graph[u].append((v, 0))  # correct direction
        graph[v].append((u, 1))  # reversed direction

    visited = set()
    cost = {}

    # First DFS: count reversals when root is at edges[0][0]
    def dfs_count(u):
        visited.add(u)
        total = 0

        for v, w in graph[u]:
            if v not in visited:
                total += w
                total += dfs_count(v)

        return total

    root = edges[0][0]  # take first node as initial root
    cost[root] = dfs_count(root)

    # Second DFS: re-root dynamically
    def dfs_reroot(u):
        for v, w in graph[u]:
            if v not in cost:
                if w == 0:
                    # Forward edge: we need one MORE reversal to reach from v
                    cost[v] = cost[u] + 1
                else:
                    # Backward edge: we need one FEWER reversal to reach from v
                    cost[v] = cost[u] - 1
                dfs_reroot(v)

    dfs_reroot(root)

    return cost

# Return as array in correct order
def min_edge_reversals_array(n, edges):
    cost_dict = min_edge_reversals(n, edges)
    return [cost_dict[i] for i in range(n)]
```

#### Example Walkthrough

**Given:**
```
n = 8
edges = [(1, 2), (2, 3), (2, 4), (3, 5), (4, 6), (6, 8)]
```

**Step 1: Build Graph**

Each directed edge `u → v` creates:
- `(u, v, cost=0)` – following the arrow
- `(v, u, cost=1)` – going backward

**Step 2: First DFS (root = 1)**

From node 1, all edges point outward, so we count 0 reversals:
- `cost[1] = 0`

**Step 3: Second DFS (Re-rooting)**

Starting from node 1, we propagate costs:
- `1 → 2`: forward edge (cost 0) → `cost[2] = 0 + 1 = 1`
- `2 → 3`: forward edge (cost 0) → `cost[3] = 1 + 1 = 2`
- `2 → 4`: forward edge (cost 0) → `cost[4] = 1 + 1 = 2`
- `3 → 5`: forward edge (cost 0) → `cost[5] = 2 + 1 = 3`
- `4 → 6`: forward edge (cost 0) → `cost[6] = 2 + 1 = 3`
- `6 → 8`: forward edge (cost 0) → `cost[8] = 3 + 1 = 4`

**Result:**
```
{1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 8: 4}
```

**Interpretation:**
- From node 1: 0 reversals needed
- From node 2: 1 reversal needed (need to reverse edge 1 → 2)
- From node 3: 2 reversals needed
- And so on...

#### Why This Works

**Tree Property:** Since the graph is a tree, there's exactly one path between any two nodes. Re-rooting changes only one edge at a time, and all other edges keep their orientation meaning.

**Efficiency:** We compute once and reuse everywhere. Instead of O(N²) BFS calls, we only need two DFS passes.

#### Complexity Analysis

**Time Complexity:** `O(N)`

Two DFS traversals, each visiting all N nodes and N-1 edges.

**Space Complexity:** `O(N)`

Space for the graph representation and cost dictionary.

#### Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(2^E * (V+E)) | O(2^E + V) | Exponential, impractical for large inputs |
| BFS Every Node | O(N²) | O(N) | Practical, straightforward |
| Re-rooting | O(N) | O(N) | Optimal, elegant, uses tree structure |

---

## Key Takeaways

1. **Recognize Tree Structure:** This problem's efficiency depends on recognizing the graph is a tree, enabling the re-rooting technique.

2. **Cost Encoding:** Encoding edge direction as a cost (0 for forward, 1 for backward) simplifies tracking reversals.

3. **Re-rooting is Powerful:** Many tree problems can be solved efficiently using re-rooting when you need to compute something for every node as the root.

4. **Compute Once, Reuse Everywhere:** Instead of redundant calculations, propagate information intelligently through the tree structure.

---

## Related Problems

- [Minimum Fuel Cost to Report to the Capital](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)
- [Count the Number of Good Nodes](https://leetcode.com/problems/count-the-number-of-good-nodes/)
- [Tree Diameter](https://en.wikipedia.org/wiki/Tree_diameter)
