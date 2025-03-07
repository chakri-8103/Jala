def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

print(remove_duplicates([1, 2, 3, 4, 2, 3, 5]))
