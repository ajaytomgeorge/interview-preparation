from collections import defaultdict
exchange_rates = [
    ("USD", "EUR", 0.9),
    ("EUR", "GBP", 0.8),
    ("USD", "JPY", 110),
    ("JPY", "GBP", 0.0065),
    ("EUR", "JPY", 120)
]

source = "USD"
target = "GBP"
amount = 1000



currency_conversion_graph = defaultdict(list)
for source_cur, dest_cur, rate in exchange_rates:
    currency_conversion_graph[source_cur].append((dest_cur,rate))
    currency_conversion_graph[dest_cur].append((source_cur,1/rate))


print(currency_conversion_graph)


def find_rate_visited_add_inside_for_loop(source, target, visited, current_rate =1, path = ''):
    if source == target:
        path +="found"
        return current_rate, path
    for connected_currency, rate in currency_conversion_graph[source]:
        if connected_currency not in visited:
            visited.add(connected_currency)
            final_rate, path = find_rate_visited_add_inside_for_loop(connected_currency, target, visited, rate*current_rate,path = path+' '+connected_currency)
            if final_rate > 0:
                print("found rate", final_rate, path)
                print("\n")
            visited.remove(connected_currency) #backtracking

    return -1 , ''


def find_rate(source, target, visited, current_rate =1, path = ''):
    if source == target:
        path +="found"
        return current_rate, path
    visited.add(source)
    for connected_currency, rate in currency_conversion_graph[source]:
        if connected_currency not in visited:
            final_rate, path = find_rate(connected_currency, target, visited, rate*current_rate,path = path+' '+connected_currency)
            if final_rate > 0:
                print("found rate", final_rate, path)
                print("\n")

    #visited.remove(source)  # if we want to backtrack
    return -1 , ''


#find_rate(source, target, set())
find_rate_visited_add_inside_for_loop(source, target, {source})