n = int(input())
array = []
for _ in range(n):
    array.append(str(input()))
print(len(list(set(array))))
