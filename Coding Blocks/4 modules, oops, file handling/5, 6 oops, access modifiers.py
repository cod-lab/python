'''

class person():
    pass

p=person()
print(p)
print(type(p))

class a():
    nationality='indian'                                            #class variable, data member, common for all object of a class
    
    def __init__(self,pn,clg):                                      #constructor, init is use to initialise the object of the class
        self.name=pn                                                #pn,clg are instance variable - these are different for every instance of class
        self.college=clg                                            #name,college are data members of class
        print('thats %s & %s'%(self.name,self.college))
        
    def hi(self,n):                                                 #self is a keyword for object and every member fn must contain this
        print('hey '+n)

    def fn1(self):
        print('this is %s'%(self.name))
        print('this is',self.college)

    def fn2(self):
        x=input('name: ')
        y=input('clg: ')
        print('i am',x,'\nmy clg is',y)

obj=a('me','my clg')
obj.hi('uh..!')
obj.fn1()
obj.fn2()

'''

class dog():
    color='brown'
    # activities=[]                                               #common list for all data members of class

    def __init__(self,breed):
        self.breed=breed
        self.activities=[]                                          #seperate list for each object
        
    def addActivity(self,act):
        self.activities.append(act)

    def __secretActivity(self):                                     #private method
        print(self.breed,'doing secret activity','\n')

    def doActivity(self):
        print(self.breed)
        print(self.activities)
        self.__secretActivity()                                     #private method only accesss through other method which is public

obj1=dog('german shepherd')
obj2=dog('golden retriever')

#obj1.__secretActivity()                                            #print err, private moethod can't be accessed directly
#obj2.__secretActivity()

obj1.addActivity('high jump')
obj1.addActivity('roll over')
obj2.addActivity('long jump')
obj2.addActivity('roll upside down')

obj1.doActivity()
obj2.doActivity()
    







































