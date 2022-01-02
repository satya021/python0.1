import functools
m=functools[10,20,30,40,50]
res=functools.reduce(lambda a,b:a+b,m)
print("result=",res)