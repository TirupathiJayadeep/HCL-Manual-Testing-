'''A company stores the monthly performance scores of an employee for several months.
 The scores may contain both positive and negative values depending on the employee's
 performance. Management wants to identify the continuous period during which the
  employee achieved the highest overall performance.'''
lst=list(map(int,input().split(',')))
left=lst[0]
right=lst[0]
start=0
sstart=0
end=0
for i in range(1,len(lst)):
    if lst[i]>left+lst[i]:
        left=lst[i]
        start=i
    else:
        left+=lst[i]
    if left>right:
        right=left
        sstart=start
        end=i
print(lst[sstart:end+1])
