"""Short Introduction to Variables in python
"""


"""
Variables are containers for storing data values.
In python variable is a symbolic name that is reference or pointer to an object.
Once an object is assigned to a variable, the variable can be used to refer to the object.
But the data itself is still contained within an object.

Variables are dynamically typed in python.
The type of a variable is determined by the value assigned to it at.
The type of a variable is determined at run time.




The same a can hold different data types.
Unlike in java where "a" variable can hold only one data type.
And the data type should be defined at the time of declaration.
In java we do something like :
int a = 10;
String a = "Hello";
float a = 10.5;
"""


a = 10
a = "Hello"
a = 10.5
a = True
a = None
a = [1, 2, 3]
a = (1, 2, 3)
a = {1, 2, 3}
a = {"a": 1, "b": 2}

# To print a variable, use the print() function.
a = 10
print(a)
print("The value of a is:", a)
print(f"The value of a is: {a}")
print("The value of a is: %s" % a)
print("{0}".format(a))


# The variables in python are case sensitive.
# A and a are different
# "abcd" and "ABCD" are different
abcd = 100

ABCD = 200


print(abcd, ABCD)
