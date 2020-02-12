'''
# Reading
f=open('txt1.txt','r')                      #only read file
print(f.read())
f.close()                                   #close file

# Writing

f=open('txt1.txt','w')                      #only write file, not read(wont open file)

content='hello world\n'
a=[content]*3                               #list created

#f.write(a)                                 #print err as it only takes strings
f.writelines(a)
f.write(content*2)
f.writelines(content*2)                     #writelines is use to write multiple lines
f.write('content1\n')
f.writelines('content2\n')

#print(f.read())                            #print err as file can only be written, cant read
f.close()


# Reading

f=open('txt1.txt','r')
#print(f.read())                            #read and print all the data from txt1 file as it is
print(f.readline())                         #read and print only first line of the file
#print(f.readlines())                       #create and print the list of lines present in the file

x=f.readlines()
print(x)
print(type(x))

'''

# Reading using WITH OPEN

with open('txt1.txt','r') as y:             #as y: means we are opening the file and this is the file handler
    print(y.closed)                         #chk if file is closed or not, false-not closed
    print(y.read())
    y.seek(50)                              #read file from 51th index
    print(y.read())                         #print all data from 51th index or after 50th index
    y.close()                               #file is closed
    print(y.closed)                         #true-file closed
    #print(y.read())                        #print err, after closing file it is not operable

#a file automatically closes after its caller/opener block ends

print(y.closed)                             #even if y.close had not written above, it would still print true
















    



