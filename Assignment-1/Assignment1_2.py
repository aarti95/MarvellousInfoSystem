# Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11
# Output : Odd Number
# Input : 8
# Output : Even Number

def ChkNum(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    print("Enter the input number")
    input_number = int(input())         #input number converted into integer
    result = ChkNum(input_number)       #calling function
    if result == True:
        print("Given input number {} is Even Number".format(input_number))
    else:
        print("Given input number {} is  Odd Number".format(input_number))


if __name__ =="__main__":
    main()