class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        if self.gender == "Male":
            pronoun = "His"
        else:
            pronoun = "Her"
        return f"{pronoun} name is {self.name} and her age is {self.age}"


saurav = Person("saurav shrestha", 10, "Male")
print(saurav.name)
print(saurav.age)
saurav.details()

sangita = Person("sangita shrestha", 15, "female")
print(sangita.name)
print(sangita.age)
sangita.details()


class Student(Person):
    def __init__(self, name, age, gender, classlevel):
        super().__init__(name, age, gender)
        self.classlevel = classlevel

    def details(self):
        detail = super().details()
        return detail + f" and studies in class {self.classlevel}"


sangita = Student("sangita shrestha", 15, "female", 5)
print(sangita.name)
print(sangita.age)
print(sangita.details())


class Student(Person):
    def __init__(self, name, age, gender, classlevel):
        super().__init__(name, age, gender)
        self.classlevel = classlevel

    def details(self):
        detail = super().details()
        return detail + f" and studies in class {self.classlevel}"


class Parent(Student):
    def __init__(self, name, age, gender, classlevel, parentname):
        super().__init__(name, age, gender, classlevel)
        self.parentname = parentname


# ============================================================================


class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Male(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.gender = "Male"


class Female(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.gender = "Female"


# MRO
# method resolution order

"""

In Python, the MRO is from bottom to top and left to right. 
This means that, first, the method is searched in the class of the object. 
If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer



Old style classes use DLR or depth-first left to right algorithm whereas new style classes use C3 Linearization algorithm for method resolution while doing multiple inheritances. 

"""


"""
DLR Algorithm 
During implementing multiple inheritances, Python builds a list of classes to search as it needs to resolve which method has to be called when one is invoked by an instance. As the name suggests, the method resolution order will search the depth-first, then go left to right. For Example 


"""


class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(B, A):
    pass


# There is a problem here
# class E(C, D):
#     pass


"""
In the above Example algorithm first looks into the instance class for the invoked method. If not present, then it looks into the first parent, if that too is not present then-parent of the parent is looked into. 
This continues till the end of the depth of class and finally, till the end of inherited classes. So, the resolution order in our last example will be D, B, A, C, A. 
But, A cannot be twice present thus, the order will be D, B, A, C. But this algorithm varying in different ways and showing different behaviours at different times .
So Samuele Pedroni first discovered an inconsistency and introduce C3 Linearization algorithm. 

"""


# it prints the lookup order
print(C.__mro__)
print(C.mro())

print(D.__mro__)
print(D.mro())


# http://www.srikanthtechnologies.com/blog/python/mro.aspx
