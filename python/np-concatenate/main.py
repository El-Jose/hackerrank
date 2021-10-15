import numpy

import numpy as np
n, m, p = map(int,input().split())
array_one = np.array([input().split() for _ in range(n)],int)
array_two = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((array_one, array_two), axis = 0))
