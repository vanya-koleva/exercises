def remove_char(s: str, idx: int) -> str:
    first_part = s[:idx]
    second_part = s[idx+1:]
    return first_part + second_part


some_string = input()
index = int(input())
print(remove_char(some_string, index))
