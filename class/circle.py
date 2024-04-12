# Write a Python class named Circle constructed from a radius and
# two methods that will compute the area and the perimeter of a circle
class Circle:
    __pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.__pi * self.radius ** 2

    def get_perimeter(self):
        return Circle.__pi * self.radius * 2


circle1 = Circle(4)
print(circle1.get_area())
print(circle1.get_perimeter())
