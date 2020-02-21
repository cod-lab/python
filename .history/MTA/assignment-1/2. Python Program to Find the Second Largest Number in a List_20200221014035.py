#method 2:
n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list=[int(input()) for num in range(n)]
print("list is ",list)
print("largest no. in the list is ",max(list))
x=max(list)
list.remove(max(list))
print("second largest no. is ",max(list))
list.append(x)

#print(list)