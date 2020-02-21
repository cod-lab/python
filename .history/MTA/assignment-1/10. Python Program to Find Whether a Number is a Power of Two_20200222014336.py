#method 1:
n=int(input("enter no. to check:\t"))
(lambda: print("not power of 2"), lambda: print("power of 2"))[(n and (not(n & (n-1))))]()



#method: 2
''' x=int(input("enter no. to check:\t"))
def isPowerOfTwoNumber(x):
    return (x and (not(x & (x-1))))

if(isPowerOfTwoNumber(x)):
    print("Yes")
else:
    print("No") '''