# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def count_words(words: list[str]) -> int:
    counter = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            counter += 1
    return counter


my_list = ['abc', 'xyz', 'aba', '1221']
print(count_words(my_list))
