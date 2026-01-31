📘 Problem Statement: Path With Constraints (Graph Backtracking)

You are given an undirected graph represented as an adjacency list.

Each node represents a city, and edges represent roads.

You are also given:

A start node S

An end node T

An integer K

Task

Determine whether there exists a simple path from S to T such that:

The path uses exactly K edges

No node is visited more than once

You must return True if such a path exists, otherwise False

Example
Input
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

S = 0
T = 3
K = 2

Output
True

Explanation

Valid path:

0 → 1 → 3


Uses exactly 2 edges.

❓ Why Backtracking Is Required

You must try all possible paths

Once you go down a path:

Mark node as visited

Explore deeper

Unmark (backtrack) when returning

Greedy or BFS alone cannot handle the exact K constraint

🧠 Key Interview Signals

Interviewers expect:

DFS

Visited set

Backtracking (undo visited)

Pruning when path length exceeds K

✍️ Python Solution (Backtracking DFS)
def has_path_with_k_edges(graph, start, end, k):
    visited = set()

    def dfs(node, edges_used):
        # Base case: reached end with exact K edges
        if node == end and edges_used == k:
            return True

        # Too many edges used
        if edges_used > k:
            return False

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, edges_used + 1):
                    return True

        # Backtrack
        visited.remove(node)
        return False

    return dfs(start, 0)

🧪 More Test Cases
❌ No valid path
has_path_with_k_edges(graph, 0, 3, 3)  # False

✅ Start equals end
has_path_with_k_edges(graph, 0, 0, 0)  # True
