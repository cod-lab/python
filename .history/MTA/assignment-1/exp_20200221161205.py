n=int(input("enter no. of elements:\t"))
print("enter the elements:")
l=[int(input()) for num in range(n)]
print("list is ",l)
x,y=[],[]
for num in l:
    (lambda: (x.append(num)), lambda: "")[(num%2) == 0]()
print("odd list is ",x,"\n","even list is ",list(set(l) - set(even_list)))




    #x.append(int(input()))
    #print ("a" if n%2 == 0 else "b" if n%2 != 0 else "c")