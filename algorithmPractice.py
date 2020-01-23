##Linear Search
unsortedArray = [12, 8, 10, 5, 40, 67]
def linearSearch(x, array):
	for i in range(len(array)):
		if array[i] == x:
			return i
	return -1

result = linearSearch(5, unsortedArray)
print(f"Linear Search of {unsortedArray}")
print(f"The index position of 5 is: {result}!")

##Binary Search
sortedArray = [1, 3, 4, 6, 7, 8, 10]
def binarySearch(sortedArray, l, r, x):
	if r >= l:
		mid = l + (r-1)/2
		mid = int(mid)
		if sortedArray[mid] == x:
			return mid
		elif sortedArray[mid] > x:
			return binarySearch(sortedArray, l, mid-1, x)
		else:
			return binarySearch(sortedArray, mid+1, r, x)
	else:
		return -1

result = binarySearch(sortedArray, 0, len(sortedArray)-1, 7)
print(f"Binary Search of {sortedArray}")
print(f"The index position of 7 is: {result}!")