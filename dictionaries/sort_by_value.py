def sorted_dict(some_dict, reverse=False):
    sorted_values = dict(sorted(some_dict.items(), key=lambda x: x[1], reverse=reverse))
    return sorted_values


sample_dict = {"one": 1, "four": 4, "two": 2, "five": 5, "three": 3}

print("Sorted by values in ascending order:")
print(sorted_dict(sample_dict))
print("Sorted by values in descending order:")
print(sorted_dict(sample_dict, reverse=True))

