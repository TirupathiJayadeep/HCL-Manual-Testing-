'''A bank stores transaction amounts for a customer's account.
 A continuous group of transactions may add up to a specific target amount.
The auditing system needs to determine how many different continuous transaction
groups produce exactly the specified amount.'''
lst=list(map(int,input().split(',')))
target=int(input())
count=0
for i in range(len(lst)):
    total=0
    for j in range(i,len(lst)):
        total+=lst[j]
        if total==target:
            count+=1
print(count)