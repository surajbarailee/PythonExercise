#they are unchangable
thistuple=("mango","apple","mango")
print(thistuple)
temp=list(thistuple)
temp.append("abcd")
thistuple=tuple(temp)
print(thistuple)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))