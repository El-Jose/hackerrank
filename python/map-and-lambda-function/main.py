cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    res = [0,1]
    if n in res:
        return res[:n]
    for i in range(2,n):
        res.append(res[i-2]+res[i-1])
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
