'''

def add(a,b):
    return 10+6
add(2,5)                                #print nothing
print(add)                              #print err bcs accessing variable not fn
add=6,9                                 #variable...not fn...independent from fn add(), created tuple
print(add)                              #print value of add, accessing variable not fn

syntax --> variable = lambda arg1,arg2,arg3... : definition

add=lambda a,b:print(a+b)               #lambda fn will only hv 1 line in its body
add(2,5)                                #print value of add
print(add)                              #print err
add=5
print(add)                              #print value of add


a=[1,8,9,4,6,9]
print(a.sort())                         #sort the list a but return nothing
print(sorted(a))                        #return the sorted form of a

'''

a=[('jatin',5),('prateek',10),('pranav',1),('arnav',20)]
print(sorted(a))                                                #bydefault sorted by first element/cell of tuple/row/object in list

def z(x):
    return x[1]
print(sorted(a,key=z))                                           #sort by second element of tuple(using simple fn)

print(sorted(a,key=lambda x:x[1]))                               #sort by second element of tuple(using lambda fn)
                                                                 #key=formal parameter, x=tuple, x[1]=second cell of tuple

