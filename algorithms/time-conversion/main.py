import os

"""
Complete the 'timeConversion' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.
"""

def timeConversion(s):
    x = s[:2]
    if s[-2:] == "AM":
        if x == "12":
            x = "00"
    elif s[-2:] == "PM":
        if int(x) < 12:
            x = str(int(x)+12)
    return("".join(x+s[2:-2]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
