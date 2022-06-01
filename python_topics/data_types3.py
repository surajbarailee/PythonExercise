"""
Python has a module called collections that features a little modified version of data types.

They are :
Counters
OrderedDicts
DefaultDicts
ChainMaps
NamedTuples
Deque
UserDict
UserList
UserString
"""

from collections import (
    Counter,
    OrderedDict,
    defaultdict,
    ChainMap,
    namedtuple,
    deque,
    UserDict,
    UserList,
    UserString,
)

# counter example
# counter is subclass of dict
my_list = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]

my_counter = Counter(my_list)
print(type(my_counter))
print(issubclass(Counter, dict))
print(my_counter)
print(issubclass(bool, int))
my_counter.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_counter)


# OrderedDict
# SubClass of dictionary but unlike dictionary it maintains the order of the keys in which they are inserted
# But after python 3.7 it is kind of unnecessary for main purpose.
# However it is useful for some other methods that it provides.
# move_to_end(key, last=True) can be one example.
# Though python supports this, other frameworks built using python may not
# assume that dictionary is ordered and order matters.

print(issubclass(OrderedDict, dict))
print("This is an Ordered Dict:")
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4


for key, value in od.items():
    print(key, value)


# DefaultDict
# The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError.
# It provides a default value for the key that does not exists.


def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d = defaultdict(int)  # default value is 0.0 here.
# float is callable. Int is callable,etc

d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


# ChainMap
# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"e": 5, "f": 6}
d4 = {"f": 5, "e": 7}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
c = c.new_child(d4)

print("=======================================")
print(c)

# Accessing Values using key name
print(c["f"])
# First value is accessed and  Ordering is done as the dictionaries are passed in function

# Accessing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())


# Named Tuples
# their elements can be accessed by both their attribute name and the positional index.
# Declaring namedtuple()
# 'Student' is  the name of the generated class:
Student = namedtuple("Student", ["name", "age", "DOB"])

# Adding values
S = Student("Nandini", "19", "2541997")
print(type(S))
print(type(Student))
# type is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass.
print(type(namedtuple))
# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)


# 20

# It sets the name of the generated class:

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# Point
# <class '__main__.Point'>
# Point = namedtuple('Foobar', ['x', 'y'])
# Point
# <class '__main__.Foobar'>
# The Point name in your globals is just a reference to the generated class, the class itself needs to have a name. The name cannot be taken from the variable to which the object is assigned, because the class is generated first and only then assigned in a separate step (after the namedtuple() call returns).


# Deque

# Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.
# Declaring deque
queue = deque(["name", "age", "DOB"])

print(queue)


# initializing deque
de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)


# UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality.


class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
d = MyDict({"a": 1, "b": 2, "c": 3})

# d.pop(1)


# UserList
# UserList is a list like container that acts as a wrapper around the list objects.
# This is useful when someone wants to create their own list with some modified or additional functionality.


class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")

# Deleting From List
# L.remove()


# UserString is a string like container and just like UserDict and UserList it acts as a wrapper around string objects.
# It is used when someone wants to create their own strings with some modified or additional functionality.


class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)
