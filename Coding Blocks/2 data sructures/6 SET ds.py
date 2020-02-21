#unorderedset
#unique elements, elements not repeated

'''

a=set([1,1,2,4,2,5,4,7,89,65,41,12])            #set{}
print(a)                                        #no element repeated
print(type(a))

f={'a','df','g','h',43,8}                       #set{}
print(f)
print(type(f))

#add
a.add(8)                                        #add 8 at appropriate place in set
print(a)

#union
b=set([3,45,89,74])
print(b.union(a))                               #all nos. of a are placed at appropriate place in b, union of both

#intersection
print(b.intersection(a))                        #common in a, b is printed

#difference
print(b.difference(a))                          #delete elements of a present in b and print remaining b

#or/union
print(b|a)                                      #or/union

#and/intersection
print(b&a)                                      #and/common

#minus/difference
print(b-a)
print(a-b)

a.clear()                                       #delete all elements of a(empty set)

#membership
if 13 in b:
    print('present')
else:
    print('nopes')

if 96 not in b:
    print('ok')
else:
    print('nopes')

'''
#Symmetric difference (^)
x={1,2,3,6,54}
y={2,6,54,98,7,8}
print(x^y)                                      #uncommon elements only, print elements present only in any one set not in both