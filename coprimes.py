#Test paper Question 2

count_gcd_pairs = 0

def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return b

    if a>b:
        return gcd(a-b, b)
    return gcd(a, b-a)

n = int(input("Enter the range of the numbers : "))

for values in range(n-1):
    if gcd(values, values+1) == 1:
        count_gcd_pairs+=1
    
print("The number of coprime pairs are : ", count_gcd_pairs)