"""
Given an integer,(N) , and (N) space-separated integers as input, create a tuple,(T)  of those (N) integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""
if __name__ == "__main__":
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
