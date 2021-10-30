import os


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    for index in range(len(arr)):
        while index +1 != arr[index]:
            swap_idx = arr[index] -1
            arr[index], arr[swap_idx] = arr[swap_idx], arr[index]
            count += 1
    return count
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()

