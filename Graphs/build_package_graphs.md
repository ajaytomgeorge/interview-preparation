# Package Build Dependencies

## Case 1: Solution - Simple DFS with State

### Problem Statement (Python)

You are given a dictionary representing package dependencies.

- Each key is a package name
- Each value is a list of packages it depends on

A package can be built if:
- All its dependencies exist
- All its dependencies can be built
- There is no circular dependency in its dependency chain

**Task:** Write a function `can_build(package, deps)` that returns:
- `True` if the package can be built
- `False` otherwise

### Example Input

```python
dependencies = {
    "A": ["B", "C"],
    "B": [],
    "C": ["B"]
}
```

### Expected Output

```python
can_build("A", dependencies)  # True
```

### Solution

```python
def can_build(package, deps):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    state = {}

    def dfs(pkg):
        # Missing dependency
        if pkg not in deps:
            return False

        # Cycle detected
        if state.get(pkg) == VISITING:
            return False

        # Already checked and buildable
        if state.get(pkg) == VISITED:
            return True

        # Mark as visiting
        state[pkg] = VISITING

        # Check dependencies
        for dep in deps[pkg]:
            if not dfs(dep):
                return False

        # Mark as visited (buildable)
        state[pkg] = VISITED
        return True

    return dfs(package)
```

### Test Cases

#### ✅ Your Case (Buildable)

```python
deps = {
    "A": ["B", "C"],
    "B": [],
    "C": ["B"]
}

print(can_build("A", deps))  # True
```

#### ❌ Cycle Case

```python
deps = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print(can_build("A", deps))  # False
```

#### ❌ Missing Dependency

```python
deps = {
    "A": ["B"],
    "B": ["C"]  # C missing
}

print(can_build("A", deps))  # False
```

---

## Case 2: Solution - Topological Sort

### Problem Statement (Interview Style)

You are given a dictionary of package dependencies.

- Each key is a package
- Each value is a list of packages it depends on

**Tasks:**
- Determine whether all packages can be built
- If yes, return a valid build order
- If no, detect a cycle

### Example Input

```python
packages = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
```

### Key Insight (Topological Sort)

A topological order exists if and only if the dependency graph has no cycles.

We will use **Kahn's Algorithm**.

### How Kahn's Algorithm Works

**Step 1:** Build the graph
- Edges go dependency → package
- Example:
  ```
  D → B → A
  D → C → A
  ```

**Step 2:** Compute indegrees
- `indegree[pkg]` = number of dependencies

**Step 3:** Start with indegree = 0 nodes
- These can be built immediately.

**Step 4:** Remove them and update neighbors
- Repeat until:
  - All nodes processed → ✅ buildable
  - Some nodes left → ❌ cycle detected

### Python Solution: Build Order + Cycle Detection

```python
from collections import defaultdict, deque

def build_packages(packages):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Initialize indegree
    for pkg in packages:
        indegree[pkg] = 0

    # Build graph and indegree
    for pkg, deps in packages.items():
        for dep in deps:
            if dep not in packages:
                return False, "Missing dependency", None
            graph[dep].append(pkg)
            indegree[pkg] += 1

    # Queue of buildable packages
    queue = deque([pkg for pkg in indegree if indegree[pkg] == 0])

    build_order = []

    while queue:
        pkg = queue.popleft()
        build_order.append(pkg)

        for neighbor in graph[pkg]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle detection
    if len(build_order) != len(packages):
        return False, "Cycle detected", None

    return True, "Build successful", build_order
```

### Test Cases

#### ✅ Buildable Case

```python
packages = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

ok, msg, order = build_packages(packages)
print(ok)      # True
print(order)   # ['D', 'B', 'C', 'A'] (one valid order)
```

#### ❌ Cycle Detected

```python
packages = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

ok, msg, order = build_packages(packages)
print(ok)   # False
print(msg)  # Cycle detected
```

#### ❌ Missing Dependency

```python
packages = {
    "A": ["B"],
    "B": ["C"]  # C missing
}

ok, msg, order = build_packages(packages)
print(ok)   # False
print(msg)  # Missing dependency
```

### How Cycle Detection Works Here

Topological sort does NOT explicitly search for cycles.

Instead:

🔴 **If after processing all possible nodes, some nodes still have indegree > 0 → they are part of a cycle**

This is guaranteed by graph theory.

#### Visual Cycle Failure

```
A → B → C → A

Indegrees:
A:1  B:1  C:1

No node has indegree 0 → algorithm cannot start → ❌ cycle
```

---

## Additional Approach: DFS with Recursion Stack

### 1️⃣ DFS with Recursion Stack (Simplest & Most Common)

**Idea:**

While doing DFS:
- Mark a node as visited
- Also mark it as in current path
- If you see a node that's already in the current path, you found a cycle

**Why it's simple:**
- One DFS
- Two boolean arrays / sets
- Very easy to explain in interviews

**Pseudocode:**

```python
visited = set()
in_stack = set()

def dfs(node):
    if node in in_stack:
        return True   # cycle
    if node in visited:
        return False

    visited.add(node)
    in_stack.add(node)

    for neigh in graph[node]:
        if dfs(neigh):
            return True

    in_stack.remove(node)
    return False
```

**Use when:**
- Graph is directed
- You just want yes/no cycle
- Dependency problems
