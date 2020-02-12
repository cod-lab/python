d={}
print(type(d))

d={"mango":50,"apple":80}                #dictionary   key-mango,value-50
print(d)
print(type(d))
print(d["mango"])                        #print value of key mango

d["guava"]=40                            #adds key guava to the dictionary at the end
print(d)

d["grape"]=[12,20]                       #adds key grape with value as array to the dictionary
print(d)
print(d['grape'])

d['banana']={'small':20,'large':40}      #adds key banna with value as dictionary to the dictionary
print(d)
print(d['banana'])
print(d['banana']['small'])              #print value of small banana

print(d.keys())                         #print all the keys of d
print(d.values())                       #print all the values of d
