#Access the file and open

f = open("foo.txt", "r")

print(f.read(10))
print(f.readline())
print(f.read()) #read() once executed takes the file pointer at the end of the file post which further reads 
#don't result in any ouput
print(f.readline())

f.close()

#WAP to read first 3 characters of a file named output.txt then read consecutive lines
#Output.txt : 
# This file contains covid-19 virus data. 
# Also many analysed data

f = open("output.txt", "r", encoding="utf-8")

print(f.read(3))
print(f.readline())
print(f.readline())

f.close()

#creating a new file
newFile = open("created.txt", "x") #is used for creating a new text file named as created.txt
newFile = open("created.txt", "w") #writing into the file.

newFile.write("I have been just created")

newFile.close()



