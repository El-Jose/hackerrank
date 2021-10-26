import os

"""
Complete the 'birthdayCakeCandles' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY candles as parameter.
"""

def birthdayCakeCandles(candles):
    res = [0,0]
    for i in candles:
        if i > res[0]:
            res[0] = i
            res[1] = 1
        elif i == res[0]:
            res[1] += 1
    return res[1]    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

