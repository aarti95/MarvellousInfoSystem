# 5. Write a recursive program which accept number from user and return its
# factorial.

def fact(no):
    if(no == 0):
        return 1
    return no * fact(no-1)
value = int(input("Enter number"))
ret = fact(value)
print("Factorial of {} is {}".format(value,ret))