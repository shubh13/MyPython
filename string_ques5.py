#Solution 5

my_string = "I am the flower"

#sorting the string alphabetically
new_string = my_string.replace(" ", "")
print("".join(sorted(new_string.lower())))

#rearranging string in descending order of length of the words

temp_string = my_string
value_list = []
word_len = {}
descending_string = ""

def get_dict_value(value):
    for keys, values in word_len.items():
        if values == value:
            return keys

for words in temp_string.split():
    keys = words
    values = len(words)

    word_len[keys] = values

for values in word_len.values():
    value_list.append(values)

for values in sorted(value_list, reverse=True):
    descending_string+=get_dict_value(values)+" "

print(descending_string)