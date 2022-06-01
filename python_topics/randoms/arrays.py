"""
All the values of same type
they dont have fixed values

"""
from array import *
vals=array('i',[1,2,3,4,5])
print(vals)
newvals=array(vals.typecode,(a for a in vals))
print(newvals)
vals.append(6)
print(vals)
print(vals.buffer_info())
vals.reverse()
print(vals)
vals.remove(5)
print(vals)
vals.pop()
print(vals)
vals.append(10)
print(vals)
for i in vals:
    print i