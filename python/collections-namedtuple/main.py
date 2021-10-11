# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
students = []
marks = 0.0
columns = input().split(" ")
for i in range(n):
    x = input().split()
    Student = namedtuple("Student", ",".join(columns))
    students.append(Student._make(x))
for i in students:
    marks += float(i.MARKS)
print(marks / len(students))
