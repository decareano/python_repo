def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		#return number // 2
	elif number % 2 == 1:
		result = 3 * number + 1
		print(result)
		#return result

ab = input("Give me a number:")

while ab != 1:
	ab = collatz(int(ab))
