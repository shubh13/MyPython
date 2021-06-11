import unittest

def sum67(numbers):
    flag = True
    result_sum = 0

    for value in numbers:
        if value == 6:
            flag = False

        if flag:
            result_sum+= value
        
        if value == 7:
            flag = True

    return result_sum

class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum67([1, 2, 2, 6, 7]), 5)

    def test_case_2(self):
        self.assertEqual(sum67([1, 2, 2, 6, 6, 7, 7, 2]), 14)

    def test_case_3(self):
        self.assertEqual(sum67([1, 2, 2, 3, 6, 6, 7, 7, 2]), 17)