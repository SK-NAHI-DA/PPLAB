f1=open('d:/Ctemp.txt','r')
f2=open('d:/Ftemp.txt','w')
contents = f1.readline()
t=contents.split()
for x in t:
    fh=9.0/5*float(x)+32
    f2.write(str(fh))
    f2.write('\n')
f1.close()
f2.close()
f2=open('d:/Ftemp.txt','r')
print('Contents of Ftemp.txt file')
for x in f2.readlines():
    print(x)
