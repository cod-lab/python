'''

# default args

def abc(d=4,e=5):
    print(d,e)

abc()

def abc(d,e):                       #formal parameters
    print(d,e)

abc(7,'lkfmkl')                     #actual parameters

# keyword args

abc(e=7,d='lkfmkl')                 #explicit declaration of parameters


# packed args

print('this','is','a','fruit')      #args in print()

def show(*x):                       #positional args (packs any no. of given args into a tuple & pass it to this fn as 'x') (not a pointer of c/c++)
                                    #this is used to give any no. of actual parameters without declaring formal parameters
    print(x)

show()
show(1,2,3,'asdaf')


def show(a,b,c,*x):    #*x=args     #positional args with formal parameters (min of 3 args must be given for a,b,c)
                                    #(apart from a,b,c all left n args will be packed into x)
    print(x)
    print(a,b,x)
    print(a,b,c,x)

#show('ojn',)                       #print err (atleast 3 args must be given)
show(1,2,'asdaf')
show(1,2,3,'asdaf')


def show(a,b,c,*x,p,q):             #positional args with formal parameters (min of 3 args must be given for a,b,c)
                                    #(no actual parameter will store in p,q because all parameters after 3 formal parameters will store into x)
                                    #(apart from a,b,c all left n args will be packed into x, not a single args in p,q)
                                    #print err because no default value is given to p,q and actual parameter cant be declared to these,
                                    # so they must be defined when declared for the first time(implicitly) or explicitly
    print(x)
    print(a,b,x)
    print(a,b,c,x,p,q)

#show('ojn',)                                           #print err (atleast 3 args must be given and value for p,q must be given)
#show(1,2,'asdaf')                                      #print err (value for p,q must be given)
show(1,2,3,'asdaf',45,'asdf',5165,p=0,q=0)              #explicit declaration of p,q


def show(a,b,c,*x,p='p',q='q'):                         #implicit declaration (requires min of 3 args) (produces no err)
                                                        # (explicit declaration can also done at further stage to change the value of p,q)
    print(x)
    print(a,b,c)
    print(a,b,c,x)
    print(a,b,c,x,p,q)

#show(1)                                                #print err(min 3 args)
show('a','b','c','sdf','sdom','wdfwef','wef')
show('a','b','c','sdf','sdom','wdfwef','wef',p=0,q=0)   #explicit declaration of p,q

'''

def show(a,b,c,*x,p='p',q='q',**y):     #**y=kwargs     #everything's same except one thing i.e the undefined varibles will be stored in y)
                                                        # (explicitly declarated and defined varibles)
    print(a,b,c,x,p,q)
    print(y)
    print(a,b,c,x,p,q,y)

show('a','b','c','sdf','sdom','wdfwef','wef')           #print empty list for y
show('a','b','c','sdf','sdom','wdfwef','wef',name='munna',profession='BHAI')            #the order of args must be according to implicit declaration
show('a','b','c','sdf','sdom','wdfwef','wef',p=0,name='munna',q=0,profession='BHAI')




    

























