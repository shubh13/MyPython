random_ints = [1, 2, 2, 3, 4, 5, 4, 5, 4, 6, 7, 8, 1, 9, 6, 1, 2, 3, 4, 9]

freq_dict = {}
flipped_dict = {}
value_list = []
sublist = []

def get_dict_values(values):
    for keys, dictvalues in flipped_dict.items():
        if keys == values:
            return dictvalues

#Creating a frequency dictionary
for value in random_ints:
    keys = value
    values = random_ints.count(keys) 

    freq_dict[keys] = values

#Creating a modified dictionary by clubbing the keys with same frequency values as a single list
for keys, values in freq_dict.items():
    if values not in flipped_dict:
        flipped_dict[values] = [keys]
    else:
        flipped_dict[values].append(keys)

#Extracting the keys which are frequency values in a list
for keys in flipped_dict.keys():
    sublist.append(keys)

#Extracting values from the modified dictionary according to ascending order of their frequencies
for frequencies in sorted(sublist):
    value_list.append(get_dict_values(frequencies))

print(value_list)