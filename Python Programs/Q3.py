'''Write a program which can compute the factorial of a given numbers.The
results should be printed in a comma-separated sequence on a single
line.Suppose the following input is supplied to the program:8
Then, the output should be:40320'''
def factorial(lst):
    res=[]
    for i in lst:
        fact=1
        for j in range(1,i+1):
            fact*=j
        res.append(fact)
        fact=1
    return res
lst=list(map(int,input().split(',')))
res=factorial(lst)
print(",".join(map(str,res)))