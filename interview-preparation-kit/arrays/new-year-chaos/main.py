import os

def minimumBribes(q):
    bribes = 0
    for index in range(len(q)-1, 0, -1):
        #if element is different than index+1 means that the element was moved
        if q[index] != index+1:
            if q[index-1] == index+1:
                bribes += 1
                q[index-1], q[index] = q[index], q[index-1]
            elif q[index-2] == index+1:
                bribes += 2
                q[index-2], q[index-1], q[index] = q[index-1], q[index], q[index-2]
            else:
                print("Too chaotic")
                return
    print(bribes)    
    
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
