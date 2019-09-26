#Method overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a,b,c=None):
        s=a+b
        return s

s1=Student(58,69)

print(s1.sum(5,9))


#Method overriding
class A:
    def show(self):
        print("in a show")

class B(A):
    def show(self):
        print("in b show")
    pass


a1=B()
a1.show()