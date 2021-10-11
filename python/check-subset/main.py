# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
for i in range(a):
    m = int(input())
    y = set(map(int, input().split(" ")))
    n = int(input())
    z = set(map(int, input().split(" ")))
    if y.issubset(z):
        print(True)
    else:
        print(False)
