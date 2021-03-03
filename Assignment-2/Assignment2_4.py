# 4.Write a program which accept one number form user and return addition of its factors.

print("Enter first number: ")
number1 = int(input())
add= 0
for i in range(1, number1):
    if number1 % i ==0:
        print(i)
        add = add+i
print("Addition of the factors:", add)
