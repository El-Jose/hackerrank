import numpy

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array = numpy.array(array)
print(numpy.transpose(array))
print(array.flatten())
