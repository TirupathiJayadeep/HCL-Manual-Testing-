'''A network monitoring system receives packet identifiers in chronological order.
 The system must determine the longest sequence of consecutive packets whose
 identifiers form a continuous numerical sequence, regardless of their original
 order in the incoming data.'''
nums=list(map(int,input().split(',')))
nums.sort()
longest=1
count=1
for i in range(1,len(nums)):
    if nums[i]==nums[i-1] + 1:
        count+=1
    elif nums[i]!=nums[i-1]:
        count=1
    longest=max(longest,count)
print(longest)