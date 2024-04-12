# Write a Python class named Student with two instances student1, student2 and
# assign values to the instances' attributes.
# Print all the attributes of the student1, student2 instances with their values.
class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id

    def display(self):
        return f"Student name: {self.student_name}, student ID: {self.student_id}"


student1 = Student("Maria Ivanova", 100100)
student2 = Student("John Atanasov", 100101)
print(student1.display())
print(student2.display())
