class Solution:
    def show(self, *args):  
        if len(args) == 1:
            print(f"One Parameter: {args[0]} (Type: {type(args[0]).__name__})")
        elif len(args) == 2:
            print(f"Two Parameters: {args[0]} (Type: {type(args[0]).__name__}), {args[1]} (Type: {type(args[1]).__name__})")
        else:
            print("Invalid number of arguments")

obj = Solution()
obj.show(1)        
obj.show("Chakradhar", 21)  
obj.show("0.001", True)  