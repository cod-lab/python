n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list1=[int(input()) for num in range(n)]
print("list is ",list1)
odd_list=[]
for num in list1:
    (lambda: (odd_list.append(num),list1.remove(num)), lambda: "")[(num%2) == 0]()
print("odd list is ",odd_list,"\neven list is ",list(set(list1) - set(odd_list)))




""" a="coding blocks"
list1=[c for c in a]
print(list1) """