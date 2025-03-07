def count_even_odd(arr):
    even = sum(1 for x in arr if x % 2 == 0)
    odd = len(arr) - even
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6])) 
