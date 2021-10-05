"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == "__main__":
    commands = []
    my_list = []
    n = int(input())
    for _ in range(n):
        commands.append(str(input()).split(" "))
    
    for i in commands:
        if i[0] == "insert":
            my_list.insert(int(i[1]), int(i[2])) 
        elif i[0] == "print":
            print(my_list)
        elif i[0] == "remove":
            my_list.remove(int(i[1]))
        elif i[0] == "append":
            my_list.append(int(i[1]))
        elif i[0] == "sort":
            my_list.sort()
        elif i[0] == "pop":
            my_list.pop()
        elif i[0] == "reverse":
            my_list.reverse()
