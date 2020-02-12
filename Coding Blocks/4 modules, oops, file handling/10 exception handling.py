'''

#f=open('a.txt','r')                #show predefined err if described file not found

try:
    f=open('a.txt','r')
except:
    print('file not found')         #try & exception print the prescribed err

try:
    f=open('a.txt','r')
except Exception:                   #'Exception' is an inbuilt class in python
    print('file not found')         #try & exception print the prescribed err
    print(Exception)                #print name of class
    print(type(Exception))          #print type of data structure
    

try:
    a=input('enter ur nme: ')                       #block 'else' run
    #a=10/0                                          #block 'Exception' run
    #f=open('a.txt','r')                             #block 'FileNotFoundError' run
    #a=b                                             #block 'NameError' run

except FileNotFoundError:                           #if file not found then this block will run
    print("file doesn't exist, plz reupload")

except NameError:
    print('variable not defined')
    print(NameError)                                #print name of class
    
except Exception:                                  #'Exception' is an inbuilt class in python, if any other err occurs then this block will run
    print("something's wrong")                      #try & exception print the prescribed err
    print(Exception)                                #print name of class
    print(type(Exception))                          #print type of data structure 'Exception' is

else:
    print('try executed successfully, no err found')
    print('ur name is',a)
    print('form submitted successfully')

'''

try:
    a=input('enter ur nme: ')
    if(len(a)<3):
        raise Exception                                     #run 'Exception' block

except Exception:
    print('enter ur complete name')        
    
else:
    print('try executed successfully, no err found')
    print('ur name is',a)
    print('form submitted successfully')

finally:                                                    #it will always run
    print('its finally block')

'''

try:
    a=input('enter ur nme: ')
    if(len(a)<3):
        raise Exception                                     #run 'Exception' block

except Exception:
    print('enter ur complete name')
    a=input('enter ur nme: ')
    if(len(a)<3):
        raise Exception
    
else:
    print('try executed successfully, no err found')
    print('ur name is',a)
    print('form submitted successfully')
'''






















    



