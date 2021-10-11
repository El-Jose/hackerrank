n = int(input())
s = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    x = list(input().split())
    try:
        if x[0] == "pop":
            s.pop()
        if x[0] == "remove":
            s.remove(int(x[1]))
        if x[0] == "discard":
            s.discard(int(x[1]))
    except:
        pass
print(sum(list(s)))
