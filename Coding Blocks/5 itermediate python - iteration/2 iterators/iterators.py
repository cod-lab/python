#iterator object in python is an iterator that can be iterated upon using for loop or any other tool in python
#it returns single object one by one to us so that we can perform some task over it

'''
a=[1,2,3,4]                              #list, iterable object
for x in a:
    #perform some task on each element
    print(x**2)

a=[1,2,[8,9],3,4]                        #list in list, iterable object
for x in a: 
    print(x)

name='alpha'
for x in name:
    print(x)

d={'name':'alpha','age':'23','lvl':'rookie'}    #dictionary, iterable object
for x in d:                                     #return all the keys
    print(x)
    
for x in d.values():                            #return all the values
    print(x)

for x in open('txt1.txt','r'):
    print(x)

print('~'.join(['1','2','3','4','5']))

print('}-{'.join(d))

'''

a=list('alpha')
print(a)                                
print(list('alpha'))

a=[1,2,3,4]
print(sum(a))

d={1:'alpha',2:'23',3:'rookie'}
print(sum(d))                               #print the sum of keys

d={'alpha':1,'23':2,'rookie':3}
print(sum(d.values()))                      #print the sum of values


















