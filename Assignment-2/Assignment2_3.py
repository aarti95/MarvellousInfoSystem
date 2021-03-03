# Write a program which accept one number from user and return its factorial.

def Factorial(number):
    value = 1
    for i in range(1,number+1):
        value = value * i
    return value

def main():
    print("Enter first number: ")
    number = int(input())

    Fact = Factorial(number)
    print("Addition of two number {} is {}".format(number, Fact))


if __name__ == "__main__":
    main()