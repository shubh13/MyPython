String = 'I am a superfoo file and will have an interesting file operation.'
appendString = ''

filename = 'superfoo.txt'
try:
    filewrite = open(filename, mode='w').write(String)

    with open(filename, 'r') as fileread:
        for line in fileread:
            for words in line.split():
                appendString += words[0]+words[:0:-1]+' '

    fileappend = open(filename, 'a').write(appendString)
    print(open(filename, 'r').read())
finally:
    open(filename).close()