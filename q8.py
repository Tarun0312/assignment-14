# 8. Write a Python script to print distinct elements along with their frequencies of
# occurrence in the list.

l1=[56,89,56,8,90,8,90,56]

l1=sorted(l1)

i=0 
j=0
while(i<len(l1)):
    count=0
    while(j<len(l1) and l1[i]==l1[j]):
        count+=1
        j+=1
    print("%d - %d"%(l1[i],count))    
    i=j         