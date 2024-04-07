def find_longest_word(lst: list[str]) -> str:
    longest_word = max(lst, key=len)
    return longest_word


result = find_longest_word(["PHP", "Exercises", "Backend"])
print(f"Longest word: {result}")
print(f"Length of the longest word: {len(result)}")
