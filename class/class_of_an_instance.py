# Write a Python program to get the class name of an instance in Python.
class MyClass:
    pass


instance = MyClass()
print(type(instance).__name__)
