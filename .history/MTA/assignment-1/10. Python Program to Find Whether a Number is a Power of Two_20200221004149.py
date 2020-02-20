import math
def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(n)):
    print("Yes")
else:
    print("No")