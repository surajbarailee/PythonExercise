class A(object):
    def __init__(self):
        print("init of a")
    def feature1(self):
        print("Feature 1 working of A")

    def feature2(self):
        print("Feature 2 working of A")


class B(A):
    def __init__(self):
        super(A,self).__init__()
        print("init of b")
    def feature3(self):
        print("Feature 3 working of B")

    def feature4(self):
        print("Feature 4 working of B")

class C(B):
    def feature5(self):
        print("Feature 5 working of C")
a1=A()
a1.feature1()
a2=B()
a2.feature2()
a3=C()
a3.feature1()


print("------------------------------------------------")


class A1(object):
    def __init__(self):
        print("init of a")
    def feature1(self):
        print("Feature 1 working of A")

    def feature2(self):
        print("Feature 2 working of A")


class B1:
    def __init__(self):
        super(A1,self).__init__()
        print("init of b")
    def feature3(self):
        print("Feature 3 working of B")

    def feature4(self):
        print("Feature 4 working of B")

class C1(A1,B1):
    def __init__(self):
        print("in init c")
    def feature5(self):
        print("Feature 5 working of C")

a3=C1()
a3.feature1()
