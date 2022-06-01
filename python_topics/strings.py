"""
Strings in python

"""
string = "Hello*World!"


"""
H    e    l   l   o   *   W   o   r   l   d   !
0    1    2   3   4   5   6   7   8   9   10  11
-12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

"""
print(string[2:]) # get every element from second index
print(string[-2:]) # get every element from -2
print(string[2:6]) #get every element from second element to sixth (sixth exclusive)
print(string[2:-6])
print(string[::2])
print(string[::-1])
print(string[::-2])
print(string[::-3])
print(string[6:1:-2]) # get every second element from 6 to 1 in reversed
print("=====")
print(string[3::-3]) # get evey third element starting from 3 in reversed
print(string[11:11])

print(len(string))

print(string.upper())
print(string.lower())


print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print(string.swapcase())
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.replace("World", "Universe"))
