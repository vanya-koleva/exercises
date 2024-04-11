# Write a Python program to create an instance of a specified class
# and display the namespace of the said instance.
class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


me = Person("John", "Smith")
print(me.__dict__)
