"""

"""
def print_rangoli(size):
    n = size
    al = list(map(chr, range(97, 123)))
    x = al[n-1::-1]
    y = al[1:n]
    z = x.copy()
    z.extend(y)
    z = "-".join(z)
    width = len(z) 
    res = [z]
    for i in range(n-1):
        x = x[:-1]
        y = y[1:]
        z = x.copy()
        z.extend(y)
        z = "-".join(z)
        z = z.center(width, "-")
        res.insert(0, z)
        res.append(z)
    
    for i in res:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
