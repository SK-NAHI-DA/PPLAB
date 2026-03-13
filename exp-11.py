import random
mylist=[]
for x in range(20):
    n=random.randint(1,100)
    mylist.append(n)
mylist.sort()
print(mylist)
print('max=',max(mylist))
print('min=',min(mylist))
print("second max=",mylist[-2])
print("second min=",mylist[1])
noe=0
for i in mylist:
    if i%2==0:
        noe=noe+1
print('even=',noe)        
