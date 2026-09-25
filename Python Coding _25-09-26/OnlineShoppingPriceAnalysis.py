'''An online shopping application stores the prices of products viewed by a customer
during a browsing session. The customer wants to identify a continuous range of products
that provides the maximum possible total discount value. Given the discount values,
determine the maximum value that can be obtained from any continuous range.'''
lst=list(map(int,input().split(",")))
highest=0
total=0
i=0
while i<len(lst):
    total+=lst[i]
    if total<0:
        total=0
    highest=max(highest,total)
    i+=1
print(highest)
