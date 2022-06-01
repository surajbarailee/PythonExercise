"""

Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method. 
An iterator is an object, which is used to iterate over an iterable object using the __next__() method. Iterators have the __next__() method, which returns the next item of the object. Note that every iterator is also an iterable, but not every iterable is an iterator. For example, a list is iterable but a list is not an iterator. An iterator can be created from an iterable by using the function iter(). 
To make this possible, the class of an object needs either a method __iter__, which returns an iterator, or a __getitem__ method with sequential indexes starting with 0. 

Iterable = Gives iterator __iter__ and __get_item__
Iterable = Has Next Method that can fetch the next next next value


In Python an iterable is anything that you can iterate over and an iterator is the thing that does the actual iterating.

Iter-ables are able to be iterated over. Iter-ators are the agents that perform the iteration.
"""


# I often say that iterators are lazy single-use iterables. They’re “lazy” because they have the ability to only compute items as you loop over them. And they’re “single-use” because once you’ve “consumed” an item from an iterator, it’s gone forever. The term “exhausted” is often used for an iterator that has been fully consumed.
# The range object is “lazy” in a sense because it doesn’t generate every number that it “contains” when we create it. Instead it gives those numbers to us as we need them when looping over it.


# https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
# List is an iterable but not an iterators
# List is iterable because you can loop over .LUL
nums = [1, 2, 3]

for num in nums:
    print(num)


# For something to be an iterable
# It should have __iter__

# print(dir(nums))  # it will have __iter__


# Iterator is an object that has a state
# So that it remembers where it is during iterations
# We get the next value from __next__ method

nums = [1, 2, 3]
# print(nums.__iter__())  # or we can do iter(nums)
i_nums = iter(nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums))  # Will raise stop iterations error


# So why do we need it?
# We can create something to work like iterators


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_numbers = MyRange(1, 7)

# for num in my_numbers:
#     print(num)
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))


# Generators are iterators as well with iterators being predefined
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


for num in nums:
    print(num)
