# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5
# Output : 16

def Add(number1, number2):
    result = number1 + number2
    return result

def main():
    print("Enter first number: ")
    number1 = int(input())
    print("Enter second number: ")
    number2 =int(input())
    Addition = Add(number1,number2)
    print("Addition of two number {} and {} is {}".format(number1,number2,Addition))


if __name__ == "__main__":
    main()