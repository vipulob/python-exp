# Tested on Python 2.7
class A:
    
    def __init__(self):
    # Init should not return anything. If returns then gives TypeError 
    # exception
    # It return None
        return 1    
       

a = A()

# This program will throw following errors
# TypeError: __init__() should return None

# If you want to return some other object when a class is called, 
# then use the __new__() method:

# From official Documentation
# As a special constraint on constructors, no value may be returned; 
# doing so will cause a TypeError to be raised at runtime.
