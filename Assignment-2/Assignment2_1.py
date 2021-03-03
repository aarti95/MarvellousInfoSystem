
# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.
from Arithematic2_1 import *

def main():
    print("Enter first number: ")
    number1 = int(input())
    print("Enter second number: ")
    number2 =int(input())

    Addition = Add(number1,number2)
    print("Addition of two number {} and {} is {}".format(number1,number2,Addition))

    Subtraction = Sub(number1, number2)
    print("Subtraction of two number {} and {} is {}".format(number1, number2, Subtraction))

    Multiplication = Mult(number1, number2)
    print("Multiplication of two number {} and {} is {}".format(number1, number2, Multiplication))

    Division = Div(number1, number2)
    print("Division of two number {} and {} is {}".format(number1, number2, Division))


if __name__ == "__main__":
    main()