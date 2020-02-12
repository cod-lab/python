# INPUT
name=input()
print("hey "+name)
print(type(name))       #print variable type

age=int(name)
print(age)
print(type(age))

number=int(input())		#use to input only one element
print(number)
print(type(number))

#split
"10 20 30 40 50".split()    
a="10 20 30 40 50".split()          #print list of characters
print(a)

b=[no for no in a]                  #print list of characters
print(b)
b=[int(no) for no in a]             #print list of integers
print(b)

c=input().split()                               #print list of characters
print(c)
c=[no for no in input().split()]                #print list of characters
print(c)
c=[int(no) for no in input().split()]           #print list of integers
print(c)
