def result(s):
    if len(s) > 1:
        new_string = s[:2] + s[-2:]
    else:
        new_string = ""
    return new_string


sample_string = input()
print(result(sample_string))
