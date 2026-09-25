'''An e-commerce application stores the product IDs purchased by a customer in chronological
 order. The same product may appear multiple times. The system needs to determine the longest
  sequence of consecutive purchases in which every product ID is unique.'''
lst=list(map(int,input().split(",")))
longest=0
dic={}
left=0
for i in range(len(lst)):
    if lst[i]in dic and dic[lst[i]]>=left:
        left=dic[lst[i]]+1
    dic[lst[i]]=i
    longest=max(longest,i-left+1)
print(longest)