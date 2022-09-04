# 7. Write a Python script to remove all non int values from a list.

l1=["AMAN",67,90,9.5,9,6+5j,2.5,True]
l2=[]
for i in l1:
    if(type(i)==int):
        l2.append(i)
    l1=l2       
print(l1)        
