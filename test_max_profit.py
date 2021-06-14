import unittest

def maxprofit(transactions):
    profitlist = []
    profit = 0

    if len(transactions) == 1 or sum(transactions) < 0:
        return 0
    
    for i in range(len(transactions)-1):
        for j in range(i+1, len(transactions)):
            profit = transactions[j]-transactions[i]
            profitlist.append(profit)
    
    return max(profitlist) if max(profitlist) > 0 else 0

class Test(unittest.TestCase):
    def test_case_1(self):
        return self.assertEqual(maxprofit([8, 1, 9, 15, 21, 2, 8]), 20)

    def test_case_2(self):
        return self.assertEqual(maxprofit([10]), 0)

    def test_case_3(self):
        return self.assertEqual(maxprofit([10, 12, 13, 17, 21, 11, 9]), 11)