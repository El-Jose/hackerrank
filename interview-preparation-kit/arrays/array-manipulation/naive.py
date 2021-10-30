import os

def arrayManipulation(n, queries):
    arr = [0]*n
    max_value = 0
    for i in queries:
        for j in range(i[0]-1, i[1]):
            arr[j] += i[2]
            if arr[j] > max_value:
                max_value = arr[j]
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

