def find_minimum_coins(coins, amount):
    op = [float("inf")]*(amount+1)
    paths = ["inf"]*(amount+1)
    op[0]=0

    for i in range(1, amount+1):
        for coin in coins:
            if i>= coin:
                op[i] = min(op[i], op[i-coin]+1)
                if op[i-coin] < op[i]:
                    paths[i] = coin
    newamount = amount
    while True:
        if amount <= 0:
            break
        coin = paths[amount]
        print(coin)
        amount = amount - coin

    return op[newamount]

print("nubmer of coins")
print(find_minimum_coins([1,2,5], 13))

    