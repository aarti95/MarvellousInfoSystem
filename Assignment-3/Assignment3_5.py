# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
from CheckPrime import *

def main():
    input_num = int(input("Enter the number of elements"))
    arr=[]
    # List = list_prime(input_num)arr = []
    for i in range(input_num):
        print("Enter element number", i + 1)
        no = int(input())
        arr.append(no)

    print("Your entered data is:", arr)

    output = ChkPrime(arr)
    print(output)

if __name__ == "__main__":
    main()


