def add_ending(s: str) -> str:
    if len(s) < 3:
        return s
    elif s.endswith("ing"):
        s += "ly"
    else:
        s += "ing"
    return s


sample_str = input()
print(add_ending(sample_str))
