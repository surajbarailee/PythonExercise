# What happens when we create a variable called "a" in python?

# Application when run is given a memory portion that can be divided into 4 chunks.
# Code : Instruction
# Static/Global : Global variable values
# Stack :function calls, local vairables, etc
# Heap
# When you create a variable called "a" in python
a = 100

# The interpreter will create an integer object commonly known as PyObject.
# Gives it the value 100
# And assigns the variable "a" to refer to the object.


"""
Heap Memory and Stack Memory

Both are the part of RAM.
Heap are allocated in random order while stack are allocated in contiguous blovk of memory.
Heap memory are flexible and can be resized and Stack Memory is fixed.
Heap memory are not thread safe 
Stack memory are thread safe as they can be accessed by owner thread only.
"""

"""
When we create an integer a = 100
Python creates  Pyobject in the heap memory.
Then python creates the reference to the object called "a" in the stack memory.
"""

a = 100
b = 100


"""

        STACK                                               HEAP

a       5123123                                             Pyobject with value 100 
        This is the memory
        address of the object

b      5123123
        This is the memory
        address of the same object as a



# id(a) gives the memory address of the object that is referred by the variable "a"
# stored in the stack memory.



"""


"""
Objects are structures allocated on the heap.  Special rules apply to
the use of objects to ensure they are properly garbage-collected.
Objects are never allocated statically or on the stack; they must be
accessed through special macros and functions only.  (Type objects are
exceptions to the first rule; the standard types are represented by
statically initialized type objects, although work on type/class unification
for Python 2.2 made it possible to have heap-allocated type objects too).
An object has a 'reference count' that is increased or decreased when a
pointer to the object is copied or deleted; when the reference count
reaches zero there are no references to the object left and it can be
removed from the heap.

An object has a 'type' that determines what it represents and what kind
of data it contains.  An object's type is fixed when it is created.
Types themselves are represented as objects; an object contains a
pointer to the corresponding type object.  The type itself has a type
pointer pointing to the object representing the type 'type', which
contains a pointer to itself!.


Objects do not float around in memory; once allocated an object keeps
the same size and address.  Objects that must hold variable-size data
can contain pointers to variable-size parts of the object.  Not all
objects of the same type have the same size; but the size cannot change
after allocation.  (These restrictions are made so a reference to an
object can be simply a pointer -- moving an object would require
updating all the pointers, and changing an object's size would require
moving it if there was another object right next to it.)
Objects are always accessed through pointers of the type 'PyObject *'.

The type 'PyObject' is a structure that only contains the reference count
and the type pointer.  The actual memory allocated for an object
contains other data that can only be accessed after casting the pointer
to a pointer to a longer structure type.  This longer type must start
with the reference count and type fields; the macro PyObject_HEAD should be
used for this (to accommodate for future changes).  The implementation
of a particular object type can cast the object pointer to the proper
type and back.


"""


# Memory Management in python :

# Reference Counting in python


import ctypes

# list object which is referenced by
# my_list
my_list = [1, 2, 3]

my_list1 = my_list
my_list2 = my_list
# finding the id of list object
my_list_address = id(my_list)

# finds reference count of my_list
ref_count = ctypes.c_long.from_address(my_list_address).value

print(f"Reference count for my_list is: {ref_count}")


#


"""
Garbage Collection in python


Reference Counting in python
        Space Overhead
        Running everytime we assign something
        Not generally thread safe
        Reference counting doesnt detect cyclical references
        
        
        
        Tracing Garbage Collection in python : Mark and Sweep
        Generational Garbage collection is based on he theory that most object die young
        





"""


"""

Python program doesnt shrink in memory after garbage collection.
the freed memory is fragmented.
        -> Its not freed in one continuous block.
        
When we say memory is freed during garbage collection,
its released back to python to use for other objects not necesarily to the system

__slots__ is used to limit the number of attributes that can be added to a class.


class Point:
        __slots__ = ('x', 'y')
point = Point()
point.name = "asdasd"  = > Now you cant do this shit

when to use __slots__ ?
Creating many instances of a class
Know in advance what properties the class should have



weakref
A weakref to an object is not enough to keep it alive
When the only remaining references are weakrefs, the object is garbage collected.
Useful for implementing caches or mappings holding large objects





GIL

Global Interpreter Lock
Prevents multiple threads from running Python code in parallel.


Only one thread can run in the interpreter at a time.


If you want to take advantage of multiple cores, you can use multiprocessing.
"""


"""
References:
https://www.analyticsvidhya.com/blog/2021/04/an-overview-of-python-memory-management/
https://www.youtube.com/watch?v=URNdRl97q_0
https://www.youtube.com/watch?v=arxWaw-E8QQ
https://docs.python.org/3/c-api/memory.html#overview




"""
