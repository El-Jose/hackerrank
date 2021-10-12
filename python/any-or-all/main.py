# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = input().split()
positives = all([int(i)>0 for i in x])
palindromic = any([j == j[::-1] for j in x])
print(positives and palindromic)
