"""

"""
if __name__ == "__main__":
    from itertools import permutations
    line, n = input().split(" ")
    a = sorted(list(permutations(line, int(n))))
    for i in a:
        b = "".join(i)
        print(b)
