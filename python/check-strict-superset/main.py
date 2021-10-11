# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split(" "))
n = int(input())
r = True
sets = []
for i in range(n):
    x = set(input().split(" "))
    sets.append(x)
for i in sets:
    if not a.issuperset(i):
        r = False
print(r)

