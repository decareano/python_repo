class Restaurant():
    def __init__(self, resto_name, cuisine_type):
       self.resto_name = resto_name
       self.cuisine_type = cuisine_type

    def describe_resto(self):
    	print(self.resto_name.title() + " serves " + self.cuisine_type.title())

    def open_resto(self):
       """ simulate open resto """
       print(self.resto_name.title() + " is now open")
       #import pdb; pdb.set_trace()


resto = Restaurant('decareano', 'mexican')
print("resto_name is " + resto.resto_name.title() + ".")
print(resto.open_resto())
resto.describe_resto()
resto.open_resto

resto1 = Restaurant('maragata', 'california cuisine')
resto1.describe_resto()

class User():
	def __init__(self, first_name, last_name, employee_id, address, mobile_phone, emergency_contact, previous_employer):
		self.first_name = first_name
		self.last_name = last_name
		self.employee_id = employee_id
		self.address = address
		self.mobile_phone = mobile_phone
		self.emergency_contact = emergency_contact
		self.previous_employer = previous_employer

	def describe_user(self):
		print("Hi, " + self.first_name, self.last_name + 
			"your employee_id is" + self.employee_id + " and your mobile_phone is " + self.mobile_phone + "." + 
			"You used to work for " + self.previous_employer)

	def greet_user(self):
		print("Welcome to the company, " + self.first_name + "!")


user1 = User('Marcelo', 'Gobelli', '1405', '101 Main', '415-333-3456', 'charlie smith', 'GE')
print(user1.describe_user())