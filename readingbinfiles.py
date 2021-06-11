file = open("humanHeart.png", 'rb')
new_file = open('question3.txt', 'rb')
#print(file.read())
#print(new_file.read())


sentence = bytearray('I am a binaryfile'.encode('ascii'))
binaryFile = open('IamBinary.bin', 'wb').write(sentence)
print(open('IamBinary.bin', 'rb').read())