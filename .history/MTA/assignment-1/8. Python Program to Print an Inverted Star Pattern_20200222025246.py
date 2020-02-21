n = int(input("enter number of rows:\t"))
for i in range (n,0,-1):
    print((n-i)*'X'+ i *'*')
    
    ''' n-i
    5-5 = 0
    5-4
    5-3
    5-2
    5-1 '''
    
m=5
for i in range(m,0,-1):
    print(i*'*')