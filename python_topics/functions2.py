# Scoping LEGB rule
# Shadowing
# Decorators
# First Class Citizens
# Closures
# Higher Order Functions
# Functions that operate on other functions, either by taking them as arguments or by returning them, are called higher-order functions.

# First class function
# A programming language is said to have first-class functions if it treats functions as first-class citizens
# First Class Citizen:
# A first class citizen in a programming language is an entity which supports all the operations generally
# availae to other entities. These operations typically include being passed as an argument
# returned from a function and assigned to a variable
# MEANING : we should be able to treat function just like any other object or variable


def square(x):
    return x * x


# First class function as function can be assigned to a variable
f = square

print(square)
print(f(20))


# Passing a function as an argument


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


my_list = [1, 2, 3, 4, 5]

my_new_list = my_map(square, my_list)
print(list(my_new_list))


def logger(msg):
    def log_message():
        print("Logging:", msg)

    return log_message


hi = logger("Hi")
hi()


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")
print_h1("h1 Headline")
print_h1("h1 Headline2")


# CLOSURES
# A closure is an inner function that remembers and has access to variables in the local scope in which it was created.


def outer_func():
    message = "My message"

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()
print(my_func.__name__)

my_func()
my_func()
my_func()


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func()
hello_func()


import logging

logging.basicConfig(filename="example.log", level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info("Running {} with arguments {}".format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)


add_logger(3, 3)
add_logger(4, 5)


sub_logger(10, 5)
sub_logger(20, 10)
