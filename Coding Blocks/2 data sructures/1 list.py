'''

# List - like array, heterogenous list(contains both nums and chars)

a=[1,2,3,1.23,"asdas","asd"]
print(a)
print(type(a))

b=list([2,4,6,7,"aasd","asd","/.,';][;"])        #list constructor
print(b)
print(type(b))

c=list(b)                                       #string of b will add to c
print("this is c",c)

d=a+b                                           #string of a & b will add to d
print("this is d",d)

a.extend(["extended",2,3,";.][[."])             #string will add at the end to a
print(a)

b.extend([a])                                   #string of a will add at the end to b
print(b)

e=[i*i for i in range(1,6)]
print(e)

# List slicing                                  #removes multiple elements from the list
print(e[0:5])
print(e[0:4])
print(e[-6:-1])
print(e[-5:-1])
print(e[-4:-1])
print(e[-3:-1])
print(e[-2:-1])
print(e[-1:-1])
print(e[0:-1])
print(e[:-1])
print(e[-1:])
print(e[-3:])
print(e[-5:])


# Insertion

x=[1,2]
x.append(3)             #insert elements at the end of the list
print(x)
x.append(x)             #nested list (insert as list x in the list x)
print(x)
x.append([5,6])         #nested list (insert as list in the list x)
print(x)

x+=[7,8,9]              #insert as elements in the list x (not as list)
print(x)

print(x[4])             #gives element stored at 4th index
print(x[4][1])          #gives element stored at 1st index in the list stored in list

x.insert(2,20)          #add 20 after 2 elements
print(x)


# Delete

x.remove(3)             #del element 3 from the list
print(x)

del(x[5])               #gives element stored at 5th index
print(x)

x.remove(0)             #give err

'''

# POP

x.pop()                 #removes last element from the
print(x)
print(x.pop())          #print poped element from the list
print(x)

print(x*2)


l=["apple","mango","graped",56,98]
print(56 in l)
print("apple" in l)
#print(alknl in l)           #give err

for i in range(len(l)):
    print(l[i])

for y in l:
    print(y)

