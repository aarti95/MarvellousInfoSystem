# 2. Write a recursive program which display below pattern.
# Input : 5
# Output : 1
# 2
# 3
# 4
# 5


def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')

printNos(5)