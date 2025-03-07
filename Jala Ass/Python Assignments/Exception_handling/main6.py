class Solution(Exception):
    def __init__(self, message):
        super().__init__(message)

def checking(value):
    if value < 0:
        raise Solution("Negative values are not allowed.")
    if value==0:
        raise Solution("Zero is not allowed.")
n=int(input('Enter a value:'))
checking(n)