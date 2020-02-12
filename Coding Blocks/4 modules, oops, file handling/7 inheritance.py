print('\n1.\n')
class schoolMember():                                           #parent/base class

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('initialized school member: %s'%self.name)

    def intro(self):
        print('Name: %s\nAge: %d'%(self.name,self.age))

class teacher(schoolMember):                                    #child/derive class, inherited class schoolMember

    def __init__(self,name,age,salary):
        schoolMember.__init__(self,name,age)
        self.salary=salary
        print('initialized teacher: %s'%self.name)

    def intro(self):
        schoolMember.intro(self)
        print('Salary: %d'%self.salary,'\n')

class student(schoolMember):

    def __init__(self,name,age,marks):
        schoolMember.__init__(self,name,age)
        self.marks=marks
        print('initialized student: %s'%self.name)

    def intro(self):
        schoolMember.intro(self)
        print('marks: %d'%self.marks)

t=teacher('mr.chu',55,800000)
t.intro()
s=student('ravi',15,90)
s.intro()

print('\n2.\n')
class schoolMember():                                           #parent/base class

    def __init__(self,name):
        self.name=name
        print('initialized school member: %s'%self.name)

    def intro(self,age):
        self.age=age
        print('Name: %s\nAge: %d'%(self.name,self.age))

class teacher(schoolMember):                                    #child/derive class, inherited class schoolMember

    def __init__(self,name):
        schoolMember.__init__(self,name)
        print('initialized teacher: %s'%self.name)

    def intro(self,age,salary):
        schoolMember.intro(self,age)
        self.salary=salary
        print('Salary: %d'%self.salary,'\n')

class student(schoolMember):

    def __init__(self,name):
        schoolMember.__init__(self,name)
        print('initialized student: %s'%self.name)

    def intro(self,age,marks):
        schoolMember.intro(self,age)
        self.marks=marks
        print('marks: %d'%self.marks,'\n')
        
t=teacher('mr.chu')
t.intro(55,800000)
s=student('ravi')
s.intro(15,90)
