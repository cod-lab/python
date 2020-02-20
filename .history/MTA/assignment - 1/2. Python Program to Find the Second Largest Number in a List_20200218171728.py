n=int(input("enter no. of elements:\t"))
list=[int(input()) for num in range(n)]
print(list)

x=max(list)
list.remove(max(list))
print("second largest no. is ",max(list))
list.append(x)

#print(list)