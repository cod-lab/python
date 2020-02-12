'''

a="""this is
    multiline
    paragrapgh"""
print(a)
print(type(a))

print(a.split())             #split into words
b=a.split()
print(type(b))
print(type(b[1]))
print(type(b[3]))

print(a.splitlines())        #split into para lines

fruit="mango"
print(fruit.upper())                #print in uppercase
fruit=(fruit.upper())
print(fruit.lower())                #print in lowercase


shake2=shake="   apple shake    "
print(shake)
print(len(shake))

shake=shake.lstrip()            #removes leading space only(space before word)
print(shake)
print(len(shake))

shake=shake.rstrip()            #removes ending space only(space after word)
print(shake)
print(len(shake))

print(shake2)
print(len(shake2))
print(shake.strip())            #removes all extra space
print(len(shake))

'''

a="12314"
print(a.isdigit())             #chk if a has only nos. or not

a="naisnfi"
print(a.isalpha())             #chk if a has only chars or not

a="/,.';][?:{;"
print(a.isdigit())
print(a.isalpha())

a="jhvjhv76575"
print(a.isalnum())               #chk for both no & char (still cant include other chars)

print(a.islower())              #chk for lowercase
print(a.isupper())              #chk for uppercase

a="  "
print(a.isspace())              #chk for spaces only


































