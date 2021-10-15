def wrapper(f):
    def fun(l):
        # complete the function
        #x = []
        #for i in l:
        #    x.append(list(i[-10:]))
        #for i in x:
        #    i.insert(5, " ")
        #    i.insert(0, "+91 ")
        #f(["".join(i) for i in x])
        f(["+91 " + i[-10:-5] + " " + i[-5:] for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
