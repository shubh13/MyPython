print("Hello world")

print("Welcome to VS Code")

#variables : Those entities which are used to store values and can be changed during execution

#string variables

a = "Hello"
b = "World"

print(a+b)

#integer variables

a = 10
b = 20
print(a+b)

#defining variable names : a-z, A-Z, 0-9 in combination of letters, space not allowed, only _ allowed

a = "ABCDEFGHIJK"
a1 = "ABCDEFGH"
a_1 = "ABCDEF"

#input variables int = integer float = decimal str = string boolean = boolean

a = int(input("Enter a number : "))
print(a)

a = True
b = False

print(a)
print(b)

#control statement is a block of code that controls the outcome according to cond.
#if - else
#there is a condition A if it is true then print Even else print odd

a = True
if a:
    print("Even")
else:
    print("Odd")

#test an integer enetered by the user is odd or even

a = int(input("Enter an integer : "))
if a%2==0: # %(modulo division) it directly returns the remainder, == comparison
    print("Even")
else:
    print("Odd")

#wap to calculate the number of even numbers between 1 and 20

count = 0
for i in range(1,20):
    if i%2==0:
        count+=1 #count = count + 1 
    
print("The value of count is : ", count)

#in range of 1 to 30 check if the number entered by the user exists or not.
