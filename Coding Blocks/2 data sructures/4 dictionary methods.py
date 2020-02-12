d={"mango":50,"apple":80}
print(d)

'''

# get()
print(d.get('mango'))               #print value of key mango
print(d.get('man'))                 #print none(when no key found)
print(type(d.get('man')))           #print nonetype

if 'mago' in d:
    print('price of mango is %d'%(d['mango']))
else:
    print('no key found')

if 'man' not in d:
    print('price of mango is %d'%(d['mango']))
else:
    print('no key found')

# items()                #returns list of tuples(key,value)(all rows), this method convert dictionary into list
print(d.items())

del d['apple']           #delete key apple from the list
print(d)

# update()
a={'cherry':60}
d.update(a)             #merging of 2 dictionaries or adding data of a to d
print(d)
#d.update('asdsa',65)

# len()                  #print no. of key values are there in the dictonary
print(len(d))

# clear                  #clear all the method
d.clear()
print(len(d))
print(d)

'''

# zip                   merge two lists, creates dictionary
x=['wsf','yukty','erg','qzxcz']
y=[21,36,548,78]

#print(zip(x,y))        #creates zip object 
print(dict(zip(x,y)))
print(type(dict(zip(x,y))))

for i in dict(zip(x,y)):                    #print all keys
    print (i)
for i in dict(zip(x,y)).keys():             #print all keys
    print (i)
for i in dict(zip(x,y)).values():           #print all values
    print (i)




































