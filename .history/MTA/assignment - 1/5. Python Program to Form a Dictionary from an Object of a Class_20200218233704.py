class person():
    private country = "India"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name
        self.college = college
        print("my name is",self.name,"& my college is",self.college)
        print("my age is",age,"& my rollno. is",rollno)
        
    def fn1(self,msg):
        print(msg,"I'm from",country)
        
    def fn2(self):
        x=input("enter ur name")
        y=input("enter ur clg")
        print("ur name is",x,"& ur college is",y)
        
        
obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()