# Write a Python class named Rectangle constructed from length and width
# and a method that will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


rectangle1 = Rectangle(4, 5)
print(rectangle1.get_area())
