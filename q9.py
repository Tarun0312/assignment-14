# 9. Write a Python script to print indices of all occurrences of a given element in a given
# list.

l1=[6,89,9,6,89,7,9,89]

x=int(input("Enter an element: "))

i=0
while(i<len(l1)):
    if(l1[i]==x):
        print(i,end=' ')
    i+=1


