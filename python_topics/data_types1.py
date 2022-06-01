"""
    
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


You can get the type of an object using the type() function.

    
"""
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
x = None  # NoneType


"""
STRINGS

strings in python are surrounded by either single or double quotation marks.
single character in python is a string of length 1. and double character is a string of length 2.
Single characters are not treated differently as compared to other programming languages.

Strings are non-mutable objects in python. so you cant do something like this::
my_string[0] = "b"


Theoretically CPython can store:
Short answer would be: if you have over 100GB of RAM, one Python string can use up that much memory.

9 quintillion characters* on a 64 bit system on CPython 3.10

That's only if your string is made up of only ASCII characters. The max length can be smaller depending on what characters the string contains due to the way CPython implements strings:

9,223,372,036,854,775,758 characters if your string only has ASCII characters (U+00 to U+7F) or
9,223,372,036,854,775,734 characters if your string only has ASCII characters and characters from the Latin-1 Supplement Unicode block (U+80 to U+FF) or
4,611,686,018,427,387,866 characters if your string only contains characters in the Basic Multilingual Plane (for example if it contains Cyrillic letters but no emojis, i.e. U+0100 to U+FFFF) or
2,305,843,009,213,693,932 characters if your string might contain at least one emoji (more formally, if it can contain a character outside the Basic Multilingual Plane, i.e. U+10000 and above)
On a 32 bit system it's around 2 billion or 500 million characters. 


Python strings are length-prefixed, so their length is limited by the size of the integer holding their length and the amount of memory available on your system. 
Since PEP 353, Python uses Py_ssize_t as the data type for storing container length. Py_ssize_t is defined as the same size as the compiler's size_t but signed. 
On a 64 bit system, size_t is 64. 1 bit for the sign means you have 63 bits for the actual quantity, meaning CPython strings cannot be larger than 2⁶³ - 1 bytes or around 9 million TB (8EiB). 
This much RAM would cost you around 40 billion dollars if we multiply today's price of around $4/GB by 9 billion. On 32-bit systems (which are rare these days), it's 2³¹ - 1 bytes or 2GiB.

CPython will use 1, 2 or 4 bytes per character, depending on how many bytes it needs to encode the "longest" character in your string. 
So for example if you have a string like 'aaaaaaaaa', the a's each take 1 byte to store, but if you have a string like 'aaaaaaaaa😀' then all the a's will now take 4 bytes each. 
1-byte-per-character strings will also use either 48 or 72 bytes of metadata and 2 or 4 bytes-per-character strings will take 72 bytes for metadata. 
Each string also has an extra character at the end for a terminating null, so the empty string is actually 49 bytes.

https://stackoverflow.com/questions/1739913/what-is-the-max-length-of-a-python-string
https://docs.python.org/3.3/howto/unicode.html




"""

my_string = "a"

my_string1 = "Hello this is a string"

my_string2 = """Hello this is a second string
that is multiline"""

print(my_string[0])


""" Strings are non-mutable objects in python. so you cant do something like this::
my_string[0] = "b"
or delete my_string[0]"""

print(my_string1 + my_string2)
print(len(my_string1))
for i in my_string1:
    print(i)


print("a" in my_string1)


"""
INTEGERS

max int in python also probably depends upon the platform size



"""
import sys

print(sys.maxsize)


x = 9223372036854775807

print(type(x))  # int

x = 9223372036854775807123123123123

print(type(x))  # int

print(x)

# hex oct bin representation


# In Python integers will automatically switch from a fixed-size int representation into a variable width long representation once you pass the value sys.maxint,
# which is either 231 - 1 or 263 - 1 depending on your platform.
# Python can handle arbitrarily large integers in computation. Any integer too big to fit in 64 bits (or whatever the underlying hardware limit is) is handled in software. For that reason, Python 3 doesn't have a sys.maxint constant.

# The value sys.maxsize, on the other hand, reports the platform's pointer size, and that limits the size of Python's data structures such as strings and lists


"""
FLOATS

The float type in Python represents the floating point number. Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts. 
For example, 97.98, 32.3+e18, -32.54e100 all are floating point numbers.

Python float values are represented as 64-bit double-precision values. 
The maximum value any floating-point number can be is approx 1.8 x 10^308. Any number greater than this will be indicated by the string inf in Python


Double-precision floating-point format (sometimes called FP64 or float64) is a computer number format, usually occupying 64 bits in computer memory; 
it represents a wide dynamic range of numeric values by using a floating radix point.


Floating point inaccuracy in python:
1.2 - 1.0 = 0.2 



0.1111111111 is more accurate than 0.111111
0.11111111111111 is more accurate than 0.1111111111
0.1111111111111111 is more accurate than 0.11111111111111

and so on
If we keep on going like this trying to get more accurate, 
we will eventually get to the point where we will eventually run out of space.

Now computer science has to compromise between accuracy and memory.
After some degree of accuracy, we might not need more accuracy.
So, computer engineers will only save upto certain degree of accuracy.
"""


