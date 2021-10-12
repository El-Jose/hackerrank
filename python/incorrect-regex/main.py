# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    try:
        x = input()
        re.compile(x)
    except Exception as e:
        print(False)
    else:
        print(True)
