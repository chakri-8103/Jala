def second_smallest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[1] if len(unique_arr) > 1 else None

print(second_smallest([10, 20, 4, 45, 99]))
