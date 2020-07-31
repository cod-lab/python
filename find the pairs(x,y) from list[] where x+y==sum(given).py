def twoSum(nums,sum):
	cache={}
	for i in range(len(nums)):
		# print(cache)
		if nums[i] in cache:
			return [cache[nums[i]], i]
		cache[sum - nums[i]] = i

n=int(input("enter no. of elements:\t"))
print("enter the elements:")
nums=[int(input()) for num in range(n)]

sum=int(input("now enter the sum:\t"))

print(twoSum(nums,sum))


'''
for i in range(len(list1)):
	for j in range(len(list1)):
		if list1[i]==list1[j]:
			continue;
		if list1[i]+list1[j]==sum:
			print("the pair is:\t",list1[i],"(at",i,")") #, ",list1[j],"(at",j,")")
'''

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
