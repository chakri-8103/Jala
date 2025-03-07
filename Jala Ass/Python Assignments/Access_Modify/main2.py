#2.Creating a main class.

from subclasses import _protected
class naming():
    def __init__(self):
        access=_protected()
        print(access._message)
obj=naming()



#2.1Creating a subclass.

class _protected():
    def __init__(self):
        self._message='welcome to vs code'
        print(self._message)
obj=_protected()