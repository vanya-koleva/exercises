first_list = [1, 3, 5, 7, 9]
second_list = [1, 2, 4, 6, 7, 8]
difference = set(first_list).symmetric_difference(second_list)
print(list(difference))
