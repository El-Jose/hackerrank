import os


def sockMerchant(n, ar):
    counter = 0
    aux = set()
    for i in ar:
        if i in aux:
            aux.remove(i)
            counter += 1
        else:
            aux.add(i)
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
