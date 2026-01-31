from collections import deque
from collections import defaultdict
equations = [["USD", "EUR"], ["EUR", "JPY"]]
values = [0.9, 120]
queries = [["USD", "JPY"], ["JPY", "USD"], ["USD", "GBP"]]

currency_graph =defaultdict(list)
for i, value in enumerate(values):
    currency_graph[equations[i][0]].append((equations[i][1], value))
    currency_graph[equations[i][1]].append((equations[i][0], 1/value))


def bfs_search(source, target): 
    bfs_queue = deque([(source,1)])
    visited = set()
    while bfs_queue:
        pop_node, current_rate= bfs_queue.popleft()
        if pop_node == target:
            return current_rate
        for neigh_node, rate in currency_graph[pop_node]:
            if neigh_node not in visited:
                visited.add(neigh_node)
                bfs_queue.append((neigh_node, current_rate * rate ))

    return -1





def dfs_search(source, target): 
    dfs_queue = [(source,1)]
    visited = {source}
    while dfs_queue:
        pop_node, current_rate= dfs_queue.pop()
        if pop_node == target:
            return current_rate
        for neigh_node, rate in currency_graph[pop_node]:
            if neigh_node not in visited:
                visited.add(neigh_node)
                dfs_queue.append((neigh_node, current_rate * rate ))

    return -1

def dfs_recursion(source, target, current_rate, visited):
    if source == target:
        print("taget reach")
        return target, current_rate

    visited.add(source)
    for neigh_node, rate in currency_graph[source]:
        if neigh_node not in visited:
            match, weight = dfs_recursion(neigh_node,target, current_rate*rate, visited)
            if weight > 0 :
                print("found", weight)
                return match, weight


    return None, -1

print(dfs_recursion("USD","JPY",1, set()))    

