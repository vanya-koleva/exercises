def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), reverse=reverse))


sample_dict = {"d": 4, "a": 1, "c": 5, "b": 2, "e": 3}
print(dict(sort_dict_by_key(sample_dict)))
