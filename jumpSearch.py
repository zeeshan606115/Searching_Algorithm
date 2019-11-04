import math

def jumpSearch(arr, val):
	length = len(arr)
	jump = int(math.sqrt(length))
	low, high = 0,0
	while low < length and arr[low] <= val:
		high = min(length - 1, low + jump)
		if arr[low] <= val and arr[high] >= val:
			break
		low += jump
	if low >= length or arr[low] > val:
		return -1
	high = min(length - 1, high)
	i = low

	while i <= high and arr[i] <= val:
		if arr[i] == val:
			return i
		i += 1
	return -1

x = int(input("Enter element you want to search: "))
z = jumpSearch([1,2,3,4,5,6,7,8],x)

if (z == -1):
	print("Element {} not found in list".format(x))
else:
	print("Element {} found at index: {}".format(x,z))