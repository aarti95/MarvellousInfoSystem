# Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.


def Check_divisibity(number):
    if number % 5 == 0:
        return True
    else:
        return False
def main():
    print("Enter number: ")
    input_number = int(input())
    result = Check_divisibity((input_number))
    if result == True:
        print("Input number is divisible by 5")
    else:
        print("Input number is not divisible by 5")


if __name__ == "__main__":
    main()

