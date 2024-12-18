def f(x):
    #global a # this makes the variable "a" change from 5 to 7
    #a = 7
    x = x * 2 

def f2(x):
    x = x * 3
    return x


a = 5
f(a)
print(a) 
b = 7
b = f2(b)
print(b)