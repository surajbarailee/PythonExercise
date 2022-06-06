class Pet:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


# INTROSPECTION is a way to find what it is or what it does


class Clownfish(Pet):
    def swim(self):
        print(f"{self.name}, swims")


marvin = Clownfish("Marvin")

print(dir(marvin))  # The classes are defaultly inherited from object class
print(marvin.__dict__)
print(type(marvin))
print(isinstance(marvin, Clownfish))
print(issubclass(Clownfish, Pet))

# INSPECT
import inspect
from functools import wraps


def who_called_me(callable_):
    wraps(callable_)

    def wrapper(*args, **kwargs):
        caller = inspect.stack()[1]
        print(f"{callable_.__name__} is called by {caller.function}")

        return callable_(*args, **kwargs)

    return wrapper


@who_called_me
def peter():
    print("hello")


def james():
    peter()


print("===================================")
james()

print("===============================")
# REFLECTIONS


class Greeting:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, greet):
        def call_():
            greeting_msg = greet.replace("_", " ")
            print(f"{self.name}, {greeting_msg}")

        return call_


greeting = Greeting("suraj")
greeting.nice_to_meet_you()
greeting.hello_bro()


help(Greeting)
