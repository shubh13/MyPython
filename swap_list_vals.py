#Solution 1

integer_list_1 = [1, 2, 3]
integer_list_2 = [4, 5, 6]


if len(integer_list_1) != len(integer_list_2):
    print("Swapping not possible")

for index in range(len(integer_list_1)):
    integer_list_1[index], integer_list_2[index] = integer_list_2[index], integer_list_1[index]

print("Ineteger List 1 : ", integer_list_1, "\n Integer List 2 : ", integer_list_2)