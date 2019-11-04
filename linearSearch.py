def linearSearch(l, x):
	for i in range(len(l)):
		if (l[i] == x):
			return i
	return -1
x = int(input("Enter element you want to search: "))
z = linearSearch([3,4,5,1,6,7,9], x)
if (z == -1):
	print("Element not found")

else:
	print("Element found at index: ",z)