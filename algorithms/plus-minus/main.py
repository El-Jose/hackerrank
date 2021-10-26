import os

"""
Complete the 'plusMinus' function below.
The function accepts INTEGER_ARRAY arr as parameter.
"""

def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            pos += 1
        else:
            neg += 1
    print("{0:.6f}".format(pos/len(arr)))
    print("{0:.6f}".format(neg/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

