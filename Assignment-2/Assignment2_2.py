#Write a program which accept one number and display below pattern.


print("Enter the input number to draw the pattern of that size")
input_number = int(input())         #input number converted into integer

for i in range(1, input_number + 1):
    for j in range(1, input_number + 1):
        if j <= i:
            print("*", end=' ')
        else:
            print("*", end=' ')
    print()

