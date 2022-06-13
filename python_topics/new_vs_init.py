# new and then init
# new is what creates the instance and init is the method that does initialization
#  instance variables are local to an instance. So anything you are doing in init is local to that instance only.
# But anything you are doing in new will be affecting anything created for that type.


class Demo:
    def __new__(cls, *args):
        print("__new__ called")
        return object.__new__(cls)

    def __init__(self):
        print("__init__ called")


d = Demo()

# SingleTon Design Principle

# This can be a global config and you dont want your user to create multiple instance
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


x = Singleton()
y = Singleton()
print(x)
print(y)
print(id(x) == id(y))
