''' n=int(input("enter no. of elements:\t"))
list=[int(input()) for num in range(n)]
print("list is ",list)
even_list = []
odd_list = []
for i in range(len(list)):
    if list[i]%2 == 0:
        even_list.append(list[i])
    else:
        odd_list.append(list[i])
print("even list is ",even_list)
print("odd list is ",(list - even_list)) '''

n=int(input("enter no. of elements:\t"))
list=[int(input()) for num in range(n)]
print("list is ",list)
even_list = []
odd_list = []
for i in range(len(list)):
    if list[i]%2 == 0:
        even_list.append(list[i])

print("even list is ",even_list)

for i in range(len(list),len(even_list)):
    if list[i] != even_list[i]:
        print("odd list is ",list[i])