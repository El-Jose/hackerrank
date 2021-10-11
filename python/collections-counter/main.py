# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
shoes = Counter(input().split(" "))
m = int(input())
total = 0

for _ in range(m):
    size, price = input().split(" ")
    if size in shoes.keys() and shoes[size] > 0:
        shoes[size] -= 1
        total += int(price)
print(total)
