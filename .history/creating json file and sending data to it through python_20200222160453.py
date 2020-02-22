import json
import pprint

class person():
    country = "India"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name                                                        #name, college (on RHS) r object(instance) variables
        self.college = college
        print("my name is",self.name,"& my college is",self.college)        #self.'name', self.'college' r cls variables with no predfined value
        print("my age is",age,"& my rollno. is",rollno)                         #age, rollno r object(instance) variables
        
    def fn1(self,msg):
        print(msg,"\nI'm from",self.country)                                #self.'country' is an object(instance) variable with predfined value
        
    def fn2(self):
        x=input("\nenter ur name:\t")
        y=input("enter ur college name:\t")
        print("ur name is",x,"& ur college is",y)
        
        z=input("\nenter ur country name:\t")
        print("x: ",type(x),"\tz: ",type(z))
        if z!=self.country:
            self.list1={}
            self.n=1
            self.n+=self.update_json('outsiders.json')  #-->
            #getting length of the dictionary by calling 'update_json' fn, Using 'read' fn to read the given json file to get the length of dictionary stored in that file
            
            self.list1[self.n]={x:z}
            
            self.update_json('outsiders.json')  #-->
            #calling 'update_json' fn to write data into json file, Using 'write' fn to write data in the dictionary in the given json file


    def update_json(self,file):
        #print(self.list1)
        #print("json",type(self.list1))
        
        #reading -->
        temp={}
        with open(file,'r') as f:                           #load outsiders.json file into ram, File is opened in reading mode
            temp=json.load(f)                               #print outsiders.json file data here        

        #writing -->
        temp.update(self.list1)
        with open(file,'w') as f:                           #creates json file on hdd(same folder) if not exist already and open it internally
            print(json.dump(temp,f),"adds to json")         #add data into outsiders.json file

        return len(temp)                                    #getting count no. of keys in dict and add into n
        

obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()