"""
There is an array of N integers. There are also 2 disjoint sets, A and B, each containing  N integers. You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array M, if i E A, you add 1 to your happiness. If , you add -1 to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format

The first line contains integers N and N separated by a space.
The second line contains M integers, the elements of the array.
The third and fourth lines contain  integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
"""
if __name__ == "__main__":
    happiness = 0
    n = list(map(int, input().split(" ")))
    m = list(map(int, input().split(" ")))
    a = set(map(int, input().split(" ")))
    b = set(map(int, input().split(" ")))
    for _ in m:
        if _ in a:
            happiness +=1
        if _ in b:
            happiness -=1
    print(happiness)
