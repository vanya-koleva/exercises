# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_sting_middle(str1, str2) -> str:
    middle = len(str1) // 2
    return str1[:middle] + str2 + str1[middle:]


print(insert_sting_middle('[[]]<<>>', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
