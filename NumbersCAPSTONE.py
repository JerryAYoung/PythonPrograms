import math

##Numbers (Find Pi to the Nth digit)
def display_pi(number):
	print('{:.{}f}'.format(math.pi, num))

##Numbers (Find e to the Nth digit)

def display_e(number):
	print('{:.{}f}'.format(math.e, num))

##Numbers (Fibonacci Sequence)
def fib(number):
	if number < 0:
		print('Must be larger than 0')
	elif number == 1:
		return 0
	elif number == 2:
		return 1
	else:
		return fib(number-1) + fib(number-2)

##Numbers (Prime Factorization)
def prime(num):
	if num > 1:
		for n in range(2, num):
			if num % 2 == 0:
				print('Not a prime number')
				break
		else:
			print('Is a prime number')
	else:
		print('Is not a prime number')

##Numbers (Next Prime Number)
def find_nextprime():
	pass

##Numbers (Find Cost of Tile to Cover W x H Floor)
def cost_of_tile(w_cost, h_cost):
	totalcost = w_cost * h_cost
	return totalcost

##Numbers (Mortgage Calculator)
def mortgage(mortgage_period, mortgage_price):
	interest_rate = 0.095
	yearly_payments = mortgage_price/mortgage_period
	monthly_payments = yearly_payments/12
	print(f'Interest Rate: 9.5% \nYour monthly payments over {mortgage_period} years will be: {monthly_payments}'.format())

##Numbers (Change Return Program)
def change_return(cost, given_money):
	if given_money < cost:
		print("You arent giving enough money for the payment!")
	elif given_money == cost:
		print('You are owed no change!')
	else:
		change_needed = given_money - cost
		change_needed = round(change_needed, 2)
		print(f'Your change owed is ${change_needed}!')
		print(change_needed//0.25, 'Quarters')
		change_needed = change_needed % 0.25
		print(change_needed//0.10, 'Dimes')
		change_needed = change_needed % 0.10
		print(change_needed//0.05, 'Nickels')
		change_needed = change_needed % 0.05
		print(change_needed//0.01, 'Pennys')
		change_needed = change_needed % 0.01

##Numbers (Binary to Decimal and Back Convertor)
def bin_to_dec(dec_num):
	pass

##Numbers (Calculator)
def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	return a / b

def calculator():
	while True:
		number1 = int(input('Enter first number: '))
		choice = int(input('Select operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n'))
		number2 = int(input('Enter second number: '))
		if choice == 1:
			print(number1, '+', number2, '=', add(number1, number2))
		elif choice == 2:
			print(number1, '-', number2, '=', subtract(number1, number2))
		elif choice == 3:
			print(number1, '*', number2, '=', multiply(number1, number2))
		elif choice == 4:
			print(number1, '/', number2, '=', subtract(number1, number2))
		else:
			print('Error')





