'''
A college maintains the daily attendance details of its students
in the form of a list containing student IDs. Some students may have
attended multiple sessions on the same day. The administration wants
to identify the longest continuous sequence of sessions in which no student ID is repeated.
Develop a solution that determines the maximum length of such a sequence.
'''
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