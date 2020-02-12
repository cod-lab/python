'''

a="mango"
b="apple"
print(a+b)

print(b*5)       #creates multiple copies

# Slicing

print(a[1])      #slicing

print(a[1:])     #range slicing - print all chars starting from 1(a)

print(a[:])      #prints complete string, both start and end parameters are optional

print(a[1:4])    #prints till 3

print(a[1:-2])   #prints till end-1[-2-1=-3](n)

# Membership

a="coding blocks"
print('cod' in a)        #tells if substring(cod) is present in bigger string(a(coding blocks))
print('coding' in a)
print('asn' in a)

print('cod' not in a)
print('coding' not in a)
print('asn' not in a)

'''

# String Formating

print("my favouite food is %s and it comes from %c" % ("mango","h"))

# Triple quotes

a="""this is
multiline
paragraph"""

print(a)        #prints all 3 lines as it is

