def lists(a,b,c,b):
    n1=int(input(a))
    print(b)
    l1=[int(input()) for num in range(n1)]
    n2=int(input(a))
    print(b)
    l2=[int(input()) for num in range(n2)]
    print(l1+l2)


''' n1=int(input("enter no. of elements for list1:\t"))
print("enter the elements:")
l1=[int(input()) for num in range(n1)]
n2=int(input("enter no. of elements for list2:\t"))
print("enter the elements:")
l2=[int(input()) for num in range(n2)]
print(l1+l2) '''

b="enter the elements:"
lists("enter no. of elements for list1:\t",b,"enter no. of elements for list2:\t",b)
print(l1+l2)