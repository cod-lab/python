class person():
    nationality = "indian"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name
        self.college = college
        print("my name is",self.name,"& my college is",self.college)
        print("my age is",age,"& my rollno. is",rollno)
        
    def fn1(self,msg):
        print(msg)
        
    def fn2(self):
        
        
obj1 = person("arihant","bpibs",22,12312)