'''

# STRINGS
str1=("capital of india is %s" % "delhi")                                                             #1.
print(str1)
str2=("capital of %s is %s" % ("india","delhi"))                                                      #2.
print(str2)
str3="capital of {} is {} and its located at {}, {}". format("india","delhi","65.16","87.15")         #3.
print(str3)
str4=6                                                                                                #4.
print(str4*2**2)

# END
print("this is 1", end=" - ")
print("this is 2")

# SEP
print("a","b","c", sep='\n')

a="coding blocks"
print(a)
print(a[1])
print(a[2])
print(a[0])
print(a[-1])
print(a[-4])

print(len(a))

# a[2]='q' (editing string) its not allowed in python

for i in range(len(a)):
    print(a[i])

'''

a="coding blocks"
for c in a:
    print(c)
    
for l in a:
    print(l)

# b("asdaf") this type of defining is not allowed in python
    
    
    


