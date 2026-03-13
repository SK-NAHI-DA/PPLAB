def merge(l1,l2):
    res=[]
    i,j=0,0
    while i<len(l1)and j<len(l2):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    res=res+l1[i:]+l2[j:]
    return res
list_1=[1,3,5,7]
list_2=[2,4,6,8]
final_list=merge(list_1,list_2)
print("the given lists are:")
print("List_1=",list_1)
print("List_2",list_2)
print("the final sorted list=",final_list)
