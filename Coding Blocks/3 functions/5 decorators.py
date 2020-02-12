users={                             #dictionary
    'jatin':'pass',
    'prateek':'code'    
}

'''
def login(uname,password):
    if uname in users and users[uname]==password:
        print('logged in')
    else:
        print('invalid')

login('jatin','pass')
login('abc','pass')


def add(uname,password,a,b):
    if uname in users and users[uname]==password:
        print('valid=',a+b)
    else:
        print('invalid')

add('jatin','pass',3,5)
add('abc','pass',4,8)


def login_req(fn):                                           #Generic fn - standard fn for login for all the fns to reduce data redundancy
    def wrapper(uname,password,*args,**kwargs):
        if uname in users and users[uname]==password:
            fn(*args,**kwargs)                               #calling fn(if authenticated) which is earlier passed to login_req fn
        else:
            print('invalid')            
    return wrapper

def show(a,b):
    print(a+b)
#login_req(show)                                             #print a+b directly, wont chk for uname & password
x=login_req(show)                                            #connectivity between generic fn and the fn we want to use

print(type(x))

x('jatin','pass',1,-2)
x('asd','aasd',1,2)

q=show(5,6)                                                  #just a general eg.
#q(10,20)                                                    #print err

@login_req                                                   #same as line 'multi=login_req(multi)' or 'x=login_req(show)'
def multi(a,b):
    print(a*b)
multi('jatin','pass',100,400)
multi('asd','aasd',-50,62)

'''

# E.g.

def smart_div(func):
    def inner(p,q):
        if p<q:
            p,q=q,p
            func(p,q)
        else:
            func(p,q)
    return inner
#1.
def div(p,q):
    print(p/q)
div=smart_div(div)
div(2,4)

#2.
@smart_div
def div(p,q):
    print(p/q)
div(3,9)






















        




















