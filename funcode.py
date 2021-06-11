String = "A for apple"

for i in String:
    ch = ''
    ch+=i
    if i == ' ':
        print(ch)
        ch=''        