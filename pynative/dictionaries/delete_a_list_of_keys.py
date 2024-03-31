sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

sample_dict = {key: sample_dict[key] for key in sample_dict.keys() if key not in keys}
# for key in keys:
#     sample_dict.pop(key)

print(sample_dict)
