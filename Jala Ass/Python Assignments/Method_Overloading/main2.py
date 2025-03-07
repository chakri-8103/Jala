class Example:
    def method(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            print(f"Integer and String: {args[0]}, {args[1]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
            print(f"String and Integer: {args[0]}, {args[1]}")
        else:
            print("Other Combination")

obj = Example()
obj.method(10, "Hello")
obj.method("Hello", 10)
obj.method()
