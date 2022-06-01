# # Syntax Errors and Exceptions
# # Syntax Error occurs when the parser of python detects an syntatically incorrect statement.
# # So it is also known as parsing error
# # for Eg
# # x =234 x=32 # Raise the syntax error

# # Even if a statement or expression is syntactically correct,
# it may cause an error when an attempt is made to execute it.
# # some Example are:
# # DivisionByZero Error : Dividing by Zero
# # NameError : Variables Not defined


def classtree(cls, indent=0):
    print("." * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)


# classtree(BaseException)

# from decimal import DivisionByZero


# try:
#     # You put error prone code here
#     print("I am trying to do something")
#     # 10 / 0
#     print("After disaster code")
# except:
#     # What to do when your code is faulty
#     print("Oops something bad happened")
# else:
#     # What if your code is not faulty
#     print("Hey I am inside else")
# finally:
#     # You got to execute this anyways
#     print("Oh my God Finally")


# # First, the try clause (the statement(s) between the try and except keywords) is executed.

# # If no exception occurs, the except clause is skipped and execution of the try statement is finished.

# # If an exception occurs during execution of the try clause, the rest of the clause is skipped.
# # Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

# # If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements;
# # if no handler is found, it is an unhandled exception .

# while True:
#     try:
#         10 / 0
#     except ZeroDivisionError as e:
#         print("Why are you dividing by zero ? you idiot", dir(e))
#         print("Why are you dividing by zero ? you idiot", e)
#         print(e.__traceback__)
#         print(e.with_traceback(e.__traceback__))
#         break
#     except TypeError as e:
#         print(e)


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Oops!  That was no valid number.  Try again...")
#     except:
#         pass


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Oops!  That was no valid number.  Try again...")
#     except Exception as e:
#         print(e)

# Whats the difference between except Exception: and except:
# There is a main parent called BaseException = It handles almost everything that you can think of Including system errors and KeyboardInterrupt etc
# And there is Exception class that is derived from the BaseException that kinds of leaves those system errors and KeyboardInterrupt errors

# Exceptions derived from BaseException are: GeneratorExit, KeyboardInterrupt, SystemExit.

# According to the documentation:

# GeneratorExit: Raised when a generator‘s close() method is called. It directly inherits from BaseException instead of StandardError since it is technically not an error.
# KeyboardInterrupt: Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. Interrupts typed when a built-in function input() or raw_input() is waiting for input also raise this exception. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.
# SystemExit: The exception inherits from BaseException instead of StandardError or Exception so that it is not accidentally caught by code that catches Exception. This allows the exception to properly propagate up and cause the interpreter to exit.


# while True:
#     try:
#         x = input("Hello\n")
#         int(x)
#     except:
#         print("Oops Exception ")

# while True:
#     try:
#         x = input("Hello\n")
#         int(x)
#     except Exception:
#         print("Oops Exception ")


# You can only catch SyntaxError if it's thrown out of an eval, exec, or import operation.
# Indentation Error is a subclass of syntax error
# try:
#     import check
# except IndentationError:
#     print("OOPS")


class VeryBigNumber(Exception):
    pass


class VerySmallNumber(Exception):
    def __init__(self, message):
        self.message = message

    def abcd(self):
        print("ABCD ABCD")


# while True:
#     try:
#         my_input = int(input("Give me a number\n"))
#         if my_input > 10000:
#             raise VeryBigNumber("The number is too big", my_input)
#         elif my_input < 10:
#             raise VerySmallNumber("This number is too small")
#         if my_input == 100:
#             break
#     except VeryBigNumber as big:
#         # print(big.args)
#         print(big)  # You can override this with __str__
#         # print(big.with_traceback)
#         raise ValueError
#     except VerySmallNumber as small:
#         small.abcd()
#     except ValueError as ve:
#         print("Value Error occured")


# This ValueError is not raised ??
# Because:
# Using raise in the except clause won't search for exception handlers in the same try block (it did not occur in that try block).
# It will search for handlers one level up , that is, an outer try block. If that isn't found it'll interrupt execution as it normally does (resulting in the exception being displayed).

# while True:
#     try:
#         try:
#             my_input = int(input("Give me a number\n"))
#             if my_input > 10000:
#                 raise VeryBigNumber("The number is too big", my_input)
#             elif my_input < 10:
#                 raise VerySmallNumber("This number is too small")
#             if my_input == 100:
#                 break
#         except Exception as e:
#             # print(e.__traceback__)
#             # import traceback

#             # `e` is an exception object that you get from somewhere
#             # traceback_str = "".join(traceback.format_tb(e.__traceback__))
#             # print(traceback_str)
#             raise ValueError("Value Error occured")
#             # raise ValueError("Value Error occured").with_traceback(e.__traceback__)

#     except ValueError as e:

#         import traceback

#         # `e` is an exception object that you get from somewhere
#         traceback_str = "".join(traceback.format_tb(e.__traceback__))
#         print(traceback_str)
#         # print(e)


# The from clause is used for exception chaining: if given,
# the second expression must be another exception class or instance, which will then be attached to the raised exception as the __cause__ attribute (which is writable).
# If the raised exception is not handled, both exceptions will be printed:

# Implicit Exception Chaining

Here is an example to illustrate the __context__ attribute:

def compute(a, b):
    try:
        a/b
    except Exception as  exc:
        log(exc)

def log(exc):
    file = open('logfile.txt')  # oops, forgot the 'w'
    print >>file, exc
    file.close()
# Calling compute(0, 0) causes a ZeroDivisionError. The compute() function catches this exception and calls log(exc), but the log() function also raises an exception when it tries to write to a file that wasn’t opened for writing.

# In today’s Python, the caller of compute() gets thrown an IOError. The ZeroDivisionError is lost. With the proposed change, the instance of IOError has an additional __context__ attribute that retains the ZeroDivisionError.





# Explicit Exception Chaining


# The from clause is used for exception chaining: if given, the second expression must be another exception class or instance.
# If the second expression is an exception instance, it will be attached to the raised exception as the __cause__ attribute (which is writable).
# If the expression is an exception class, the class will be instantiated and the resulting exception instance will be attached to the raised exception as the __cause__ attribute.
# If the raised exception is not handled, both exceptions will be printed:

try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc


# raise EXCEPTION from CAUSE

# Explicit Exception Chaining
# The __cause__ attribute on exception objects is always initialized to None.
# It is set by a new form of the raise statement:

# raise EXCEPTION from CAUSE
# which is equivalent to:

# exc = EXCEPTION
# exc.__cause__ = CAUSE
# raise exc


# https://blog.ram.rachum.com/post/621791438475296768/improving-python-exception-chaining-with

# PEP 3134

# The __cause__ attribute on exception objects is always initialized to None. It is set by a new form of the raise statement:

# raise EXCEPTION from CAUSE
# which is equivalent to:

# exc = EXCEPTION
# exc.__cause__ = CAUSE
# raise exc

# This PEP proposes three standard attributes on exception instances: the __context__ attribute for implicitly chained exceptions, 
# the __cause__ attribute for explicitly chained exceptions, and the __traceback__ attribute for the traceback. A new raise ... from statement sets the __cause__ attribute.