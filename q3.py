# 3. Write a Python script to create a list of first N even natural numbers.

for j in [2*i for i in range(1,int(input("Enter a number: "))+1)]:
    print(j,end=' ')