'''

# Pass - alternative for any stmt.

for i in range(1,5):
    pass

x=2
for i in range(1,5):
    if x==5:
        pass
    print(i)

for i in range(1,10):
    if i==5:
        print(i*i)
    print(i)

# Break - stop & breaks the loop

for i in range(1,10):
    if i==5:
        break;  # breaks loop and come out of loop (for loop here)
    print(i)

'''

# Continue - skip a line of code

for i in range(1,10):
    if i==5:
        continue
    print(i)

