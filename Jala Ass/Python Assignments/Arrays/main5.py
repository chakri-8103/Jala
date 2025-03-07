def remove_element(arr, value):
    return [x for x in arr if x != value]

print(remove_element([1, 2, 3, 4, 2], 2))
