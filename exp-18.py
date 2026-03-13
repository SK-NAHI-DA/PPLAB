def is_sorted(l1):
    l2=l1.copy()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False
list_1=[6,2,3,4,5]
res=is_sorted(list_1)
print(res)
    
        
