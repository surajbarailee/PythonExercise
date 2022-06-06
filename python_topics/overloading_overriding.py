"""
In method overloading, methods must have the same name and different signatures.
In method overriding, methods must have the same name and same signature.

"""


class ABCD:
    def abcd_class_function1(self):
        print("abcd_class_function1")

    def abcd_class_function2(self):
        print("abcd_class_function2")


class EFGH(ABCD):
    def abcd_class_function1(self):
        print("abcd_class_function1 inside EFGH")

    def abcd_class_function2(self):
        print("abcd_class_function2 inside EFGH")


a = EFGH()
a.abcd_class_function1()
a.abcd_class_function2()


class E:
    def abcd_class_function1(self):
        print("abcd_class_function1 inside E")

    def abcd_class_function1(self, value):
        print(f"abcd_class_function2 inside E second one {value}")

    def abcd_class_function1(self, value, value1):
        print(f"abcd_class_function2 inside E second one {value1} {value}")


e = E()
e.abcd_class_function1(123, 123)
print(E.__dict__)  # this will only show abcd_class_function1


"""
When we define multiple functions with the same name, the later one always overrides the prior and thus, in the namespace, 
there will always be a single entry against each function name


"""
