class Employee:
    """Employee class is used to hold employee object data.

    Methods:
        __init__(self, emp_id, emp_name)
        print()
    """

    def __init__(self, emp_id, emp_name):
        """Employee Class Constructor to initialize the object.

        Input Arguments: emp_id must be int, emp_name must be str
        """
        self.id = emp_id
        self.name = emp_name

    def print(self):
        """This method prints the employee information in a user friendly way."""
        print(f'Employee data selected with an f format[{self.id}, {self.name}]')
print("________")
print(Employee.__doc__)
print(Employee.__init__.__doc__)
print("________")
print(Employee.print.__doc__)

aa = Employee(1234, "manuel miranda")
print(Employee.print(aa))
