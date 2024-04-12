# Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class and display the entire attribute and the values of the class.
# Now remove the student_name attribute and display the entire attribute with values.
class Student:
    student_id = "100100"
    student_name = "Maria Ivanova"


Student.student_class = "5A"
for attr, value in Student.__dict__.items():
    if not attr.startswith("_"):
        print(f"{attr} - {value}")

del Student.student_name
print("\nChanged attributes:")
for attr, value in Student.__dict__.items():
    if not attr.startswith("_"):
        print(f"{attr} - {value}")
