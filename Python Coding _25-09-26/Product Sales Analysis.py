'''A retail company stores the daily sales quantity of a product for several consecutive
days. Due to seasonal changes, some days may have negative adjustments. The company wants
to identify the period that produced the highest multiplication of sales-related values.
Develop a solution to determine this maximum product.'''
lst=list(map(int,input().split(",")))
currentmax=lst[0]
currentmin=lst[0]
maximum=lst[0]
for i in range(1,len(lst)):
    if lst[i]<0:
        currentmax,currentmin=currentmin,currentmax
    currentmax=max(lst[i],currentmax*lst[i])
    currentmin=max(lst[i],currentmin*lst[i])
    maximum=max(maximum,currentmax)
print(maximum)