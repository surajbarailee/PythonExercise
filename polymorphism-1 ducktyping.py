#duck typing in python

x=5

x="Navin"
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VsCode:
    def execute(self):
        print ("extra stuffs")

class Laptop:
    def code(self,ide):
        ide.execute()



ide=Pycharm()
lap1=Laptop()
lap1.code(ide)
ide=VsCode()
lap1.code(ide)