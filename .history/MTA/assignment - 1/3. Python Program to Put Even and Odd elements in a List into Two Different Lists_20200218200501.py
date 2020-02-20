#method 1:
n=int(input("enter no. of elements:\t"))
list1=[int(input()) for num in range(n)]
print("list1 is ",list1)
even_list = []
odd_list = []
for i in range(len(list1)):
    if list1[i]%2 == 0:
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
print("even list is ",even_list)
print("odd list is ",odd_list)

#method 2:
print("odd list is ",list(set(list1) - set(even_list)))         #stores elements in ascending order
