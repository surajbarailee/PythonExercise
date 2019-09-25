class name:
    def __init__(self,var1,var2):
        print("in init")
        self.var1=var1
        self.var2=var2
    def config(self):
        print("check check",self.var1,self.var2)
x=name("abcd1","abcd2")
name.config(x)
x.config()

print("---------------------------------------------")



#types of variable


class Car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()
c1.mil=8
print(c1.com,c1.mil,Car.wheels)
Car.wheels=10
print(c2.com,c2.mil,Car.wheels)