filename = "hellofoo.txt"
String = 'I am a superfoo file and will have an interesting file operation.'
appendString = ''

fileCreate = open(filename, 'x')
fileWrite = open(filename, 'w').write(String)

fileRead = open(filename, 'r')

for line in fileRead:
    for word in line.split():
        appendString+=word[0]+word[:0:-1]+' '

print(appendString)

fileAppend = open(filename, 'a').write(appendString)
print(fileRead.read())