def count_occurrences(s: str) -> dict:
    s_list = s.split()
    counts = {}
    for word in s_list:
        if word not in counts:
            occurrences = s.count(word)
            counts[word] = occurrences
    return counts


some_string = input()
print(count_occurrences(some_string))
