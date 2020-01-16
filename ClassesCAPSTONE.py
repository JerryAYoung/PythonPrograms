##Classes (Product Inventory Project)
"""
class Product():
	def __init__(self, price, name):
		self.price = price
		self.name = name

class Inventory():
	def __init__(self, products):
		self.products = products

	def value(self):
		return sum(inventory.products)

apples = Product(0.25, 'Apple')
oranges = Product(0.95, 'Orange')
steaks = Product(7.99, 'Steak')
inventory = Inventory(36 * [apples.price] + 12 * [oranges.price] + 3 * [steaks.price])

print(f'Entire inventory is worth: ${inventory.value()}')
"""

##Classes (Airline/ Hotel Reservation System)
class Plane():
	def __init__(self, sections_list):
		self.sections_list = sections_list

class Plane_Section():
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def show_section(self, section):
		print(f'The plane section is called: {self.name} with a price of ${self.price}')

first_class = Plane_Section('First Class', 450)
regular = Plane_Section('Regular Class', 150)
lower = Plane_Section('Lower Class', 55)

sections_list = [first_class, regular, lower]
sections_list = Plane(sections_list)

first_class.show_section(first_class)


