# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words = OrderedDict()
for _ in range(n):
    x = input()
    if x in words.keys():
        words[x] += 1
    else:
        words[x] = 1
print(len(words))
print(*words.values())
