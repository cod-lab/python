def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(25)):
    print("Yes")
else:
    print("No")