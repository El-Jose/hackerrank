from collections import deque
import os

def rot_left(array, d):
    array.rotate(-d)
    return array
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, d = map(int, input().split())
    a = deque(map(int, input().split()))
    result = rot_left(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

