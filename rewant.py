def strip(word):
    return word[0]+word[:0:-1]

try:
    string1 = ''

    f = open('superfoo.txt', 'w')
    f.write("I am a superfoo file and will have an interesting file operation. \n")

    f = open('superfoo.txt', 'r')
    for i in f:
        l1 = i.split()
        for j in l1:
            string1 += strip(j) + ' '
            continue

    print(string1)
    f = open('superfoo.txt', 'a')
    f.write(f'The reversed line : {string1}\n')

finally:
    f.close()