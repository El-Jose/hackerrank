# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab, bc = int(input()), int(input())
ac = math.hypot(ab,bc)                      
res = round(math.degrees(math.acos(bc/ac)))
degree = chr(176) 
print(f"{res}{degree}")
