n = int(input("enter no. to print table:\t"))
m = int(input("enter the no. times to multiply n:\t"))
i=1
a = [n*(i+1) for m in range(n)]
print(a)