def root(x,n=2):
    return x**(1/n)
x=int(input("enter a number:"))
n=int(input("enter an number:"))
res1=root(x,n)
res2=root(x)
print("the value withour default n=",res1)
print("the value wioth default n=",res2)
