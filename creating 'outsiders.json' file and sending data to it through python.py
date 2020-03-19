import json
import os

class person():
    country = "india"

    def __init__(self,name,college,age,rollno):                             #constructor
        self.name = name                                                    #name, college (on RHS) r object(instance) variables
        self.college = college
        print("my name is",self.name,"& my college is",self.college)        #self.'name', self.'college' r cls variables with no predfined value
        print("my age is",age,"& my rollno. is",rollno,"\n")                #age, rollno r object(instance) variables
        
    def fn1(self,msg):
        print(msg,"\nI'm from",self.country)                                #self.'country' is an object(instance) variable with predfined value
        
    def fn2(self):
        x=input("\nenter ur name:\t")
        y=input("enter ur college name:\t")
        print("ur name is",x,"& ur college is",y)
        
        z=input("\nenter ur country name:\t")#+"\n"
        #z+="\n"
        #print("x: ",type(x),"\tz: ",type(z))
        
        if z.lower()!=self.country:
            n=1
            list1={}
            file = 'outsiders.json'

            #if os.path.isfile(file)                                        #also works
            if os.path.exists(file) == False:                               #chk if file exists or not
                print("file created:\t",file)
                #if file doesn't exists then it is created at this point(even before calling fn' 'update_json' for reading file)
            
            n+=self.update_json(file,list1)  #--> for reading
            #getting length of the dictionary by calling fn 'update_json', Using 'READ'(r) fn to read the given json file to get the length of dictionary stored in that file

            list1[n]={x:z}#+"\n" #print("jvgjv\n"+a)
            #list1+="\n"
            
            self.update_json(file,list1)  #--> for writing
            #calling fn 'update_json' to write data into json file, Using 'WRITE'(w) fn to write data in the dictionary in the given json file
            
            print("data added -->\n",list1)
        else:
            print("\nok! u r from here only\n(no data added to json)\n")
    
    def update_json(self,file,list1):
        #print(self.list1)
        #print("json",type(self.list1))
        
        temp={}
        if os.path.exists(file) and os.stat(file).st_size != 0:     #chk if file exists or not and file is empty or not by checking its size
            #reading -->
            with open(file,'r') as f:                               #load file 'outsiders.json' in READ(r) mode and creates file handler with name 'f' to handle file
                temp=json.load(f)                                   #print file 'outsiders.json' data here and also stores in 'temp' variable

        #writing -->
        temp.update(list1)                                          #adding data into variable 'temp' in which file 'outsiders.json' data is already stored
        with open(file,'w') as f:
        #open file 'outsiders.json' in WRITE(w) mode and creates file handler with name 'f' to handle file.
        #if file doesn't exist already then creates it automatically with the name given above and store it in the same folder    
            json.dump(temp,f)
            #add data of 'temp' variable into file 'outsiders.json' through file handler 'f' and overwrites previous data of the file

        return len(temp)                                            #getting length of data(no. of keys or values) stored in json file and returning it
        

obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()