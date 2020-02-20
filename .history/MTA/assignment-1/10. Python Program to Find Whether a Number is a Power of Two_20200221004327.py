x=int(input("enter no. to check"))
def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(x)):
    print("Yes")
else:
    print("No")
    
