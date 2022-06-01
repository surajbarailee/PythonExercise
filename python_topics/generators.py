"""

Retur:. A function that returns a value is called once. The return statement returns a value and exits the function altogether.
Yield: A function that yields values, is called repeatedly. The yield statement pauses the execution of a function and returns a value. When called again, the function continues execution from the previous yield. A function that yields values is known as a generator.


# https://www.codingem.com/wp-content/uploads/2021/11/1_iBgdO1ukASeyaLtSv3Jpnw.png


A generator function returns a generator object, also known as an iterator. 
The iterator generates one value at a time. It does not store any values. This makes a generator memory-efficient.


Using the next() function demonstrates how generators work.

In reality, you don’t need to call the next() function.

Instead, you can use a for loop with the same syntax you would use on a list.

The for loop actually calls the next() function under the hood.

"""


def infinite_values(start):
    current = start
    while True:
        yield current
        current += 1


"""
When Use Yield in Python
Ask yourself, “Do I need multiple items at the same time?”.

If the answer is “No”, use a generator.



The difference between return and yield in Python is that return is used with regular functions and yield with generators.

The return statement returns a value from the function to its caller. After this, the function scope is exited and everything inside the function is gone.

The yield statement in Python turns a function into a generator.

A generator is a memory-efficient function that is called repeatedly to retrieve values one at a time.

The yield statement pauses the generator from executing and returns a single value. When the generator is called again, it continues execution from where it paused. This process continues until there are no values left.

A generator does not store any values in memory. Instead, it knows the current value and how to get the next one. This makes a generator memory-efficient to create.

The syntactical benefit of generators is that looping through a generator looks identical to looping through a list.

Using generators is good when you loop through a group of elements and do not need to store them anywhere.


    """
# https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions