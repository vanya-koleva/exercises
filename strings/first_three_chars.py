# Write a Python function to get a string made of the first three characters
# of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_three(s: str) -> str:
    if len(s) < 3:
        return s
    return s[:3]


print(first_three('ipy'))
print(first_three('python'))
print(first_three("p"))
