import re
text="""
abcdefghij
ABCDEFGHIJ
12345678










"""
txt="The rain in Spain Spain"
x=re.search("^The.*Spain$",txt)
if(x):
    print("yes")
print(re.findall("aI",txt))
print(re.split("a",txt,2))
xy=re.sub("a","b",txt)
print(xy+"Abcd")
print("=================================================================================================================")

abcd="baraileesuraj@gmail.COM"
x=re.sub(r"[\d\w_-]{2,15}@\w{2,5}(\.\w{2,3}){1,2}$","exapmle@gmail.com",abcd)
if(x):
    print(x)