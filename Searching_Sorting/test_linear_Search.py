import unittest

def linearSearch(numbers, search_key):
    found = False

    for values in numbers:
        if search_key == values:
            found = True
            break
        else:
            found = False

    return found


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(linearSearch([1, 2, 3, 4], 4), True)

    def test_case_2(self):
        self.assertEqual(linearSearch([1, 2, 10, 11, 13, 51, 21, 3, 6], 51), True)

    def test_case_3(self):
        self.assertEqual(linearSearch([1, 3, 10, 11, 12, 17, 14], 2), False)