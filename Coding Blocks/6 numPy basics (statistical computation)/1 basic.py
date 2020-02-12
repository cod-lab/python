import numpy as np                          #numpy is used to implement multi-dim array (1d is allowed without using this)

'''
#array/matrix of variables/numbers
print(np.array([1,2,3,4,5]))
print(type(np.array([1,2,3,4,5])))

a=np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.shape)                              #attribute 'shape' of array, returns the dimension of the array

b=np.array([[1,2,3,4,5],[9,8,7,6,5]])
print('\n',b)
print(b.shape)
print(b[0][4])
print(b[1][3])
print(np.array([['a','b','c','d'],['d','c','b','a']]))

c=np.array([[1],[2],[3],[4],[5]])
print('\n',c)
print(c.shape)
print(c[0][0])
print(c[1][0])
print(c[2][0])
print(c[3][0])
print(c[4][0])
print(type(c))


print(np.zeros((3,3)))                           #gives array of '0', matrix having 0 value only
d=np.zeros((3,3))
print(d)

print(np.ones((3,3)))                            #gives array of '1', matrix having 1 value only
d=np.ones((3,3))
print(d)


#array/matrix of constant
print(np.full((3,2),2))                           #creates array of constant
e=np.full((3,2),5)
print(e)
print(np.full((3,3),'pqr'))

#indentity matrix - always square
print(np.eye(5))
f=np.eye(4)
print(f)


#random matrix - any no. of elements of integers only
print(np.random.random((3,2)))
x=np.random.random((2,3))
print(x)
print(type(x))
print(x[0,1])
print(x[1,0])
print(x[:,2])                           #':' used for range of rows or cols
print(x[1,],'\n')

y=np.random.random((5,5))
print(y,'\n')
print(y[1,1:4])                         #gives 2nd row and col 2 to 4
print(y[1:4,2],'\n')                    #gives row 2 to 4 nd 3rd col
print(y[0:5,0:5])                       #gives row 1 to 5 and col 1 to 5
print(y[:,:])                           #gives row 1 to 5 and col 1 to 5

y[0:5,0:5]=2                            #set values of row 1 to 5 and col 1 to 5 as 2
print(y)
y[:,:]=1                                #set values of row 1 to 5 and col 1 to 5 as 1
print(y)


#slicing - set some elements of matrix to change value
g=np.zeros((5,5))
print(g)
g[2,]=5                                 #targeting 3rd row and no col
print('\n',g)
g[:,2]=5                                #targeting no row and 3rd col
print('\n',g)
g[:,-1]=-1                              #targeting no row and last col
print('\n',g)
g[-1,]=-1                               #targeting last row and no col
print('\n',g)


#datatypes
g=np.zeros((5,5))
print(g.dtype)                          #print default datatype of array which is float64
g=np.zeros((5,5),np.int64)              #changed datatype of array to int64
print(g.dtype)


#mathematical operations - element wise operations only(not matrix wise)

#addition
p=np.array([[1,2],[3,4]])
q=np.array([[5,6],[7,8]])
r=np.array([[9,10],[11,12]])
print(p)
print(q)
print(p+q)                              #add matrices
print(np.add(p,q))                      #add matrices
print(p+q+r)                            #add n matrices
print(np.add(p,q,r))                    #add only 2 matrices(first two matrices)

#subtraction
print('\n',q-p)                         #subtract p from q
print(np.subtract(p,q))                 #subtract q from p
print('\n',p-q-r)                       #do the subtractioin on n matrices
#print(np.subtract('\n',q,p,r))         #gives err when more than 2 matrices described


#multiplication - element wise/not a dot product
p=np.array([[1,2],[3,4]])
q=np.array([[5,6],[7,8]])
r=np.array([[9,10],[11,12]])
print(p*q)                              #multiply elements of matrices(not the complete matrix/dot product)
print(np.multiply(p,q))                 #multiply two matrices
print('\n',p*q*r)                       #do the multiplication on n matrices
#print(np.multiply('\n',p,q,r))         #gives err when more than 2 matrices described


#division
p=np.array([[1,2],[3,4]])
q=np.array([[5,6],[7,8]])
r=np.array([[9,10],[11,12]])
print(p/q)                              #divide elements of matrices(not the complete matrix)
print(np.divide(p,q))                   #divide two matrices
print('\n',p/q/r)                       #do the division on n matrices
#print(np.divide('\n',p,q,r))           #gives err when more than 2 matrices described


#sqrt
p=np.array([[4,9],[16,25]])
q=np.array([[5,6],[7,8]])
print(np.sqrt(p))
#print(np.sqrt(p,q))                    #gives err when more than 1 matrices described


#matrix multiplication/dot product
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
z=np.array([[9,10],[11,12]])
print(x)
print(y)
print('\n',x.dot(y))                       #multiply x.y
print(np.dot(x,y))                         #multiply x.y
print('\n',y.dot(x))                       #multiply y.x
print(np.dot(y,x))                         #multiply y.x
print('\n',y.dot(x,z))                     #multiply y.x
print(np.dot(y,x,z))                       #multiply y.x


#multiplication/dotproduct of vectors/array - output would be scalar
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a.dot(b))                            #gives multiplication of 2 vectors/array/matrices(a.b)
print(b.dot(a))                            #gives multiplication of 2 vectors/array/matrices(b.a)

print(sum(a))                              #sum all the elements of vector/array a
print(np.sum(a))

c=np.array([[1,2,3,4],[5,6,7,8]])
print(c)
print(sum(c))                              #column wise addition, adding all elements in all cols, adding vertically
print(np.sum(c,axis=0))                    #column wise addition, adding all elements in all cols, adding vertically
print(np.sum(c,axis=1))                    #row wise addition, adding all elements in all rows, adding horizontally

#stacking of arrays
print('\n',np.stack((a,b),axis=0))         #join two arrays row wise, horizontally
print(np.stack((a,b),axis=1))              #join two arrays column wise, verically

d=np.array([9,10,11,12])
print('\n',np.stack((a,b,d),axis=0))       #join multiple arrays horizontally
print(np.stack((a,b,d),axis=1))            #join multiple arrays verically

'''

#reshape the array/matrix - change the dimension of array without adding or deleting any element
r=np.array([[1,2,3,4,5],[9,8,7,6,5]])
print(r)
print(r.reshape(5,2))
print(r.reshape(10,1))                      #eleminate cols
print(r.reshape(10))                        #eleminate rows, linear array
print(r.reshape(1,10))                      #eleminate rows, linear array

print('\n',r.reshape(10,-1))                #automatically figure out no. of cols 
print(r.reshape(-1,5))                      #automatically figure out no. of rows 






















