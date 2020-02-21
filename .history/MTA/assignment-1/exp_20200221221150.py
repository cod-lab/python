str1 = input("enter first string:\n")
print("first string is:\t--> ",set(str1))
str2 = input("enter second string:\n")
print("second string is:\t--> ",set(str2))
print("letters which are not common in both strings",set(str1)^set(str2))



""" a="coding blocks"
list1=[x for c in a]
print(list1) """