# DECORATORS
# A function that takes another function as an argument and returns a function


def decorator(original_func):
    def wrapper():
        print("Something is happening before the original function is called.")
        return original_func()

    return wrapper


def display():
    print("Display function ran")


decorated_display = decorator(display)
decorated_display()


@decorator
def display1():
    print("Display function ran")


display1()


def decorator(original_func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the original function is called.")
        return original_func(*args, **kwargs)

    return wrapper


# Decorator with arguments


def display_info(name, age):
    print("Display info ran with arguments {} {}".format(name, age))


@decorator
def display_info1(name, age):
    print("Display info ran with arguments {} {}".format(name, age))


displaying = decorator(display_info)

displaying("John", 23)
display_info1("Johnny Johnny", 23)


# Practical Use Case of Decorators


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
def display_info(name, age):
    print("Display info ran with arguments {} {}".format(name, age))


display_info("Suraj", 23)

import time


@my_timer
def display_info1(name, age):
    time.sleep(1)
    print("Display info ran with arguments {} {}".format(name, age))


display_info1("Suraj", 23)


# @wraps functool decorator





def logger(function):
    import time
    
    def runner():
        print("Things that you have to run beforehand")
        data = function()
        
        return data
    return runner


def my_function():
    print("My function")
    
abcd = logger(my_function)
abcd()


@logger
def mero_function():
    print("Meor function")
    
mero_function()
