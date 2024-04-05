def replace_char(s: str):
    char = s[0]
    s = s.replace(char, "$")
    s = char + s[1:]
    return s


print(replace_char("restart"))
