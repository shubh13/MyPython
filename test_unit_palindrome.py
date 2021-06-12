import unittest

def check_palindrome_string(test_string):
    reverse_string = "".join(test_string[::-1])

    return True if test_string == reverse_string else False

class TestCase(unittest.TestCase):
    def test_case_1(self):
        return self.assertEqual(check_palindrome_string("radar"), True)

    def test_case_2(self):
        return self.assertEqual(check_palindrome_string("hello"), False)