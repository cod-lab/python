print("enter the number to check")
x = int(input())
squareroot= x**0.5
print(squareroot)
if(squareroot.is_integer()):
    print(x," is a Number is a Power of Two ")
else:
    print(x,"is not a number is a power of two")