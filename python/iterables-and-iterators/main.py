# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    from itertools import combinations
    n = int(input())
    x = input().split(" ")
    m = int(input())
    counter = 0
    
    x = list(combinations(x,m))
    for _ in x:
        if "a" in _: counter += 1
    print(counter/len(x))
