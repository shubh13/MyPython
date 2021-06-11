filename = "question2.txt"

try:
    file = open(filename, "x")
    file = open(filename, "w")
    file.write('I am a file containing special characters like @ # $ % ^ "" [] {} and etc.')
    file.write('\nMy objective is to be in the local directory where the parent program exists.')

    file.close()
    
except FileExistsError:
    file = open(filename, "r+")
    print(file.readline())
    print(file.read(6))
    print(file.read())

    file.close()

else:
    file = open(filename, "r+")
    print(file.readline() and file.read(6) and file.read())
    file.close()

#WAP to create a file named as superfoo.txt where it stores the following text data
#"I am a superfoo file and will have an interesting file operation." The program should be able to extract
#this line of text and reverse each word except its first letter. And then append the modified string to the file.