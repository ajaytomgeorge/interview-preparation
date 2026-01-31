
import heapq
project_to_complete = 3
current_capital = 0
profits = [1,2,3]
capitals = [0,1,2]
projects  = list(zip(capitals,profits))
projects.sort()
max_heap =[]
i = 0
for _ in range(project_to_complete):
    while i < len(projects) and projects[i][0]<=current_capital:
        heapq.heappush(max_heap, -projects[i][1] )
        i = i + 1
    current_capital +=-heapq.heappop(max_heap)

print(current_capital)