'''
# 1.While loop

print("how many no. u want to print")
n=int(input())
i=1
while(i!=n):        #print till n-1
    print(i)
    i+=1

print("how many no. u want to print")
n=int(input())
i=1
while(i<=n):        #print till n
    print(i,end=",\n")
    i+=1

print("how many no. u want to print")
n=int(input())
i=1
while(i<=n):        #print till n
    print("step %d"%i)
    i+=1

# 2.For loop

print(range(1,10))		  #print as string

for i in range(1,10):             #print till n-1
    print(i,end=",\n")

for i in range(1,10,2):           #takes jump of 2, print till n-1
    print(i,end=",\n")    

'''

# factorial of a no.
n=int(input())
b=1
for i in range(1,n+1):
    b*=i
print(b)

# 3.For each loop























