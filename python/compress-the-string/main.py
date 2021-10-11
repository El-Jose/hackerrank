# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    from itertools import groupby
    # print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
    t = []
    for key, group in groupby(input()):
        t.append(
            (
                len(list(group)), int(key)
            ))
    print(*t)
