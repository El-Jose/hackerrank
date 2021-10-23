def merge_the_tools(string, k):
    lst = [string[i:i+k] for i in range(0, len(string), k)]
    set_list = [''.join(sorted(set(j), key=j.index)) for j in lst]
    for i in set_list:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
