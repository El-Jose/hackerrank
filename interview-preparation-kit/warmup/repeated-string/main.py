import os

def repeatedString(s, n):
    x = n // len(s)
    y = n % len(s)
    count = s.count("a")*x
    if y > 0:
        count = count + str(s[:y]).count("a")
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()

