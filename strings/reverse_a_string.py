# Write a Python function to reverse a string if its length is a multiple of 4

def reverse_string(s: str) -> str:
    if len(s) % 4 == 0:
        return s[::-1]
    return s


print(reverse_string("abcd"))
print(reverse_string("python"))
