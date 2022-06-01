my_fruit = "apple"

if my_fruit == "apple":
    print("I like apples")
else:
    print("I don't like apples")


if my_fruit == "apple":
    print("I like apples")
elif my_fruit == "banana":
    print("I like bananas")
elif my_fruit == "orange":
    print("I like oranges")


if {}:
    print("True")
else:
    print("False")

if None:
    print("True")
else:
    print("False")

if 1:
    print("This is true")
else:
    print("This is false")

if 3 + 6:
    print("This is true")
else:
    print("This is false")


if 6 - 6:
    print("This is true")
else:
    print("This is false")


def function_1():
    print("This is function 1 called")
    return 123


if function_1() == 123:
    print("Hello1")
if function_1() == 456:
    print("Hello2")
if function_1() == 789:
    print("Hello3")

# use multiple if statements when you have multiple conditions that can be true
# use elif when you have multiple conditions,but only when one condition is true at a time


"""
For Loop

for element in iterable:
    do something
    
Here iterable can be string, list, tuple, set, dictionary
"""

fruit_basket = ["apple", "banana", "orange"]

for fruit in fruit_basket:
    print(fruit)


index = 0
length_of_fruit_basket = len(fruit_basket)


while index < length_of_fruit_basket:
    print(fruit_basket[index])
    index += 1


for element in range(0, 10):
    print(element)


for element, fruit in enumerate(fruit_basket):
    print(str(fruit), " is in ", str(element))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


for element in my_list:
    print(element)

print("===============")
my_dictionary = {"name": "John", "age": 30, "city": "New York"}
for element in my_dictionary:
    print(element, ":", my_dictionary[element])

print("=======HEY========")


for value in my_dictionary.values():
    print("Value:", value)

print("======================")
for element in my_tuple:
    print(element)

for element in my_set:
    print(element)


# when to use for loops and when to use while loops??
# for loop is used when you know the number of times you want to loop
# while loop is used when you don't know the number of times you want to loop
# for loop is little easier to use than while loop due to syntax simplicity

list = [0] * 500000


import time

start = time.time()
j = 100
for i in list:
    j = i + j
end = time.time()
print("For loop", end - start)


index = 0
j = 100

start = time.time()
while index < len(list):
    j = i + j
    index += 1

end = time.time()

print("While loop", end - start)


my_sum = 0
start = time.time()
for i in range(1, 1000001):
    my_sum = my_sum + i
end = time.time()

print("For loop", end - start, my_sum)

start = time.time()
my_sum = sum(range(1000001))
end = time.time()
print("Range", end - start)


# break and continue and pass


# else with loop : else is executed when there is no breaking in the loop
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!1")


for x in range(6):
    if x == 20:
        break
    print(x)
else:
    print("Finally finished!2")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i is no longer less than 6")


i = 1
while i < 6:
    print(i)
    if i == 30:
        break
    i += 1
else:
    print("i is no longer less than 6 part 2")


# Match Case. Similar to switch case of other programming language with more batteries.
# Structural Pattern Matching
# PEP 634


# A quick Internet Example of what it looks
http_code = 500
match http_code:
    case 400:
        print( "Bad request")
    case 401:
        print( "Unauthorized")
    case 403:
        print( "Forbidden")
    case 404:
        print( "Not found")
    case _:
        print( "Unknown error")

# Example Usecase

# Example a program sometimes returns three values and sometimes only two value
# Then we can use it like this

x = ("www.google.com", 8888, "OK")

match x:
    case site, port, status:
        print("Site Port Status", site, port, status)
    case site, port:
        print("Site Port", site, port)
    case site:
        print("Site", site)
        
x, *y = [1, 2, 3, 4, 5]
print(x ,y)



def run_command(command):
    match command.split():
        case ["loading", file]:
            print(f"Loading {file}")
        case ["download", file]:
            print(f"Downloading {file}")
        case ["quit" | "exit"]:
            print(f"Peaceful Exit")
        case ["abcd" as what]:
            print(f"{what} is not a valid command")
        case ["quit" | "exit", *args] if "--force" in args:
            print("ForceFul exit")
        case ["help"]:
            print(f"Available commands: loading <file>, download <file>, quit")
        case _:
            print(f"Unknown command: {command}")
            
run_command("abcd")


# We can match objects pattern with match case as well


# https://peps.python.org/pep-0636/
# https://peps.python.org/pep-0634/