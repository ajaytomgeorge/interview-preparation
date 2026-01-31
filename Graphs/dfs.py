

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(start,end):
    stack = [start]
    visited = {start}
    while stack:
        node = stack.pop()
        for nb in graph[node]:
            if nb == end:
                print("found")
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)

dfs('A','F')