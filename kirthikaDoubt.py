new=open("newTxt.txt","x")
new=open("newTxt.txt","w")
new.write("I am the file under the file operation I store only text data")
new.write ("my encoding is usually in UTF-8 format")
new.write("my encoding allows me to besecured and safe while interrupting data and acessing the data")

new=open("newTxt.txt","r")
print(new.read(20))
print(new.readline())
print(new.readline())

print(new.read())