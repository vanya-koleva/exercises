sample_string = "Python is great"

my_dict = {}

for letter in sample_string:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)
