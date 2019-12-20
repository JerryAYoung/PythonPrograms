import pandas

##Defined global variables 
dictionary_of_clothes = pandas.read_csv("catalog.csv")
price = 0
verify = 'n'

##Choose an item and stores your active price
def get_price(dictionary_of_clothes, price):
	while True:
		print(dictionary_of_clothes)
		user_item_price = input("Which clothing piece would you like? ")
		if user_item_price == "Jeans":
			price = price + 25
			return price
		elif user_item_price == "Shirt":
			price = price + 10
			return price
		elif user_item_price == "Shoes":
			price = price + 35
			return price
		elif user_item_price == "Hat":
			price = price + 15
			return price
		else:
			print('That isnt an item! Choose from the list. ')

##Gets final price including tax
def get_tax(price):
	while True:
		print(f'Your total before tax is ${price}! ')
		tax_rate = 0.095
		total_tax = price * tax_rate
		final_total = total_tax + price
		if final_total < 35:
			print(f"${final_total} is your final total! You are very cheap! ")
			return total_tax, final_total
		else:
			print(f"${final_total} is your final total! Big spender I see! ")
			return total_tax, final_total

##Asks user if they are done shopping
def done_shopping():
	verify = 'n'
	verify = input("Are you done shopping today? (y/n) ")
	if verify == 'y':
		print('Alright lets go to the checkout!')
		return verify
	else:
		print('Already lets go back to shopping!')
		return verify

##Checkout system
def checkout():
	total_tax, final_total = get_tax(price)
	return print(f"RECEIPT: \nBase Price: ${price:.2f} \nTotal Tax (9.5%): ${total_tax:.2f} \nFinal Price: ${final_total:.2f}")

while True:
	if verify == 'n':
		price = get_price(dictionary_of_clothes, price)
		print(price)
		verify = done_shopping()
		if verify == 'n':
			price = get_price(dictionary_of_clothes, price)
			print(price)
			verify = done_shopping()
	else:
		break

final_total = checkout()





