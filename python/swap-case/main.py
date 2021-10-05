"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
if __name__ == "__main__":
    res = ""
    s = str(input())
    for i in s:
        if i.islower():
            res += i.upper()
        else:
            res += i.lower()
    print(res)
