import hi_module                                #import file only, only connect file

hi_module.sayHi(' all gud')
hi_module.sayHello(' all gud',' & set\n')


from hi_module import *                         #import all fns

sayHi(' works fine')
sayHello(' works fine',' & reliable')
