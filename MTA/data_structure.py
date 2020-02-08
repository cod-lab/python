
print(5//2)
print(5/2)

#LIST
mydreamcars = ["audi","nano","porsche"]
for car in mydreamcars:
    print(car)

mydreamcars.append("ferrari")
for car in mydreamcars:
    print(car)

mydreamcars.remove("ferrari")
for car in mydreamcars:
    print(car)

print(mydreamcars.count("audi"))

#TUPLE
mymovies = ("end game","f&f","scary movie")

print(mymovies)

print(mymovies.count("end game"))

if "f&f" in mymovies:
    print("yes")
else:
    print("no")

#SETS

myset = {"kotlin","java","python"}

print(myset)
myset.pop()
print(myset)

#DICTIONARY
mydict = {"car":"merc",
          "color":"black",
          "model":"amg"}
#print(mydict)

for detail in mydict:
    print(detail)

print(mydict.keys())
print(mydict.values())




