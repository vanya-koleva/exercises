def not_poor(s:str) -> str:
    s_not = s.find("not")
    s_poor = s.find("poor")
    if s_poor > s_not > 0 and s_poor > 0:
        s = s.replace(s[s_not: s_poor + 4], "good", 1)
    return s


some_string = input()
print(not_poor(some_string))
