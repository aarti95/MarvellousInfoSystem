# 3.Write a recursive program which display below pattern.

def PrintReverseOrder(N):
    if (N <= 0):
        return
    else:
        print(N, end=" ")

        PrintReverseOrder(N - 1)


N = int(input("Enter number"))
PrintReverseOrder(N);

