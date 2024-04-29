def find_longer_words(words: list[str], n: int) -> list[str]:
    longer_words = [x for x in words if len(x) > n]
    return longer_words


list_of_words = input().split()
n = int(input())
print(find_longer_words(list_of_words, n))
