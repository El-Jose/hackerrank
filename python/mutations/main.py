"""
Read a given string, change the character at a given index and then print the modified string.
"""

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == "__main__":
    string = input()
    opts = input().split(" ")
    x = mutate_string(string, int(opts[0]), opts[1])
    print(x)
