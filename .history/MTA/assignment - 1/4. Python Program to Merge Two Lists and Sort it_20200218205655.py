def lists(a,b,c,d):
    n1=int(input(a))
    print(b)
    l1=[int(input()) for num in range(n1)]
    n2=int(input(c))
    print(d)
    l2=[int(input()) for num in range(n2)]
    print(l1+l2)

b="enter the elements:"
lists("enter no. of elements for list1:\t",b,"enter no. of elements for list2:\t",b)
