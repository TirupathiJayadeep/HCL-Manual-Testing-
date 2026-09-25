'''A city installs buildings of different heights along a straight road.
During rainfall, water gets collected between taller buildings.
The engineering team needs to calculate the total amount of water that can
remain trapped after heavy rainfall based on the heights of the buildings'''
lst=list(map(int,input().split(',')))
n=len(lst)
leftmax=[0]*n
rightmax=[0]*n
leftmax[0]=lst[0]
for i in range(1,n):
    leftmax[i]=max(leftmax[i-1],lst[i])
rightmax[n-1]=lst[n-1]
for j in range(n-2,-1,-1):
    rightmax[j]=max(rightmax[j+1],lst[j])
water=0
for i in range(n):
    water+=min(leftmax[i],rightmax[i])-lst[i]
print(water)