"""
COMPLEX NUMBERS IN PYTHON

3+5j



# Python code to demonstrate the working of
# complex(), real() and imag()



"""

# Initializing real numbers
x = 5
y = 3

# converting x and y into complex number
z = complex(x, y)

# printing real and imaginary part of complex number
print("The real part of complex number is : ", end="")
print(z.real)

print("The imaginary part of complex number is : ", end="")
print(z.imag)

# Example :https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/


"""
BOOLEANS
True and False
print(issubclass(bool, int))

Truthy And falsy values in python


0, Empty String, list, tuples and dictionaries are considered falsy.



These represent elements from the mathematical set of integers (positive and negative).

There are two types of integers:

Integers (int)
These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2’s complement which gives the illusion of an infinite string of sign bits extending to the left.

Booleans (bool)
These represent the truth values False and True. The two objects representing the values False and True are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings "False" or "True" are returned, respectively.

The rules for integer representation are intended to give the most meaningful interpretation of shift and mask operations involving negative integers.

In Python 3.x True and False are keywords and will always be equal to 1 and 0.


So when you use set() set([True,1]) will return {True}


"""


"""
NONE in python
The None keyword is used to define a null value, or no value at all. 
None is not the same as 0, False, or an empty string. 
None is a data type of its own (NoneType) and only None can be None

"""


"""
BINARY TYPES in python
https://www.youtube.com/watch?v=ls-177DIGao
https://www.youtube.com/watch?v=Dkh0nFoEwLs
https://www.devdungeon.com/content/working-binary-data-python

What is encoding ?
an international encoding standard for use with different languages and scripts, 
by which each letter, digit, or symbol is assigned a unique numeric value 
that applies across different platforms and programs.
"""


size = bytes(10)
print(size)

message = "Hello World"
size = bytes(message, encoding="ascii")
print(size)
print(size[0])
size = bytes(message, encoding="utf-8")
print(size)
print(size[0])

my_message = "मेरो"
b = bytes(my_message, encoding="utf-8")
print(b)
print(str(b, encoding="utf-8"))
print(chr(164))
print("मे".encode("utf-8"))

import unicodedata

for i in my_message:
    print(ord(i), i, hex(ord(i)), unicodedata.name(i))

print("\x61\x62\x63")
print("\u092e")


# Unicode characters also has names

print("I am on fire")
print("I am on \U0001f525")
print("I am on \U0001F30A")
print("I really love \N{WATERMELON}")
print("\N{DEVANAGARI LETTER MA}")
print(unicodedata.name("🔥"))


"""
BYTEARRAY in python
mutable version of bytes
"""
print("=================================")
byte = bytearray()
print(byte)

# The bytearray type is a mutable sequence of integers in the range 0 <= x < 256.
my_bytes = bytearray("Hello World 🔥", encoding="utf-8")
print(my_bytes)
print(my_bytes[0])
my_bytes[0] = 255

print(my_bytes)


a = "abc"
b = a.replace("a", "f")
print(b)

a = b"abc"
b = a.replace(b"a", b"f")
print(b)

# https://docs.python.org/3/library/stdtypes.html#bytes-objects


"""
MemoryView in python

Returns memory view object of array or bytearray given in the argument
\memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying. The memoryview() function allows direct read and write access to an object’s byte-oriented data without needing to copy it first. That can yield large performance gains when operating on large objects since it doesn’t create a copy when slicing.

The Python buffer protocol, also known in the community as PEP 3118, is a framework in which Python objects can expose raw byte arrays to other Python objects. This can be extremely useful for scientific computing, where we often use packages such as NumPy to efficiently store and manipulate large arrays of data.
    
    """

view = memoryview(b"Hello World")
print(view)
print(view[0])
print(chr(view[0]))
print(view[0:5])


print("=================================")
import time

size = range(1000, 15000, 1000)


l1 = []

for n in size:
    data = b"x" * n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    stop = time.time()
    print(f"bytes:{n} {stop-start}")
    l1.append(stop - start)

l2 = []
for n in size:
    data = b"x" * n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    stop = time.time()
    print(f"bytes:{n} {stop-start}")
    l2.append(stop - start)

import matplotlib.pyplot as plt

plt.plot(l1, "x-", label="Without memoryview")
plt.plot(l2, "o-", label="With memoryview")
plt.xlabel("Size of Byte Array")
plt.ylabel("Time taken")
plt.legend()
plt.show()
