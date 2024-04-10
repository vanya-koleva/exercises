# Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag: str, word: str) -> str:
    return f"<{tag}>{word}</{tag}>"


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
