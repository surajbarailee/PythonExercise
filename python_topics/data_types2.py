"""
LISTS

Square Brackets: []
Collection of items and of different types
Ordered
Changable
list()
Belongs to class list



CPython’s lists are really variable-length arrays, not Lisp-style linked lists. The implementation uses a contiguous array of references to other objects, and keeps a pointer to this array and the array’s length in a list head structure.

This makes indexing a list a[i] an operation whose cost is independent of the size of the list or the value of the index.

When items are appended or inserted, the array of references is resized. 
Some cleverness is applied to improve the performance of appending items repeatedly;
when the array must be grown, some extra space is allocated so the next few times don’t require an actual resize.


The elements in the list are not stored themselves. 
Instead, every element of the list is stored at random locations, 
and the list stores the address of those random locations.


Whenever we created the list ls with 4 elements we reserved a continuous block of memory which can store 4 elements consecutively. 
The list we were having was : ls = [1, 2 , 'Medium' , 1.2]
Suppose now we want to store a new element 'Happy' at the end of the list 'ls'. So we can't be sure that there is an empty space at the end of the list and for that reason python uses resizing for optimizing this problem. The moment we will use append to add the element 'Happy' at the end of list :
ls.append('Happy')
So if there is no empty space at the end of the list 'ls' python will find a new block in the memory of double the size of the list 'ls' and copy all the element of the list 'ls' into it and now 'ls' will point to that new list & then append the new element at end at there is enough space for more new elements. This process is called Resizing of List and is used in python because lists are dynamically allocated. Finallyour list will look like :
ls = [1, 2 , 'Medium' , 1.2 , 'Happy'] #With more spaces left


http://www.laurentluce.com/posts/python-list-implementation/


"""


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist.remove("banana")
thislist.pop()
del thislist[0]
thislist.clear()

# We have arrays in python as well but not supported built in data types.
import array

myarray = array.array("i", [5, 6, 7, 2, 3, 5])
print(myarray)
myarray[0] = 1
print(myarray)


"""
TUPLES:
Tuple items are ordered, unchangeable, and allow duplicate values.
Uses parenthesis
Single tuple has a comma to show it is a tuple.
"""
x = (1,)
print(type(x))

y = 1
print(type(y))

print(x[0])
# x[0] = 2  # This will give an TypeError because tuples are immutable


"""
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Not Subscriptable
unchangable meaning you can add or remove but you cant index and change that element 
Uses curly braces
#sets are unordered, it rearranges itself in sorted order


SETS are stored as keys in a dictionary just with no values. 
[In 3.7 dictionaries are ordered but implementation of sets are unchanged]
Keys are hashed, and hash values are assigned to slots in a dynamic table (it can grow or shrink based on needs).
And that mapping process can lead to collisions, 
meaning that a key will have to be slotted in a next slot based on what is already there.




"""

x = {"hi", 2, "bye", "Hello World", 1}
x.add(10)
x.remove(1)
print(x)
# print(x[0])
for i in x:
    print(i)


# for i in range(len(x)):
#     print(x[i])


x = {"hi", 2, "bye", "Hello World", 1}
print(x)


x = {1, 5, 6, 3, 4, 5}
print(x)  # see how it gets ordered

# Understanding why there is a perceived order requires understanding a few things:

# That Python uses hash sets,

# How CPython's hash set is stored in memory and

# How numbers get hashed

# https://stackoverflow.com/questions/15479928/why-is-the-order-in-dictionaries-and-sets-arbitrary
# Look at the second comment


print(set([1, True]))  # prints {1} because True is treated as 1 in python


"""The frozenset() inbuilt function is used to create a frozen set. We can pass any iterable like list, set, tuple, etc and it will return us an immutable set of class type frozenset.

Syntax:

frozenset(iterable)
Example:
"""
immutable_set = frozenset((2, 4, 2, 1, 2, 3))
print(immutable_set)


"""
DICTIONARIES 
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example
Print the "brand" value of the dictionary:


"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])


for i in thisdict:
    print(i)

for i in thisdict.values():
    print(i)

for i in thisdict.keys():
    print(i)

for i in thisdict.items():  # returns tuple
    print(i)

for i, j in thisdict.items():
    print(i, j)




print("=======HEY========")  

# returns a view object that displays a list of all the keys in the dictionary in order of insertion.

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())


"""
Range in python


The range() method returns an immutable sequence of numbers between the given start integer to the stop integer.
range(stop)
range(start, stop[, step])


In Python 2, there are two functions that allow you to generate a sequence of integers, range and xrange. These functions are very similar, with the main difference being that range returns a list, and xrange returns an xrange object.

In Python 3, the xrange function has been dropped, and the range function behaves similarly to the Python 2 xrange. Python 3 range is not a function but rather a type that represents an immutable sequence of numbers.



In python3 range belongs to class range,returns an object of class range which is an iterable.
It doesnt implement list under the hood as python2 used to do making it memory efficient.

"""
