# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    regex = r"^[-+]?[0-9]*\.[0-9]+$"
    x = bool(re.match(regex, input()))
    print(x)
