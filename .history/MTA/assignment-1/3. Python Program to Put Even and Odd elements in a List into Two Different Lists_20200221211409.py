#method1:
n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list1=[int(input()) for num in range(n)]
print("list is ",list1)
odd_list=[]
for num in list1:
    (lambda: (odd_list.append(num),list1.remove(num)), lambda: "")[(num%2) == 0]()
print("odd list is ",odd_list,"\neven list is ",list(set(list1) - set(odd_list)))




#method 2:
""" n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list1=[int(input()) for num in range(n)]
print("list is ",list1)
even_list = []
for i in range(n):
    if list1[i]%2 == 0:
        even_list.append(list1[i])
print("even list is ",even_list)
print("odd list is ",list(set(list1) - set(even_list)))                 #stores elements in ascending order in list """



#method 3:
''' n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list1=[int(input()) for num in range(n)]
print("list is ",list1)
even_list = []
odd_list = []
for i in range(len(list1)):
    if list1[i]%2 == 0:
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
print("even list is ",even_list)
print("odd list is ",odd_list) '''