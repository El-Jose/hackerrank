# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
my_dequeu = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "append":
        my_dequeu.append(command[1])
        pass
    elif command[0] == "appendleft":
        my_dequeu.appendleft(command[1])
    elif command[0] == "pop":
        my_dequeu.pop()
    elif command[0] == "popleft":
        my_dequeu.popleft()

print(*my_dequeu)
