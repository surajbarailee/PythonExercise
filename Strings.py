print("Hello")
a="Hello worldy"
print(a)
b="""hello 
multiline strings
"""
print(b)
print("Strings are array")
print(a[0])
print(a[:-1])
print(a[::-1])
print(list(a))
print(len(a))
a1=" agh kajsd   "
print(a1.strip())
print(a1.upper())
print(a1.replace("a","1"))
splitting="abcd abcd abcd"
print(splitting.split(" "))

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
print(a+txt)


age = 36
sex="Male"
txt = "My name is John, I am {1}and I am {0}"
print(txt.format(age,sex))

text="banana"
x100=text.center(9,"x")
print(x100)
print(text.count("a",0,len(text)-1))
txt = "My name is Stae"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.endswith("e"))
txt = "Hello, welcome to my world."

x = txt.find("welcome",5)

print(x)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "We have {:b} chickens."
print(txt.format(49))
print(bin(49)[2:])

txt = "Hello, welcome to my world."

x = txt[::-1].index("e",)

print(x)
txt = "Company12"

x = txt.isalnum()

print(x)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
txt = "I could eat bananas all day bananas"

x = txt.partition("bananas")

print(x)

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
x = txt.rindex("casa")

print(x)

txt = "apple, banana, cherry , orange"

x = txt.rsplit(", ",2)

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))