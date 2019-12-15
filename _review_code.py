class Car():
    """ represent a car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        

    def a_description(self):
    	""" return a neatly defined name"""
    	long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    	return long_name.title()

    def read_odometer(self):
        """ print a statement showing car's mileage"""
        print("this car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """ set odometer reading to a given value"""
        #self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("cannot roll back the odometer...thats a no-no")
    def increment_odometer(self, miles):
        """ add to a given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery():
    """ a simple attempt to model a battery for an electric car """
    def __init__(self, battery_size=70):
        """ what are the batteries attributes """
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print statement about the range this battery provides """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attr of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    #def describe_battery(self):
        #"""print a statement describing the battery size"""
        #print("This car has a " + str(self.battery_size) + "-kWh battery.")
        

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.a_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

a_new_car = Car('audi', 'a4', 2016)
print(a_new_car.a_description())
another_new_car = Car("subaru", "outback", 2013)
print(another_new_car.a_description())
another_new_car.update_odometer(30000)
another_new_car.read_odometer()
another_new_car.increment_odometer(200)
another_new_car.read_odometer()
another_new_car.update_odometer(21000)
another_new_car.read_odometer()
