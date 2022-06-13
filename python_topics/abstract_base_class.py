from abc import ABC, abstractmethod

# Imagine you dont want others to initialize Human Class directly
class Human(ABC):
    @abstractmethod
    def nameprinter(self):
        pass

    @abstractmethod
    def ageprinter(self):
        pass


class Employee(Human):
    pass
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def name(self):
    #     print(f"Name is {self.name}")

    # def age(self):
    #     print(f"Age is {self.age}")


class Employee1(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def nameprinter(self):
        print(f"Name is {self.name}")

    def ageprinter(self):
        print(f"Age is {self.age}")


a = Employee1("Suraj", 100)
a.nameprinter()
a.ageprinter()
