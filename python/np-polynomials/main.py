import numpy as np

n = list(map(float, input().split()))
x = float(input())
print(np.polyval(n,x))
