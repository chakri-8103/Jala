class Example:
    def method(self, a, b, mode="default"):
        if mode == "first":
            print(f"First Method: {a}, {b}")
        else:
            print(f"Second Method: {a}, {b}")

obj = Example()
obj.method(10, 20, "first")
obj.method(10, 20)
