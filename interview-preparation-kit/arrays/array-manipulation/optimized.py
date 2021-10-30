import os

def arrayManipulation(n, queries):
    arr = [0]*n
    max_value = 0
    temp = 0
    for i in queries:
        start_idx = i[0]-1
        end_idx = i[1]-1
        value = i[2]
        arr[start_idx] += value
        if end_idx + 1 < len(arr):
            arr[end_idx + 1] -= value

    for i in arr:
        temp +=i
        if temp > max_value:
            max_value = temp    
    return max_value
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()

