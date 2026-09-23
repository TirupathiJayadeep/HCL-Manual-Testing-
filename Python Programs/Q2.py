'''Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
s=input()
Lcount=0
Dcount=0
for i in s:
    if i.isdigit():
        Lcount+=1
    elif i.isalpha():
        Dcount+=1
print("LETTERS ",Lcount)
print("DIGITS ",Dcount)
