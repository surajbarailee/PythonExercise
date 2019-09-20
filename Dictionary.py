#Key value set unordered changable and indexed
thisdict={}
print(bool(thisdict))
thisdict={
    "abcd":"zxy",
    "1":123,
    "2":123456,
    "3":12345678945
}
print(thisdict["abcd"])
for x in thisdict.values():
    print x
for x,y in thisdict.items():
    print(x,y)
if "1" in thisdict.items():
    print("yes")
else:
    print("No")
thisdict.pop("2")
thisdict.popitem()
print(thisdict)
for x,y in thisdict.items():
    if y==123:
        del thisdict[x]
print(thisdict)