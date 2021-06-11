def maxProfit(l):
    profit = 0
    while l:
        max_cost = max(l)
        for i in range(0, l.index(max_cost)):
            if l[i] < 0:
                profit = None
                print('one or more values in the list is negative.')
                break
            temp = max_cost-l[i]
            if temp > profit:
                profit = temp
        l.remove(max_cost)

    return (f'profit : {profit}')

print(maxProfit([10, 10, 11, 12, 9, 2, -24]))