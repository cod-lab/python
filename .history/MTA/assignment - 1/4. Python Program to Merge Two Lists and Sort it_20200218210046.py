def lists(a,b,c):
    n1=int(input(a))
    print(b)
    l1=[int(input()) for num in range(n1)]
    n2=int(input(c))
    print(b)
    l2=[int(input()) for num in range(n2)]
    print("unsorted merged list is ",l1+l2)

b="enter the elements:"
lists("enter no. of elements for list1:\n",b,"enter no. of elements for list2:\n")
