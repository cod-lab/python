#x,y=[],[]
for n in range(1,5):
    #x.append(int(input()))
    #print ("a" if n%2 == 0 else "b" if n%2 != 0 else "c")
    (lambda: (x.append(n)), lambda: (y.append(n)))[(n%2) == 0]()
print(x,"\n",y)