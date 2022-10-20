my_string = " Never look back"
my_dict = {}

letter_list = list(set(my_string))
for i in range(len(letter_list)):
    my_dict[letter_list[i]] = my_string.count(letter_list[i])

print(my_dict)