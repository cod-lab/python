'''

def sheldon_knock():
    print('knock knock knock, me')
    print('knock knock knock, me')
    print('knock knock knock, me')

sheldon_knock()
print(10+20)
for i in range(10):
    print(i)
sheldon_knock()

'''

def sheldon_knock(name):
    print('knock knock knock {}'.format(name))
    print('knock knock knock {}'.format(name))
sheldon_knock('asd')

def sheldon_knock(name,ntime):
    for i in range(ntime):
        print('knock knock knock {}'.format(name))
sheldon_knock('ononpi',2)

def sheldon_knock(name,ntime=2):                               #default parameter, print 2 times bydefault
    for i in range(ntime):
        print('knock knock knock {}'.format(name))
sheldon_knock('3656')
sheldon_knock('nji',1)                                         #explicit declaration, print 1 time only

