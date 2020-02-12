def myfunc(score,lang,roll):
    print("i scored %d in %s" % (score,lang))
    print(roll)

myfunc(100,"python",12)                        #order of args should match always else it will give err

myfunc(lang="python",roll=12,score=100)        #any order can go

print("hello","world",end='+')
print("\nhello","world",sep=' + ')
