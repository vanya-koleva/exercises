# Write a Python program to remove duplicates from a list.
def clean_list(lst: list) -> list:
    new_list = []
    for ele in lst:
        if ele not in new_list:
            new_list.append(ele)
    return new_list


my_list = [1, 1, 2, 3, 3]
print(clean_list(my_list))
