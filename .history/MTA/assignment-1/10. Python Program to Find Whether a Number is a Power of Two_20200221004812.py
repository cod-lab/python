x=int(input("enter no. to check:\t"))
def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(x)):
    print("Yes")
else:
    print("No")