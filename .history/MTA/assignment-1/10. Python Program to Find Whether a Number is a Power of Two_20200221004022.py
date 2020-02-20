x=int(input("enter the number to check:\t"))
squareroot= x**0.5
print(squareroot)
if(squareroot.is_integer()):
    print(x," is a Number is a Power of Two ")
else:
    print(x,"is not a number is a power of two")