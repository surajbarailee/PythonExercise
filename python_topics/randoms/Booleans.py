print(bool("hello"))
print(bool(15))
print(bool("false"))
a=[]
b=''
c=0
print(bool(a))
print(bool(b))
print(bool(c))
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


x=200
print(isinstance(x,str))