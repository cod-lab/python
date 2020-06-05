n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list1=[int(input()) for num in range(n)]

s=int(input("now enter the sum:\t"))

for x in list1:
	for y in list1:
		if x+y==s:
			print("the pair is:\t",x,"(at",list1.index(x),"), ",y,"(at",list1.index(y),")")

# i=0

# for x in range(n):
# 	i+=1
# 	if i<n:
# 		if list1[x]+list1[x+i]==s:
# 			print("the pair is:\t",list1[x],list1[x+i])
# 	else:
# 		i-=1
# 		x+=1
# 		if list1[x]+list1[x+i]==s:
# 			print("the pair is:\t",list1[x],list1[x+i])
