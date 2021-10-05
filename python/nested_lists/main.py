"""
Given the names and grades for each student in a class of (N) students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    import pdb; pdb.set_trace()
    second_lowest = sorted(set([score for name, score in students]))[1]
    names = sorted([i[0] for i in students if i[1] == second_lowest])
    for _ in names: print(_)
