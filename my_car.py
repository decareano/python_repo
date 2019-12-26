from _review_code import Car, ElectricCar

my_new_car = Car('toyota', 'x43', 2016)
print(my_new_car.a_description())

my_new_car.odometer_reading = 55
my_new_car.read_odometer()

my_tesla = ElectricCar('Tesla', 'roadster', 2016)
print(my_tesla.a_description())
