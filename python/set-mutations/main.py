# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = set(map(int, input().split(" ")))
m = int(input())

for _ in range(m):
    command = input().split(" ")
    if command[0] == "intersection_update":
        x.intersection_update(set(map(int, input().split(" "))))
    elif command[0] == "update":
        x.update(set(map(int, input().split(" "))))
    elif command[0] == "symmetric_difference_update":
        x.symmetric_difference_update(set(map(int, input().split(" "))))
    elif command[0] == "difference_update":
        x.difference_update(set(map(int, input().split(" "))))

print(sum(list(x)))
