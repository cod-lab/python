'''
# Infinite Loop

# Reverse Loop

for i in range(10,1,-1):
    print(i,end=",")

'''

# Nested Loop

n=10
for x in range(n):
    for y in range(n):
        print(max(x+1,y+1,n-x,n-y),end=" ")
    print()


