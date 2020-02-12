#fibonacci series

'''
#through iterator
class fib:
    def __init__(self):
        self.prev=0
        self.curr=1

    def __iter__(self):                     #iterator class
        return self

    def __next__(self):
        value=self.curr
        self.curr+=self.prev
        self.prev=value
        return value

f=fib()
print(next(f))
print(next(f))
print(next(f))
print(type(f))

f=iter(fib())
print(next(f))
print(next(f))
print(next(f))
print(type(f))


#through generator                           #reduce code
def fib():
    prev,curr=0,1
    while True:
        yield curr                          #generator keyword
        prev,curr=curr,prev+curr

print(type(fib()))                          #when calling fib retuns generator
print(type(fib))                            #fib itself is a fn

print(next(fib()))                          #fn is called to return value as generator
print(next(fib()))
print(next(fib()))
print(next(fib()))

gen=fib()
print(type(gen))

print(next(gen))                             #fn is called to return value as generator
print(next(gen))
print(next(gen))
print(next(gen))

'''

#generator expression
gen=(x**2 for x in range(1,5))
print(type(gen))

print(next(gen))                            #return value without calling fn
print(next(gen))
print(next(gen))
print(next(gen))





