str1 = input("enter first string:\n")
a=list(str1)
print("first string is:\t--> ",list(str1))
str2 = input("enter second string:\n")
b=list(str2)
print("second string is:\t--> ",list(str2))

for i,j in list(str1)[:],list(str2)[:]:
    if i != j:
        print(i,j)
    