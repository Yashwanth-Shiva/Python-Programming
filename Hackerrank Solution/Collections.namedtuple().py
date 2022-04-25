# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
field=input()
total=0
stud=namedtuple("stud",field)
for i in range(n):
    student=stud(*input().split())
    total+=int(student.MARKS)
print("{:.2f}".format(total/n))
