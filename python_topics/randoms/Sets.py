#not duplicate unordered and unindexed


thisset={"apple","mango","mango","apple"}
print(thisset)
#cannot change but add
thisset.add("another apple")
thisset.update(["another mango","another kela"])
print(thisset)
abcd="aabbccddssdfsdfsddddfsdfsdfsdf"
abcd=set(abcd)
print(abcd)