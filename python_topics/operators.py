# += operator
"""Arithmetic Operator
""" ""

a = 10
b = 20
# Addition
c = a + b
print(c)
# Subtraction
c = a - b
print(c)

# Multiplication
c = a * b
print(c)

# Division
c = a / b
print(c)

# Modulus
c = a % b
print(c)

# Power
c = a ** b
print(c)

# Floor Division
c = a // b
print(c)


"""Assignment Operator
"""

# Show all the examples of assignment operators


a += b
print(a)

a -= b
print(a)

a *= b
print(a)

a /= b
print(a)

a %= b
print(a)

a **= b
print(a)

a //= b
print(a)

a = 100
b = 20
a &= b
print(a)

a |= b
print(a)

a ^= b
print(a)

a >>= b
print(a)

a <<= b
print(a)


# Comparison Operators

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Logical Operators

print(a and b)
print(a or b)
print(not a)

# Identity Operators

print(a is b)
print(a is not b)


# Membership Operators

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(1 in (1, 2, 3))
print(1 not in (1, 2, 3))
print("a" in "abc")
print("a" not in "abc")
print("a" in {1: "a", 2: "b", 3: "c"})
print("a" not in {1: "a", 2: "b", 3: "c"})
print(1 in {"a": 1, "b": 2, "c": 3})
print(1 not in {"a": 1, "b": 2, "c": 3})


# Bitwise Operators
# Computer programming tasks that require bit manipulation include low-level device control,
# error detection and correction algorithms, data compression, encryption algorithms, and optimization.
# Can be used as flags to indicate the state of a device or to indicate the type of data.


# Bitwise AND
print(a & b)
# Bitwise OR
print(a | b)
# Bitwise XOR
print(a ^ b)
# Bitwise Left Shift
print(a << b)
# Bitwise Right Shift
print(a >> b)
# Bitwise NOT
print(~a)


# An Example of AND operator
# a	b	a & b
# 0	0	0
# 0	1	0
# 1	0	0
# 1	1	1

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

c = a & b
# 12 = 0000 1100
print("Value of AND c is ", c)


# ==================================================================================


# An example of bitwise OR operator

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

c = a | b
# 61 = 0011 1101
print("Value of OR c is ", c)


# An example of bitwise XOR operator
# XOR = a logical operator which results true when either of the operands are true

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101


# Table of Exclusive OR
# a    b    a^b
# 0    0    0
# 0    1    1
# 1    0    1
# 1    1    0

c = a ^ b
# 49 = 0011 0001
print("Value of XOR c is ", c)


# An Example of bitwise NOT operator


#  Not operator is used to reverse the bits of the number.
# If the number is in binary form, then the result is obtained by reversing the bits of the number.
# If the number is in decimal form, then the result is obtained by subtracting the number from 2 raised to the power of the number of bits.
# The result is obtained by adding 1 to the result of the subtraction.
# For example:
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = ~a
# -61 = 1100 0011


# Bitwise right shift:
# Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result.
# Similar effect as of dividing the number with some power of two.

# Example 1:
a = 10  # = 0000 1010 (Binary)
a >> 1  # = 0000 0101 = 5

# Example 2:
a = -10  # = 1111 0110 (Binary)
a >> 1  # = 1111 1011 = -5


# Bitwise left shift:
# Shifts the bits of the number to the left and fills 0 on voids right as a result.
# Similar effect as of multiplying the number with some power of two.
# Example:

# Example 1:
a = 5  # = 0000 0101 (Binary)
a << 1  # = 0000 1010 = 10
a << 2  # = 0001 0100 = 20

# Example 2:
b = -10  # = 1111 0110 (Binary)
b << 1  # = 1110 1100 = -20
b << 2  # = 1101 1000 = -40


# Now coming to an idiot situation with a python += operator


my_film = (
    ["The Elephant Princess", "Hanna Montana", "Vicky Aur Veetal"],
    ["Naruto", "Bleach", "One Piece"],
    ["The Hobbit", "The Lord of the Rings", "The Silmarillion"],
)

print(my_film)
print(my_film[0])

# my_film[0] += ["Ben 10"]
# This will raise an error but the value will still be changed. What a mess python is.
# This is a feature and not a bug in python


try:
    my_film[0] += ["Ben 10"]
except TypeError:
    print(my_film)


# Explanation
# my_film[0] += ["Ben 10"]
# the above actually is:
# my_film[0] = my_film[0] + ["Ben 10"]
# How above works is: first it calculates the leftside and then assigns it to the right side.
# The right hand side is perfectly valid and runs.
# You take a list and add an element to it ,making the list ["The Elephant Princess", "Hanna Montana", "Vicky Aur Veetal","Ben 10"]
# The problem here is that the left hand side is a tuple and it is immutable.


# But hold on a sec:


x = 100
print(id(x))
x += 1
print(id(x))  # This is changed

x = []

print(id(x))
x += [1]
print(id(x))

# print(id(x)) Not changed Why ? LOL
# Saving Spaces as your list can be very long and copying over and over will make python slower

# https://www.youtube.com/watch?v=cGveIvwwSq4


x = 5
y = 10
z = 15

if x < y < z:  # This is equivalent to x < y  and y < z
    print("True")
else:
    print("false")

if (
    x < y == z <= x > 1 + 5 == 20 != 15 == 18 > x
):  # This is equivalent to x<y and y == z and z<=x and so on
    print("True")
else:
    print("false")


# Unary Operators:
x = -20
print(x)
y = +10
print(y)


# Operator Precedence
# https://docs.python.org/3/reference/expressions.html#operator-precedence
# PEMDAS


# Associativity of Python operators
# Associativity is the order in which an expression is evaluated
# that has multiple operators of the same precedence.
#  Almost all the operators have left-to-right associativity.


# Left-right associativity
# Output: 3
print(5 * 2 // 3)

# Output 0
print(5 * (2 // 3))

# Output 3
print((5 * 2) // 3)


# But exponential are little different it has right to left associativity

print(5 ** 2 ** 3)
print((5 ** 2) ** 3)
print(5 ** (2 ** 3))


# Also comparision operators are different

x = 0
y = 30
z = 40


print(x < y < z)  # This is equal to x < y and y < z
print((x < y) < z)  # x < y returns True and True (1) is less than 40. So overall true
print(x == (y > z))  # y > z is False and False is equal to 0
# And since True and False have values as integers you get the answers you do out of the parenthesized versions.


x = 20
y = [200]

x ,= y
# What the hell is this ?
print(x)


x ,= [100]
print(x)



# Walrus operator

# res = re.match(...)
# if res:
#     print(res.group(0))
    
# if (res:= re.match(...)):
#     print(res.group(0))

# x = 20 doesnt return anything
# (x := 20) returns something