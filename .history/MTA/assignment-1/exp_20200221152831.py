n,m=int(input("enter no. of elements")),int(input("enter no. of elements"))
x,y=[int(input()) for num in range(n)],[int(input()) for num in range(m)]
for n in range(1,5):
    (lambda: (x.append(n)), lambda: (y.append(n)))[(n%2) == 0]()
print(x,"\n",y)




    #x.append(int(input()))
    #print ("a" if n%2 == 0 else "b" if n%2 != 0 else "c")