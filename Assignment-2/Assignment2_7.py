#Write a program which accept one number and display below pattern.


print("Enter number: ")
number = int(input())

for i in range(1, number + 1):
    for j in range(1, number + 1):
        if j == i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

