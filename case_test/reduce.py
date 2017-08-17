from functools import reduce
def fn(x,y):
    return 10*x+y

s=reduce(fn,[1,2.,3,4])
print(s)