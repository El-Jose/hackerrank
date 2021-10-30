import os


def hourglassSum(arr):
    sums = []
    for i in range(4):
        for j in range(4):
            hourglass_top = arr[i][j] + arr[i][j+1] + arr[i][j+2] 
            hourglass_mid = arr[i+1][j+1]
            hourglass_bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total = hourglass_top + hourglass_mid + hourglass_bottom
            sums.append(total)
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
