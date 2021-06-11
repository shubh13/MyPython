import pytest

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
            
def test_answer1():
    assert sum67([1, 2, 3, 6, 11, 12, 13, 7, 1]) == 7

def test_answer2():
    assert sum67([1, 2, 2, 6, 7]) == 5 

def test_answer3():    
    assert sum67([1, 2, 2, 3, 6, 6, 7, 7, 2]) == 17