import os
import ast

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
            file = 'txt1'                                                   #file can be created of any format or evn without any

            #if os.path.isfile(file)                                        #also works
            if os.path.exists(file) == False:                               #chk if file exists or not
                print("file created:\t",file)
                #if file doesn't exist then it is created at this point(even before calling fn 'update_file' for reading file)
            
            n+=self.update_file(file,list1)  #--> for reading
            #getting length of the dictionary stored in variable 'temp' by calling fn 'update_file', Using 'READ'(r) fn to read the given file to get the length of string stored in that file

            list1[n]={x:z}#+"\n" #print("jvgjv\n"+a)
            #list1+="\n"
            
            self.update_file(file,list1)  #--> for writing
            #calling fn 'update_file' to write dict data stored in variable 'temp' in string format into file, Using 'WRITE'(w) fn to write(add) data in the given file
            
            print("data added -->\n",list1)
        else:
            print("\nok! u r from here only\n(no data added to file)\n")
    
    
    def update_file(self,file,list1):
        temp={}
        if os.path.exists(file) and os.stat(file).st_size != 0:     #chk if file exists or not and file is empty or not by checking its size
            #reading -->                                            #executes only if file exists and isn't empty
            f = open(file,"r")                                      #load file 'txt1' in READ(r) mode in file-handler 'f' to access file
            temp = ast.literal_eval(f.read())    #str --> dict      #take data of file 'txt1' through file-handler 'f' and convert str data to dict and store in variable 'temp'
            f.close()                                               #file is closed
            
        #writing -->
        temp.update(list1)                                          #adding data into variable 'temp' in which file data is already stored
        f = open(file,"w")
        #load file 'txt1' in WRITE(w) mode in file-handler 'f' to access file
        #if file doesn't exist already then creates it automatically with the name given above and store it in the same folder
        f.write(str(temp).replace("'}, " , "'},\n\t").replace("{1: {'" , "{\n\t1: {'").replace("'}}" , "'}\n}"))        
        #dict --> str
        #convert dict data stored in variable 'temp' to str and edit string by replacing multiple sub-strings with the given sub-strings and write updated string into file 'txt1' through file-handler 'f'
        #f.write(str(d).translate(str.maketrans({"},": "},\n", "{'1": "{\n'1", "'}}": "'}\n}"})))   #'str.maketrans' takes only one char to replace
        f.close()                                                   #file is closed
        
        return len(temp)                                            #getting length of data(no. of keys or values) stored in 'temp' or file and returning it
        

obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()