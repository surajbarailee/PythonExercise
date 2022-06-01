# Typecasting is conversion of data types
# Implicit Typecasting  = Done by interpreter itself
# Eg:

# int to float
x = 20
x = x / 2
print(x)

# Explicit Typecasting/ Type Conversion = Done by you manually

x = "10"
x = int(x)
print(x)

# When doing explicit typecasting or conversion directly we generally get loss of data
x = {"a":1,"b":2}
x = list(x)
print(x)

x = 10.123
print(int(x))
