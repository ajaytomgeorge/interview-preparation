graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

from collections import deque
def bfs(start,end):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        start = queue.popleft()
        for nb in graph[start]:
            if nb ==end:
                print("found")
                break
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)

bfs('A','F')