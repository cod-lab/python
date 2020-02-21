n=int(input("enter no. of elements:\t"))
print("enter the elements:")
l=[int(input()) for num in range(n)]
print("list is ",l)
x,y=[],[]
for num in l:
    (lambda: (x.append(num)), lambda: (y.append(num)))[(num%2) == 0]()
print("even list is ",x,"\n","odd list is ",y)




    #x.append(int(input()))
    #print ("a" if n%2 == 0 else "b" if n%2 != 0 else "c")