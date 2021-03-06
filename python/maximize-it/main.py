# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())
n = [list(map(int, input().split()))[1:] for _ in range(k)]
all_posible_combinations = product(*n)
results = map(lambda x: sum(i**2 for i in x) % m, all_posible_combinations)
print(max(results))
