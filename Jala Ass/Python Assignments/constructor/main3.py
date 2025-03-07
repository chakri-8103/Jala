class Example:
    def __init__(self):  
        print("Public Constructor Called")

    def _protected(self):
        print("Protected Constructor-like Method Called")

    def __private(self):
        print("Private Constructor-like Method Called")

obj = Example()
obj._protected()
