#The code below accesses a file which is placed at the local directory

filename = "foo.txt"

f = open(filename, "r")

print(f.read())  #Read all the values present in the file

f.close()

f = open("foo.txt", "w")
f.write("I have been written later")

f.close()

f = open("foo.txt", "r+")
print(f.read())
f.close()

f = open("foo.txt", "r")
print(f.readline())  #Read the file line by line

print(f.read(5)) #Read any stream of characters with a specified size

for values in f:
    print(values) #The values that are printed are taken one line at a time

f.close()


#The code to access any file in some foreign directory
import os 

HOME_PATH = '/home/shubhadeep'
target = 'Desktop'
filename = 'newfoo.txt'
pathname = os.path.join(HOME_PATH, target, filename)

f = open(pathname, "r")
print("Reading File in a foreign directory\n\n")
print(f.read())