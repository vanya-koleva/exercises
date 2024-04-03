sample_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
result = 1
for key in sample_dict.keys():
    result *= sample_dict[key]
print(result)
