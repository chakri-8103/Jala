class Solution:
    def show(self, a, b=None):
        if b is None:
            print(f"One Parameter: {a}")
        else:
            print(f"Two Parameters: {a}, {b}")
obj = Solution()
obj.show(25)
obj.show(80,65)