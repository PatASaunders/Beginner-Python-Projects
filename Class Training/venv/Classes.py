class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("The name is "+self.name)
p1=Person("John",36)
p1.myfunc()
p1.name="David"
p1.myfunc()
del p1

mytuple=("apple","banana","cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

