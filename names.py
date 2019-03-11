from name_function import get_formatted_name

print("enter 'q' at any time")
while True:
	first = input("first: ")
	if first == 'q':
		break
	last = input("last: ")
	if last == 'q':
		break
	formatted_name = get_formatted_name(first, last)
	print("\neatly formatted name: " + formatted_name + ".")
