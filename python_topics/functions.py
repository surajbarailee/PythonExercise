# functions are blocks of code that can be reused


def print_name(name):
    print("My name is " + name)


print_name("Sally")
print_name("Joe")
print_name("Mary")


def print_details(name, age):
    print("My name is " + name + " and I am " + str(age) + " years old.")


print_details("Sally", 23)
print_details("Joe", 34)
print_details("Mary", 45)


def calculate_area(length, width):
    area = length * width
    return "The area is " + str(area)  # By default, the return value is None


a = calculate_area(5, 6)
print(a)

# Argument is the value that is passed to the function
# Parameter is the variable that is used to define the function or say store the value passed to the function

print("+++++++++++++++++++++++++++++++")


def area_of_sphere(radius=10, pi=3.14):
    print("Radius and Pi are: ", radius, pi)
    area = 4 * pi * radius ** 2
    print("The area of sphere is " + str(area))


area_of_sphere(23, 12)  # This is an example of positional arguments
area_of_sphere(pi=12, radius=23)  # This is an example of keyword arguments


# We can mix positional and keyword arguments


def company_details(name, age, salary, company):
    print("Name: " + name)
    print("Age: " + str(age))
    print("Salary: " + str(salary))
    print("Company: " + company)


company_details(
    "Sally", 23, 12000, "Google"
)  # This is an example of positional arguments
company_details(
    company="Google", age=23, salary=12000, name="Sally"
)  # This is an example of keyword arguments
company_details(
    "Sally", 23, company="Google", salary=12000
)  # This is an example of mixed arguments


# Things you cant do
# company_details(23, 12000, "Google") # There is no name parameter
# company_details(company="Google", age=23, salary=12000, company="Sally") #There is duplicate parameter
# company_details("Sally", 23, 12000, "Google", "Sally") # There is more than 4 positional arguments
# company_details( salary=12000,"Sally", 23, company="Google")
# Positional arguments must be passed before keyword arguments


def company_details(name, age, salary=15000, company="cotiviti"):
    print("Name: " + name)
    print("Age: " + str(age))
    print("Salary: " + str(salary))
    print("Company: " + company)


company_details(name="Suraj", age=100)
company_details(name="Suraj", age=100, salary=12000, company="Google")


print("============MAD CALCULATION==============")


def mad_calculation(name, age):
    fullname = "His name is " + name
    age = "and he is " + str(age) + " years old"
    return fullname, age, "and he is a good"
    # When you return multiple values, tuple is returned


# abcd = mad_calculation("Suraj", 100)
# print(abcd)
# fullname, age = mad_calculation("Suraj", 100)
# fullname, age, company = mad_calculation("Suraj", 100)
# print(fullname, age)


def full_naming(first_name, last_name, middle_name=""):
    if middle_name == "":
        return first_name.title(), last_name.title()
    return first_name.title(), middle_name.title(), last_name.title()


fullname, *others = full_naming("suraj", "kumar", "bahadur")
print(fullname, *others)


fullname, *middle_name, last_name = full_naming("Tribhuwan", "Shah", "Bikram")
print(fullname, *middle_name, last_name)


def calculate_sum(*args):  # *args is a tuple
    print(*args)
    print(sum(args))


calculate_sum(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
calculate_sum(
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
)
calculate_sum(10)


def calculate_total_age(**kwargs):  # **kwargs is a dictionary
    """This function calculates the total age of all the people.
    You give the function a dictionary of people and their ages.
    """
    print(kwargs)
    print(kwargs["suraj"])
    print(sum(kwargs.values()))


calculate_total_age(suraj=23, sally=24, joe=25, mary=25)


my_function = calculate_total_age  # This is a reference to the function
my_function(suraj=23, sally=24, joe=25, mary=25)


# Recursion is a function that calls itself
# In a recursive function, the function calls itself until it reaches a base case

base_case = 100


def print_name(name):
    global base_case
    base_case = base_case - 1
    if base_case > 0:
        print(name)
        print_name(name)
    return None


print_name("Suraj")


# Write a program that prints fibonacci series
# What is a fibonacci series?
# A fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# lambda is a small anonymous function
# Example:

add = lambda x, y: "The sum is " + str(x + y)

# Doesnt have a name
# Has a single expression
# Returns a value

print(add(10, 20))


# Example of map function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x: x * 2, numbers))
print(result)

# Example of filter function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)






# You can seperate arguments and keyword arguments with an asterisk


def seperator(first, second, third, * , fourth, fifth):
    print(first, second, third, fourth, fifth)
    
seperator(1, 2, 3, fourth = 4, fifth=5) # This is allowed
# seperator(1,2,3,4,5) # This is not allowed
