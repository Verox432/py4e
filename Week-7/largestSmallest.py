largest = None
smallest = None
while True:
	num = input("Enter a number: ")
	if num == 'done' :
		break

	try :
		numInt = int(num)
	except :
		print('Invalid input')
		continue

	if smallest is None :
		smallest = numInt
	if largest is None :
		largest = numInt

	if smallest > numInt :
		smallest = numInt
	if largest < numInt :
		largest = numInt

print("Maximum is", largest)
print('Minimum is', smallest)
