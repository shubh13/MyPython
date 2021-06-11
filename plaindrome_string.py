#Solution 6(b)

def check_palindrome_string(test_string):
    reverse_string = "".join(test_string[::-1])

    return True if test_string == reverse_string else False

input_string = input("Enter the string : ")

if(check_palindrome_string(input_string)):
    print("Palindrome")
else:
    print("Not Palindrome")