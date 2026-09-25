'''A company receives a list of employee skill codes represented as strings.
Employees having the same set of characters in their skill codes belong to
the same skill category, even if the characters appear in a different order.
The HR system needs to organize employees into appropriate skill groups.'''
from collections import defaultdict
lst=input().split(',')
dic=defaultdict(list)
for i in lst:
    key="".join(sorted(i))
    dic[key].append(i)
print(list(dic.values()))