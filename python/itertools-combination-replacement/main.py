if __name__ == "__main__":
    from itertools import combinations_with_replacement as cwr

    line, times = input().split()
    x = cwr(sorted(line), int(times))
    for i in x:
        print("".join(i))
