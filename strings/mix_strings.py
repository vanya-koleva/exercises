def mix_strings(str1, str2) -> str:
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2


print(mix_strings('abc', 'xyz'))
