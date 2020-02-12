'''

a=[1,20,46,5,2,3,4]
print(max(a))               #gives max element
print(min(a))               #gives min element


# Searching
print(a.index(5))           #gives index of element 5

# Sorting
sorted(a)                   #print sorted list (not change original list)
print(a)                    #print original list
a=sorted(a)                 #sort original list
print(a)

b=[2,8,6,3,4,9]
b.sort()                    #sort original list
print(b)
b.sort(reverse=True)        #sort in decreasing order
print(b)


n=input()                   #gives string(not list)
print(n)
print(type(n))

n=input().split()           #create list of chars
print(n)
print(type(n))


n=int(input())          #used to input only one element(integer)
print(n)
print(type(n))

n=[int(n) for n in input().split()]          #create list of integers 
print(n)
print(type(n))

'''

n=[int(n)*int(n) for n in input().split()]          #create list of square integers 
print(n)
print(type(n))






















