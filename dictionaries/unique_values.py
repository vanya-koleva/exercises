sample_data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]
unique_values = set(val for dic in sample_data for val in dic.values())
print(unique_values)
