# Write a program which accept number from user and return addition of digits in that number.
print("Enter the name to be find the length")
number = int(input())
sum = 0
while(number > 0):
    digit = number % 10
    sum = sum + digit
    number = number //10


print("Addition of digit: ",  sum)