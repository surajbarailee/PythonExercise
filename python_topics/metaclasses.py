# Code That manipulates code
# Why would you care ?
#   Extensively used in frameworks
#   Can help to move to DRY code


# METACLASSES


def hello():
    class Hello:
        pass

    return Hello


# class is an object itself
# This means class itself must have some sort of upper class from which it was made
# MetaClass defines the rules of the class and defines how this class is created


# class Test:
#     pass


# print(Test)
# print(Test())
# print(type(Test()))
# print(type(Test))  # Type of class type
# This type is what essentially defines the class behaviour
#
Test = type("Test", (), {})  # this line of code is equal to class Test: pass
# Test is name for internal usage


class Foo:
    def show(self):
        print("Hello")


def add_attribute(self):
    self.z = 8


# Name Test is internal representation of class
# Foo if we are inheriting something
# and then attributes
Test = type("Test", (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test()
t.wy = "hello"
print(t.wy)


# Getting Into Metaclasses


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        # modify object instantiation
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")


d = Dog()
print(dir(d))


# Never to allow some attributes
# Change attributes to your desire
# Can be used in framework when you want your user to be very specific

##########################################################################################
# Mind-bending metaclasses-adding function overloads
# The wizardry of Metaprogramming
