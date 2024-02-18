class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12
    
# Add your code below!
# PartTimeEmployee extends Employee
# Employee is parent class and PartTimeEmployee is child class
# super is Employee and it makes sense that full_time_wage is
# calling super for calculate_wage
class PartTimeEmployee(Employee):
    # def calculate_wage(self, hours):
    #     self.hours = hours
    #     return hours * 12
    
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

obj = PartTimeEmployee("Milton")
#print(a_test.calculate_wage(10))
print(obj.full_time_wage(10))
