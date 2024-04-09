def exchange_chars(s: str) -> str:
    new_s = s[-1] + s[1:-1] + s[0]
    return new_s


some_string = input()
print(exchange_chars(some_string))
