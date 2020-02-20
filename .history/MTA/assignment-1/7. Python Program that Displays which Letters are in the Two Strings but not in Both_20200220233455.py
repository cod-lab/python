str1 = input("enter first string:\n")
print("first string is:\t--> ",list(str1))
str2 = input("enter second string:\n")
print("second string is:\t--> ",list(str2))

for i,j in list(str1)[:],list(str2)[:]:
    if i != j:
        print(i,j)
    