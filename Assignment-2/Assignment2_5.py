# 5.Write a program which accept one number for user and check whether number is prime or not.

print("Enter numbers to check : ")
num = int(input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Number is not prime", num)
            break
    else:
        print("Number is prime", num)
else:
    print("Number is not prime", num)