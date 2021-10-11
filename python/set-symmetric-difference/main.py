# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = set(map(int, input().split(" ")))
m = int(input())
y = set(map(int, input().split(" ")))
print(len(x.symmetric-difference(y)))
