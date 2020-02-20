import json
import pprint

class person():
    country = "India"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name                                                        #name, college (on RHS) r object(instance) variables
        self.college = college
        print("my name is",self.name,"& my college is",self.college)     #self.'name', self.'college' r cls variables with no predfined value
        print("my age is",age,"& my rollno. is",rollno)                         #age, rollno r object(instance) variables
        
    def fn1(self,msg):
        print(msg,"\nI'm from",self.country)                             #self.'country' is an object(instance) variable with predfined value
        
    def fn2(self):
        x=input("\nenter ur name:\t")
        y=input("enter ur college name:\t")
        print("ur name is",x,"& ur college is",y)
        
        z=input("\nenter ur country name:\t")
        self.list={}
        if z!=self.country:
            self.list[x]=z
            self.update_json('outsiders.json')
            ''' with open('outsiders.json','w') as e:              #creates json file on hdd(same folder) if not exist already and open it internally
                json.dump(list,e)                              #add data into outsiders.json file
            with open('outsiders.json','r') as f:              #load outsiders.json file into ram
                pprint.pprint(json.load(f))                    #print outsiders.json file data here

            print(list) '''
            print("fn2",type(self.list))
            
    def update_json(self,file):
        print(self.list)
        print("json",type(self.list))
        temp={}
        with open(file,'r') as f:
            temp=json.load(f)
        temp.update(self.list)
        with open(file,'w') as f:
            print(json.dump(temp,f))
        


        
obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()