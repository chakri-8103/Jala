a=input('Enter a file path:')
try:
    with open("a", "r") as f:
        res = f.read()
except OSError as e:
    print("IO Exception occurred:", e)