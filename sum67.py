#Solution 6(a)

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
            
print(sum67([1, 2, 2, 6, 12, 13, 14, 7, 1]))