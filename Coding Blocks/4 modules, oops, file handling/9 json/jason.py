import json

  

# Python object

book={
    'name':'learning python',
    'page':1341,
    'authors':[
       {'name':'A1','age':30},
       {'name':'A2','age':40}
    ]
}

print(type(book))
print(book['authors'][0])
print(book['page'])

# python to json
with open('myjsonfile.json','w') as f:          #creates json file on hdd(same folder) if not exist already and open it internally
    json.dump(book,f)                           #dumping(writing/copying) book(python(on ram)) into json file(on hdd)
                                                #dump-convert data with any ds to string and dump it to file in form of string

import pprint                                   #pretty print header file for prettier text
# json to python
with open('myjsonfile.json','r') as f:
    #print(json.load(f))                        #print data of json file direclty
    d=json.load(f)                              #load-read data from json file, convert it(string) to any(earlier) ds and store it in d
    pprint.pprint(d)                            #print text prettier
    print('d is',type(d))

# any ds to string
#print(json.dumps(book))                        #convert dictionary(book) to string and return and print it

s=json.dumps(book)                              #convert dictionary to json string and store in s 
print(s)                                        #dumps-convert and return any ds into string (nothing to do with file)
print('s is',type(s))

# string to any ds
obj=json.loads(s)                               #convert json string to json object(its previous ds)(dictionary object)
print(obj)                                      #loads-convert and return string into any(earlier) ds (nothing to do with file)
print('obj is',type(obj))



new=json.dumps(s)                               #convert dictionary to json string and store in new 
print(new)                                      #dumps-convert and return any ds into string (nothing to do with file)
print('new is',type(new))




