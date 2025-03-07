class Solution:
    def display(self, a, b):  
        if isinstance(a,int) and isinstance(b,int):
            print(f"Integer Method: {a} and {b}")
        else:
            print(f"String Method: {a} and {b}")
obj = Solution()
obj.display(10, 20)  
obj.display("Hello", "World")  