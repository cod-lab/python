class person():
    country = "India"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name                                             #name, college (on LHS) r object(instance) variables with no predfined value
        self.college = college
        print("my name is",self.name,"& my college is",self.college)            #self.'name', self.'college' r cls variables
        print("my age is",age,"& my rollno. is",rollno)                         #age, rollno r object(instance) variables
        
    def fn1(self,msg):
        print(msg,"\nI'm from",self.country)                          #country is an object(instance) variable with predfined value
        
    def fn2(self):
        x=input("enter ur name")
        y=input("enter ur college name")
        print("ur name is",x,"& ur college is",y)
        
        z=input("\nenter ur country name")
        outsiders=[]
        if z!=self.country:
            outsiders += []
        
obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()