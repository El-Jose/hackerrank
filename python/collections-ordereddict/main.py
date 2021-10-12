# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
d = OrderedDict()

for _ in range(n):
    x = input().split()
    price = int(x.pop())
    product = " ".join(x)
    if product in d.keys():
        d[product] += price
    else:
        d[product] = price
for _ in d.keys():
    print(_,d[_])
