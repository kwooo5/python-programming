#demoscope function (function inside function)
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()# if its remove it will not work as it is calling the inner functions 

myfunc()

#global scoope 
x = 300 
def myfunc():
    print(x)
myfunc()
print(x)

x = 300 
def myfunc():
    print('inside functionx',x)
myfunc()
print(x)
print('inside functionx',x)

x = 300 
def myfunc_global():
    print(x)
myfunc_global()
print(x)