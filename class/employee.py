class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.emp_salary = self.emp_salary + (overtime * (salary / 50))

    def print_employee_details(self):
        print(f"Name: {self.emp_name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: {self.emp_salary}")
        print(f"Department: {self.emp_department}")


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp1.assign_department("OPERATIONS")
emp4.assign_department("SALES")

emp2.calculate_salary(45000, 52)
emp4.calculate_salary(45000, 60)

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()
