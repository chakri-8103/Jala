a = input('Enter name of the file: ')
f = open(a, "r")

folder = input('Enter a Folder: ')
file = input('Enter a File: ')

try:
    from folder import file
except Exception as e:
    print(f"Error: {e}")
