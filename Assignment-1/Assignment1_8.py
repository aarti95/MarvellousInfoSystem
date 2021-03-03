# Write a program which accept number from user and print that number of “*” on screen.

print("Enter numbers to be displayed on the screen")
number = int(input())

for i in range(number):
    print('*',end= " " )
    