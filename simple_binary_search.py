'''A standard iterative implementation of binary search that returns the index of the found element
in an array and -1 when not found'''

def binary_search(target, array):
	if array == None:
		return "array is of NoneType"
	lower_index = 0
	upper_index = len(array) - 1
	while lower_index <= upper_index:
		match_index = int(lower_index + (upper_index - lower_index) / 2)
		if array[match_index] < target:
			lower_index = match_index + 1
		elif array[match_index] == target:
			return match_index
		else:
			upper_index = match_index - 1
	return -1 # not found 


def main():
	test_array = None
	target = 2
	found = binary_search(20, test_array)
	print(found)


if __name__ == '__main__':
	main()
