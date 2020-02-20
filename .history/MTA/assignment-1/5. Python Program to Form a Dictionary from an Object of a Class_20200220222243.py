class A():
    def fn1(self,a,b):
        x=a+b
        print(a+b)
        
obj1=A()
obj1.fn1(5,4)
print(obj1.__dict__)