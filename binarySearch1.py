def binarySearch(arr, l, h, x):
	if h >= l:
		mid = h +l//2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		else:
			return binarySearch(arr, mid+1, r, x)

	else:
		return -1

arr = [10,20,30,40,50,60,70,80]
x = int(input("Enter element you want to search: "))
z = binarySearch(arr, 0, len(arr)-1, x)

if z == -1:
	print("Element not found!!!")
else:
	print("Element found at position: ",z)


