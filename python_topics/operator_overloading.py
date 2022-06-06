class FirstClass:
    def __init__(self, a):
        self.a = a

    def __eq__(self, another_object: object):
        return self.a == another_object.a

    def __add__(self, another_object: object):
        return self.a + another_object.a


a = FirstClass(13)
b = FirstClass(13)
print(a == b)
print(a + b)
