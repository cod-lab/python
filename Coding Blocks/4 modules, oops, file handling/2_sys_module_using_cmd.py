#execute through cmd. Wont run through python shell

#sys module provide access to variables related to system or python interpreter

import sys

print(sys.argv)                                             #print list of cmd line args(input enetered at runtime)(no input for this cmd tho)

#print(int(sys.argv[1])+int(sys.argv[2]))                    #take 2 inputs at time of executing the file and add them, for intergers
#print(float(sys.argv[1])+float(sys.argv[2]))                #take 2 inputs at time of executing the file and add them, for floating nos.

print(sys.version)

print(sys.path)                                             #print locs where python interpreter looks for the package

#print(sys.maxint)
print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)
