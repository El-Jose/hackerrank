from collections import defaultdict
import os


def sockMerchant(n, ar):
    total = 0
    pairs = defaultdict(int)
    for i in ar:
        pairs[i] += 1
    for i in pairs.keys():
        total += pairs[i] // 2
        print(total)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()

