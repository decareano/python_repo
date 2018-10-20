class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 120
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make  + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) + " miles in it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(mileage)
            print(self.odometer_reading)
        else:
            print("nope, cannot roll back odometer")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(140)

my_new_car.read_odometer()


