gv=1000
def function1():
    x=300
    global gv
    gv1=gv
    print(gv1)
    gv=5000
    print(x)
    def innerfunction1():
        print(x+100+gv1)
    innerfunction1()
function1()
print(gv)