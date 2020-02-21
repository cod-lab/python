#iterable - like operand
#iterator - like operator
#iteration - like operator working on operand, like fn of operator
'''

x=[1,2,3]
x_iter=iter(x)
print(x_iter)

print(next(x_iter))
print(next(x_iter))                     #on every new/next 'next' it return next element of the list
print(next(x_iter))
#print(next(x_iter))                     #after end of elemnts print err


#iteration using classes
#creating our own range fn using 1 class only - makes the class both iterable and iterator
class yrange:                                   #both iterable and iterator
    def __init__(self,n):
        self.i=0                                #iterator, i is the initial point (which is mostly 0) of the range
        self.n=n                                #n is the final point upto which the range should be

    def __iter__(self):                         #makes class iterable
        return self 
        
    def __next__(self):                         #implemented by iterator, iterates the class
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration

for x in yrange(10):
    print(x)

y=yrange(5)                                 #object of class yrange created, now y holds list just like x logically

print(list(z))                              #print list
print(list(z))                              #print nothing second time bcs iterator and iterable are same class so it consume only once

y_iter=iter(y)
print(y_iter)                               #print main & class name bcs both iterable and iterator are same (which is class)
print(next(y_iter))
print(next(y_iter))
print(next(y_iter))

'''

#creating our own range fn using multiple classes - makes different class for iterable and iterator
class zrange:                                       #iterable class
    def __init__(self,n):
        self.n=n

    def __iter__(self):                           #makes class iterable
        return zrange_iter(self.n)                #returning a new class

class zrange_iter():                                #iterator class
    def __init__(self,n):                           #will hold
        self.i=0                                    #iterating value
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()

for x in zrange(5):
    print(x**2)

z=zrange(5)
print(list(z))                          
print(list(z))                               #can consume and print second time bcs iterator and iterable classes are different here



        
        



























        
