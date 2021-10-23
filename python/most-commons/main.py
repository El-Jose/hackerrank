from collections import Counter

if __name__ == '__main__':
    [print(*c) for c in Counter(sorted(input())).most_common(3)]
