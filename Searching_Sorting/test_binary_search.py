import unittest

def binary_search(numbers, key, least_index, max_index):

    if numbers != sorted(numbers):
        return False

    mid_index = least_index+max_index//2

    if numbers[mid_index] == key:
        return True
    elif numbers[mid_index] < key:
        return binary_search(numbers, key, least_index, mid_index-1)
    else:
        return binary_search(numbers, key, mid_index, max_index)

class TestBinarySearch(unittest.TestCase):
    def test_case_1(self):
        numbers = [1, 2, 3, 4]
        return self.assertEqual(binary_search(numbers, 3, 0, len(numbers)-1), True)

    def test_case_2(self):
        numbers = [1, 3, 2, 4]
        return self.assertEqual(binary_search(numbers, 4, 0, len(numbers)-1), False)

    def test_case_3(self):
        numbers = [10, 21, 22, 31, 101, 116, 135]
        return self.assertEqual(binary_search(numbers, 116, 0, len(numbers)-1), True)