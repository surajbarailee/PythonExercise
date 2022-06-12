# Logically Speaking python has no private or public variable concepts
# But getters and setters are used to insert validation while doing getters and setters things.


# Property() function
# Property sets three methods:
# get set and delete


class Employee:
    def __init__(self):
        self._name = "Suraj"

    def get_name(self):
        print("get_name called")
        return self._name

    def set_name(self, new_name):
        print("set_name called")
        self._name = new_name

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)


suraj = Employee()
suraj.name = "Suraj Barailee"
print(suraj.name)


# Python program to explain property()
# function using decorator


class Employee:
    def __init__(self, name):
        self._name = name

    # getting the names
    @property
    def name(self):
        print("Getting name")
        return self._name

    # setting the names
    @name.setter
    def name(self, name):
        print("Setting name to " + name)
        self._name = name

    # deleting the names
    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name


# passing the name
x = Employee("Suraj Barailee")
print(x.name)

x.name = "Sakar Shrestha"

del x.name
