#method 1:
n = int(input("enter number of rows:\t"))
for i in range(n,0,-1):
    print(i*'*')



#method 2:
''' n = int(input("enter number of rows:\t"))
x=[y*'*' for y in range(n,0,-1)]
print('\n'.join(x)) '''



#method 3:
''' n = int(input("enter number of rows:\t"))
for i in range (n,0,-1):
    print((n-i)*'X'+ i *'*') '''
    
''' 
n-i
5-5 = 0
5-4
5-3
5-2
5-1 '''