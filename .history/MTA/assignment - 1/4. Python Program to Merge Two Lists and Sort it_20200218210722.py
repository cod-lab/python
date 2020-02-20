def lists(a,b,c):
    n1=int(input(a))
    print(b)
    l1=[int(input()) for num in range(n1)]
    n2=int(input(c))
    print(b)
    l2=[int(input()) for num in range(n2)]
    
    print("list1 is ",l1)
    print("list2 is ",l2)
    print("unsorted merged list is ",l1+l2)
    print("sorted merged list is ",sorted(l1+l2))

lists("enter no. of elements for list1:\n","enter the elements:","enter no. of elements for list2:\n")