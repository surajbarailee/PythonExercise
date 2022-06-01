# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable (if conditional)]


my_list = []
for i in range(11):
    if i % 2 == 0:
        my_list.append(i ** 2)

print(my_list)


my_list1 = [i ** 2 for i in range(11) if i % 2 == 0]
print(my_list1)


my_list2 = []
for i in range(5):
    for j in range(i):
        my_list2.append((i, j))
print(my_list2)

my_list3 = [(i, j) for i in range(5) for j in range(i)]
print(my_list3)


my_list5 = []
for i in range(20):
    if i % 5 == 0:
        for j in range(i):
            if j % 5 == 0:
                my_list5.append((i, j))


print(my_list5)

my_list6 = [(i, j) for i in range(20) if i % 5 == 0 for j in range(i) if j % 5 == 0]
print(my_list6)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]


# Comparision of list vs for loop to create lists

import time

iterations = 1000000
start = time.time()
mylist = []
for i in range(iterations):
    mylist.append(i)
end = time.time()
print(end - start)


start = time.time()
mylist = [i for i in range(iterations)]
end = time.time()
print(end - start)


# creating list with comprehension are little faster
# But, this is because we are creating a list by appending new elements to it at each iteration.

start = time.time()
mylist = list(range(iterations))
end = time.time()
print(end - start)
# Range and list are more faster to create arrays


# But for computations. This might vary,Sometimes loops are faster and sometimes slower
start = time.time()
for i in range(iterations):
    i + 1
end = time.time()
print(end - start)

start = time.time()
[i + 1 for i in range(iterations)]
end = time.time()
print(end - start)

a = [(x, x + 1) for x in range(20)]
print(a)


# Set Comprehension

a = {(x, x + 1) for x in range(20)}
print(a)

# Dictionary
a = {x: "Number" + str(x) for x in range(20)}
print(a)


# We dont have tuple comprehension
# This will be a generator
a = (x for x in (range(10)))
print(type(a))
print(list(a))
