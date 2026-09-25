'''A hospital receives appointment requests represented by starting and ending
times. Some appointments overlap with each other. The scheduling
system needs to combine overlapping appointment periods so that the
final schedule contains only non-overlapping time ranges.'''
intervals=eval(input())
intervals.sort()
result=[]
for i in intervals:
    if not result or i[0]>result[-1][1]:
        result.append(i)
    else:
        result[-1][1]=max(result[-1][1],i[1])
print(result)