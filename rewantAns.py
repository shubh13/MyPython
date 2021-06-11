def maxProfit(l):
    profit = 0
    while l:
        max_cost = max(l)
        for i in range(0, l.index(max_cost)):
            temp = max_cost-l[i]
            if temp > profit:
                profit = temp
        l.remove(max_cost)

    return profit

print(maxProfit([-14, -12]))