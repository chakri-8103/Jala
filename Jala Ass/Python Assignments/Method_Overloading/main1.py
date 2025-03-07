class Example:
    def method(self, *args):
        if len(args) == 0:
            print("No Parameters")
        elif len(args) == 1:
            print(f"One Parameter: {args[0]}")
        elif len(args) == 2:
            print(f"Two Parameters: {args[0]}, {args[1]}")

obj = Example()
obj.method()
obj.method(10)
obj.method(10, 20)
