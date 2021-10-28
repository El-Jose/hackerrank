import os


def jumpingOnClouds(c):
    index = 0
    jumps = 0
    while index < n-1:
        if index+2 < n and c[index+2] == 0:
            index += 2
            jumps += 1
        elif index+1 < n and c[index+1] == 0:
            index += 1
            jumps += 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

