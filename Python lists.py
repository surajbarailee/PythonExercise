"""
List is ordered changable and allows duplicate members
Tuples is ordered and unchangable allows duplicates
Set is unordered and unindexed ,no duplicate
dictionary is unordered changable and indexed no duplicates
"""
"""
List are square brackets


"""
thislist = ["abcd", "xyz", "next", "ablke", "ashd", "asd"]
print(thislist)
print thislist[0]
print thislist[-1]
print(thislist[1:])
for i in thislist:
    print i

if "abcd" in thislist:
    print("yes")
thislist.append("added")
thislist.insert(0, "0 place")
print(thislist)
thislist.remove("0 place")
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
thislistcopy=list(thislist)
print(thislistcopy)
x=thislist.index("next")
print(x)
thislist.reverse()
print(thislist)
