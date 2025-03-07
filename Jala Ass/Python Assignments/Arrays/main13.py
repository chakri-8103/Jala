def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

print(second_largest([10, 20, 4, 45, 99])) 
