def first_diff(s1,s2):
    min_len=min(len(s1),len(s2))
    for i in range(min_len):
        if s1[i]!=s2[i]:
            return i
        if len(s1)!=len(s2):
            return min_len
        return -1
s1=input("enter first string:")
s2=input("enter second string:")
result=first_diff(s1,s2)
print("fist difference at index:",result)
