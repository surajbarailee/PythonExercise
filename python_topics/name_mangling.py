# Name Mangling is used to resolve or prevent naming conflict in derived classes
# _ and __


class Employee:
    def __init__(self):
        self.name = "Suraj Barailee"
        self._bar = 10
        self.__salary = 10000  # _Employee_salary


class Designer(Employee):
    def __init__(self):
        super().__init__()
        print(self.name)
        print(self._bar)
        # print(self.__salary)


e = Employee()
print(dir(e))

d = Designer()
print(dir(d))
