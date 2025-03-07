folder=input('Enter a Folder:')
file=input('Enter a File:')
try:
    from folder import file
except Error:
    print("Error: Class not Found.")