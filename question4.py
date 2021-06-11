filename = 'wordCount.txt'
string = 'I am a file whose word count is the result.'

def charSpaceCount(filename, charCount, spaceCount):
    fileLine = open(filename, 'r').read()

    for index in range(len(fileLine)-1):
        if fileLine[index] != ' ':
            charCount+=1
        else:
            spaceCount+=1

    return charCount, spaceCount

appendString = 'The word count of the file '+ str(charSpaceCount(filename, 0, 0))

try:
    fileWrite = open(filename, 'w').write(string)
    open(filename, 'a').write(appendString)
finally:
    open(filename).close()