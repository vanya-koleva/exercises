def multiply_items(items: list[int]) -> int:
    total_sum = 1
    for item in items:
        total_sum *= item
    return total_sum


my_list = [2, 3, 4]
print(multiply_items(my_list))
