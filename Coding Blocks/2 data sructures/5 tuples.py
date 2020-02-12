# hold together multiple object
# update not allowed
# data is constant(write protected)
# comma seperated heterogenous enteries within () - (1,'dasd',2.3)
# tuple faster than list
# returns multiple values from a fn

'''

a=(1,2,5,'hello')           #produce tuple
print(a)                    #tuple

print(a[0])
#a[0]=5                     #gives err(cant update)
print(a)

b=list(a)                   #tuple() converted to list[]
print(b)                    #list
b[0]=5                      #now it can be updated
print(b)                    

c=tuple(b)                  #list[] converted to tuple() 
print(c)                    #tuple

print(a+c)                  #concatenation
print(c*2)                  #repeatition
print(b*2)

print(len(a))

'''

d=(1,-5,9,7,3)
print(max(d))
print(min(d))

del(d)                      #del tuple
