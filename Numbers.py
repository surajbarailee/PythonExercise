import random
"""
There are three numeric:
int
float
complex
"""
print("--------integers-------")
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


print("---------float--------")
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


print("---------complex---------")
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


print("----------type conversion-----")
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)

print(random.randrange(1,1000))
