import os

"""
Complete the 'diagonalDifference' function below.

The function is expected to return an INTEGER.
The function accepts 2D_INTEGER_ARRAY arr as parameter.
"""
def diagonalDifference(arr):
    first_diag = 0
    second_diag = 0
    x, y = 0, len(arr)-1
    for i in arr:
        first_diag += i[x]
        second_diag += i[y]
        x += 1
        y -= 1
    return abs(first_diag - second_diag)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

