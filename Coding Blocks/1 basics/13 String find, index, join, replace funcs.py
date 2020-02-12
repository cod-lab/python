'''

# Find Func - returns -1 if string not found

a="I love apple and I like apple"
print(a.find("apple"))              #chks from left and counts index(from left) of first encountered apple
print(a.rfind("apple"))             #chks from right and counts index(from left) of first encountered apple
print(a.find("apple",20))           #chks after index 20 and counts index(from left) of first encountered apple
print(a.find("apple",20,30))        #chks from index 20 to 30
print(a.find("apple",20,len(a)))    #chks from index 20 till end
print(a.find("asinons"))            #gives -1 if string not found


# Index Func - throws exception if string not found (gives err and stops execution)

a="I love apple and I like apple"
print(a.index("apple"))                 #chks from left and counts index(from left) of first encountered apple
print(a.rindex("apple"))                #chks from right and counts index(from left) of first encountered apple
print(a.index("apple",20))              #chks after index 20 and counts index(from left) of first encountered apple
print(a.index("apple",20,30))           #chks from index 20 to 30
print(a.index("apple",20,len(a)))       #chks from index 20 till end
print(a.index("asinons"))               #gives err if string not found


# Replace Func - replace selected words in the string
a="I love apple and I like apple"
print(a)
a=a.replace("apple","mango")
print(a)

# Count Func - counts the occurance of a word in the string
print(a.count("mango"))             
print(a.count("asasasf"))           #gives 0 if word not found


# Join
a="I love apple and I like apple"
print(a.split())
l=a.split()
print(l)

print(".?.".join(l))             #join splited words with .?.

x="\/\/"
print(x.join(l))                 #join through value of x

print(" ".join(l))
print("123".join(l))
print("inbtig".join(l))

'''

# Capitalize

company="actuality is here"
print(company.capitalize())         #capitalize only first char

# Title
print(company.title())              #capitalize first char of all the words of string



































