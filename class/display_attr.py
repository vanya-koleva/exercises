# Write a Python class named Student with two attributes: student_id, student_name.
# Add a new attribute: student_class.
# Create a function to display all attributes and their values in the Student class.
class Student:
    student_id = 100100
    student_name = "Maria Ivanova"

    def display_attr():
        for attr, value in Student.__dict__.items():
            if not attr.startswith("_") and attr != "display":
                print(attr, value)


Student.student_class = "5B"
Student.display_attr()
