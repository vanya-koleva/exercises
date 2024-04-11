# Write a Python function student_data ()
# that will print the ID of a student (student_id).
# If the user passes an argument student_name or student_class
# the function will print the student name and class.
def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if "student_name" in kwargs:
        print(f"Student name: {kwargs['student_name']}")
    elif "student_class" in kwargs:
        print(f"Student class: {kwargs['student_class']}")


student_data(student_id='SV12', student_name='Jean Garner')
