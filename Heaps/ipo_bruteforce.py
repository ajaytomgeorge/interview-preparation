from collections import defaultdict
import heapq
project_to_complete = 3
current_capital = 0
profits = [1,2,3]
capitals = [0,1,2]


max_capital = 0
capital_profit_heap = defaultdict(list)
for i, capital in enumerate(capitals):
    capital_profit_heap[capital].append(profits[i])

for _ in range(project_to_complete):
    if current_capital in  capital_profit_heap.keys():
        key = current_capital
    else:
        key = sorted(capital_profit_heap.keys(), reverse=True)[0]

    current_capital += sorted(capital_profit_heap[key],reverse=True)[0]
print(current_capital)





