# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
array = list(map(int, input().split(" ")))
unique, repeated = set(), set()

for i in array:
    if i in unique:
        repeated.add(i)
    else:
        unique.add(i)

print(*unique.difference(repeated))
