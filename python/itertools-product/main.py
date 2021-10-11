"""
Task

You are given a two lists A and B. Your task is to compute their cartesian product AXB.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""
if __name__ == "__main__":
    from itertools import product
    a = map(int, input().split(" "))
    b = map(int, input().split(" "))
    c = list(product(a,b))
    for i in c:
        print(i, end=" ")
