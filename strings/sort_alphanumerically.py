def sort_words(list_of_words: list) -> str:
    return ", ".join(sorted(set(list_of_words)))


words = input().split(", ")
print(sort_words(words))
