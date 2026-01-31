from collections import defaultdict
coins = [1,3,5,6]
target = 11

smallest_num_coins = defaultdict(lambda:float("inf"))
smallest_num_coins[0] = 0
for i in range(1,target+1):
    print(i)
    for coin in coins:
        if i - coin >=0:
            smallest_num_coins[i] = min(smallest_num_coins[i - coin]+1, smallest_num_coins[i])

print(smallest_num_coins)
