# Write a Python class that has two methods: get_String and print_String ,
# get_String accept a string from the user and print_String prints the string in upper case.
class MyString:
    def __init__(self):
        self.some_string = ""

    def get_String(self):
        self.some_string = input()

    def print_String(self):
        print(self.some_string.upper())


str1 = MyString()
str1.get_String()
str1.print_String()
