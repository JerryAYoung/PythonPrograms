while True:
	try:
		num = int(input("Pick a number! Any number at all: "))
		if num > 1:
			for i in range (2, num):
				if num % i == 0:
					print(f"{num} is not a prime number")
					break
				else: 
					print(f"{num} is a prime number!")
					break
		else:
			print(f"{num} is not a prime number!")
			break
	except:
		print('That was not a valid integer, try again. ')
