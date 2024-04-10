def split_string(s: str, ch: str) -> str:
    idx = s.find(ch)
    return s[:idx]


some_string = input("Enter string: ")
char = input("Enter the character to split the string: ")
print(split_string(some_string, char))
