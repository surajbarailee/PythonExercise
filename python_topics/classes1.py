# Classes are like blue prints.you use them to create real data
# Objects are the instance of Classes


class classname:
    pass


class1 = classname()
print(class1)

class1.name = "Class One"
class1.no_of_student = 56
print(class1.__dict__)
print(dir(class1))


class MyClass:
    def __init__(self, classname, no_of_student):
        self.classname = classname
        self.no_of_student = no_of_student


class1 = MyClass("Class One", 56)

print(class1.classname)

class1.classname = "Class 2"
print(class1.classname)


# self is just a name and can be anything
class MyClass1:
    def __init__(this, classname, no_of_student):
        this.classname = classname
        this.no_of_student = no_of_student


class1 = MyClass1("abcd", 80)
print(class1.classname)
print(class1.no_of_student)


class MyClass:
    total_class = 10

    def __init__(self, classname, no_of_student):
        self.classname = classname
        self.no_of_student = no_of_student

    def details(self):
        print(
            f"The class name is {self.classname} and total student is {self.no_of_student}"
        )

    def total_fees_collection(self, total_student):
        fee_per_student = 100
        return fee_per_student * total_student


class_one = MyClass("Class One", 20)
print(dir(class_one))
class_one.details()
print(class_one.total_fees_collection(class_one.no_of_student))

class_two = MyClass("Class two", 30)
print(class_two.total_fees_collection(class_two.no_of_student))


"""
1.It eliminates the use of self argument.

2.It reduces memory usage because Python doesn't have to instantiate a bound-method for each object instiantiated:

3.It improves code readability, signifying that the method does not depend on state of the object itself.

4.It allows for method overriding in that if the method were defined at the module-level (i.e. outside the class) a subclass would not be able to override that method.
"""


"""
class methods are methods that are bound to classes rather than objects instance


"""


# class Person:
#     age = 25

#     def print_age(cls):
#         print("The age is:", cls.age)


# # create printAge class method
# Person.print_age = classmethod(Person.print_age)

# Person.print_age()
# person1 = Person


class Person:
    age = 25

    @classmethod
    def print_age(cls):
        cls.age = 100
        print("The cls age is:", cls.age)

    def print_age1(self):
        print("The self age is ", self.age)

    def change_age(self):
        self.age = 100


# create printAge class method
person1 = Person()
person1.change_age()
person1.print_age()
person1.print_age1()
print(Person.age)
