if __name__=='__main__':
    # what to do when this module run directly
    print('m1 module is %s'%(__name__))
else:
    # specify what to do when this module is imported
    print('i m in m1 else block')
