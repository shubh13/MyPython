import os

filename = 'question2.txt'
fileread = open(filename, mode='rt')
fileWrite = open(filename, mode='w')
String1 = 'I am a file containing special characters like @ # $ % ^ "" [] {} and etc.'
String2 = '\nMy objective is to be in the local directory where the parent program exists.'

def fileOps(filename):
    fileWrite.write(String1+String2)
    print(fileread.readline(),"\n",fileread.read(6),"\n",fileread.read())

if os.path.isfile(filename):
    fileOps(filename)
else:
    fileCreate = open(filename, mode='x')
    fileOps(filename)
    
