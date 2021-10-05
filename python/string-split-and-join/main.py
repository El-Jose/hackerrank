"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line):
    temp = line.split(" ")
    return ("-").join(temp)

if __name__ == "__main__":
    l = str(input())
    print(split_and_join(l))

