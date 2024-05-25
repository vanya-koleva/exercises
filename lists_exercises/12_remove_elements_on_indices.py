some_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
some_list = [x for i, x in enumerate(some_list) if i not in (0, 4, 5)]
print(some_list)
