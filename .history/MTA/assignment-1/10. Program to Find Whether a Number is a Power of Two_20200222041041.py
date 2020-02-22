#method 1:
n=int(input("enter a no. to check:\t"))
(lambda: print(n,"is not power of 2"), lambda: print(n,"is power of 2"))[(n and (not(n & (n-1))))]()

# n&n-1 --> do the bitwise(*) operation on the binary value of n and n-1



#method: 2
''' x=int(input("enter no. to check:\t"))
def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(x)):
    print("Yes")
else:
    print("No") '''