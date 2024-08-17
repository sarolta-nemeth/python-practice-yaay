def where_is_waldo(arr):
	if arr:
		repeated_elem = ""
		if arr[0][0] == arr[0][1]:
			repeated_elem = arr[0][0]
		else:
			repeated_elem = arr[0][2]
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				if arr[i][j] != repeated_elem:
					return [i+1, j+1]
		return "Waldo was not found :("
	return "Array is empty"
			
test_arr1 = [
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
]

test_arr2 = [
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
]

test_arr3 = [
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
]

test_arr4 = []

test_arr5 = [
["W", "W", "W"],
["W", "W", "W"],
["W", "W", "W"]
]

print(where_is_waldo(test_arr1))
print(where_is_waldo(test_arr2))
print(where_is_waldo(test_arr3))
print(where_is_waldo(test_arr4))
print(where_is_waldo(test_arr5))

