import os

def countingValleys(steps, path):
    position, valleys = 0, 0
    for i in path:
        if i == "D":
            position -= 1
        elif i == "U":
            init_position = position
            position += 1
            if init_position < 0 and position >= 0:
                valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
