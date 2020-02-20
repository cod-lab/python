n=int(input("enter no. of elements\n"))
list=[int(input()) for num in range(n)]
print(list)
x=max(list)
del(max(list))
print(list)
