# A namespace is a system that has a unique name for each and every o
# object in python. An object might be a variable or a method.
# Python scopes are implemented as dictionaries that map names to objects. These dictionaries are commonly called namespaces. These are the concrete mechanisms that Python uses to store names. 
# They’re stored in a special attribute called .__dict__.

# LEGB
# Local Enclosing Global Built-in

x = "global x"


def outside():
    x = "outer x"

    def inside():
        nonlocal x
        # print(x)
        print(x)

    inside()
    print(x)


outside()


# builtin
print(len("abc"))
len = "abc"
print(len("abcdd"))
