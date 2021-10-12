# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = input().split()
scores = []
for _ in range(int(y)):
    scores.append(list(map(float, input().split())))

x = list(zip(*scores))
for i in x:
    print(sum(i)/len(i))
    
