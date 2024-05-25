def common_element(first_list, second_list):
    if set(first_list).intersection(set(second_list)):
        return True
    return False


print(common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_element([1, 2, 3, 4, 5], [6, 7, 8, 9]))
