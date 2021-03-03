# .Write a recursive program which accept number from user and return
# summation of its digits.

def SumDigit( n ):
    if n == 0:
        return 0
    return (n % 10 + SumDigit(int(n / 10)))



N = int(input("Enter number"))

Sum = SumDigit(N)
print("Sum of given input digit {} is {}".format(N,Sum))