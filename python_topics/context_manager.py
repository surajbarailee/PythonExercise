"""
Context Managers are used to properly work with resources like files
connection with database, network connection etc

Its basically a up level version of try catch.
We create context manager using with statement.

Most people know using with statement is preferred way to manage file than using close method.



Advantage of using context manager:
Avoid leaving any files or database connections open as thery are limited

Context Manager allows us to better manage these resources by telling an object
what to do when created or destroyed.



The use of with statement allows us to reduce code duplication


"""


from fileinput import filename


with open("hello.txt", "w+") as my_file:
    data = my_file.read()
    print(data)
    my_file.write("Hello My Universe")


"""
We can also create our own context managers.
We can use either our own class [Class based context manager] or 
use contextlib decorator [Function based context manager]
"""


# Class Based Context Managers
# we need to apply __enter__ and __exit__ methods


class File_Opener:
    def __init__(self, file_name, mode) -> None:
        self.filename = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback) -> None:
        print("Running the argument exe_type", exc_type)

        print("=========")

        print(exc_val, traceback)
        self.file.close()


with File_Opener("context.txt", "r") as file:
    file.write("contexting contexting")
print(file.closed)


# timing.py
# https://realpython.com/python-with-statement/#creating-function-based-context-managers


"""
Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited.
If the context was exited without an exception, all three arguments will be None.

If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value.

Otherwise, the exception will be processed normally upon exit from this method.


"""

from time import perf_counter


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()


from time import sleep

with Timer() as timer:
    sleep(0.5)

print(timer())


from contextlib import contextmanager


@contextmanager
def hello_function_context():
    print("Entering")
    yield "Hello World"
    print("leaving the context manager")


with hello_function_context() as hello:
    print(hello)


@context_manager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file("sample.txt") as f:
    f.write("Lorem Lorem")

print(f.closed)
