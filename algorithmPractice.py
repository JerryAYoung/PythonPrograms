##Linear Search

array = [3, 7, 9]

def linearSearch(x, array):
	for i in range(len(array)):
		if array[i] == x:
			return i
		return -1


sortedArray = [1, 3, 4, 6, 7, 8, 10]

def binarySearch(sortedArray, l, r, x):
	if r >= l:
		mid = l + (r-1)/2
		if sortedArray[mid] == x:
			return mid
		elif sortedArray[mid] > x:
			return binarySearch(sortedArray, l, mid-1, x)
		else:
			return binarySearch(sortedArray, mid+1, r, x)
	else:
		return -1

result = binarySearch(sortedArray, 0, len(sortedArray)-1, 7)