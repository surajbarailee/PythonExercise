import itertools

counter = itertools.count()
# starts at 0 and goes on
print(next(counter))


# Infinite Loop
# for i in counter:
#     print(i)


data = [100, 200, 300, 400]

my_Data = list(zip(range(10), data))
print(my_Data)

# zip_longest
my_Data = list(itertools.zip_longest(range(10), data))
print(my_Data)


counter = itertools.cycle(["On", "Off"])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.repeat(2)
counter = itertools.repeat(2, times=3)

squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(squares))


letters = ["a", "b", "c", "d"]

for i in itertools.combinations(letters, 3):
    print(i)


for i in itertools.permutations(letters, 3):
    print(i)

numbers = [1, 2, 3, 4, 5]

for i in itertools.product(numbers, repeat=4):
    print(i)


for i in itertools.chain(letters, numbers):
    print(i)

for i in itertools.islice(range(10), 5):
    print(i)
