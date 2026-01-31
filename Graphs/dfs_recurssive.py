

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
def dfs(start,end, visited={}):
    if start == end:
        print("found")
        return True:
    
    for nb in graph[start]:
        if nb not in visited:
            visited.add(nb)
            if dfs(nb,end, visited):
                return True
    
    return True
        

print(dfs('A','F',{'A'}))
        
