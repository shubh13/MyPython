#Using recursion to count even numbers in range of i to n

def i_count_evens(i, n,  count):
  if i%2 == 0 and i <= n:
    count+=1
    i_count_evens(i+1, n, count)
  elif i <= n:
    i_count_evens(i+1, n, count)
  else:
    print(count)
    
i = int(input("Enter the starting value of the range : "))
n = int(input("Enter the final value of the range : "))

print("Number of even numbers in the range of ", i, "and ", n, " is : ", i_count_evens(i, n, 0))