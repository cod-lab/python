#everything in python is object
#there is nothing like primitive in python
#even fn is also an object

'''

# return stmt

def add(a,b):
    x=a+b
    print(x)
add(2,3)

def add(a,b):
    print(a+b)
x=add(5,6)                  #fn called and ran but result not stored in x
print(x)                    #print 'none'

def add(a,b):
    return(a+b)             #return and store result
x=add(5,6)                  #fn called and ran and result stored in x
print(x)                    #print a+b

def div(a,b):
    try:
        print(a/b)
    except:
        print('err')
        
div(12,4)                   #print try block
div(12,0)                   #print except block


def div(a,b):
    try:
        print(a/b)
    except:
        print('err')
    finally:
        print('dn')
        
div(12,4)                   #print try block & finally block
div(12,0)                   #print except block & finally block

def div(a,b):
    try:
        return a/b          #print nothing
    except:
        print('err')
    finally:
        print('dn')
        
div(12,4)                   #run try block & finally block
div(12,0)                   #run except block & finally block

def div(a,b):
    try:
        return a/b          #print nothing
    except:
        print('err')
    finally:
        print('dn')
        return (20)
        
div(12,4)                   #run finally block only
div(12,0)                   #run finally block only

# scope of variable

n=3                         #global var
def func1():
    print(n)
func1()                     #print global var

n=3                         #global var
def func1():
    n=8                     #local var
    print(n)
func1()                     #print local var

n=3                         #global var
def func1():
    n+=8                    #local var
    print(n)
func1()                     #print err

n=3                         #global var
def func1():
    global n                #declaring to use global var(prgm searches x in global area)
    print(n)                #print global var
    n+=1                    #changes value of global var
    print(n)                #print new global var 
func1()

n=3                         #global var
def func1():
    n=8                     #local var
    n+=1
    print(n)
func1()                     #print local var

z=10
def show():
    y="local"
    print(z)
    print(y)
show()

# enclosures - function within function

def outer():
    x='local'
    def inner():
        print(x)
    inner()
    print(x)

outer()

'''

def p():                                #outer func
    x=20
    def q():                            #inner func
        #global x                       #gives err (prgm searches x in global area not in outer func)
        nonlocal x                      #declaring to use var of outer func i.e p() (prgm searches x in outer func)
        x+=1                            #changes value of x of p()
        print(x)
    q()
    print(x)

p()


































