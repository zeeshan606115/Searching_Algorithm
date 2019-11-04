def binarySearch(l, val):
	low = 0
	high = len(l)-1
	index = -1
	while((low <= high) and(index == -1)):
		mid = high + low // 2
		if l[mid] == val:
			index = mid
		elif val < l[mid]:
			high = mid - 1

		else:
			low = mid + 1
	return index

x = int(input("Enter the value you want to search: "))
z = binarySearch([1,2,3,5,6,7,9,11,23,34,55],x)
if (z == -1):
	print("Element not found")

else:
	print("Element found at index position: ",z)