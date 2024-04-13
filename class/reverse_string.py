# Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'
class MyClass:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(MyClass().reverse_words('hello .py'))
