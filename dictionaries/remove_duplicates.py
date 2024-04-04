sample_dict = {"one": 1, "two": 2, "three": 3, "2": 2, "1": 1}
result = {}
for key, value in sample_dict.items():
    if value not in result.values():
        result[key] = value
print(result)
