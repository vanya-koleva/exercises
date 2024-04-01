def check_key(key):
    if key in sample_dict:
        print("The key exists.")
    else:
        print("The key does not exist.")


sample_dict = {"one": 1, "two": 2, "three": 3}
#print(sample_dict.get("one", "The key does not exist."))
check_key("one")
