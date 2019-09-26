nums=[7,8,9,5]
for x in nums:
    print x

it=iter(nums)
print(it)
print(next(it))


print("--------------------")

class Topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def next(self):
        if self.num<=10:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration
values=Topten()
print(next(values))
for i in values:
    print(i)