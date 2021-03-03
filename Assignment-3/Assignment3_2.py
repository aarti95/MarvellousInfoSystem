# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.

def Maximum(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def main():
    input_num = int(input("Enter the number of elements"))
    arr = []
    for i in range(input_num):
        print("Enter element number", i + 1)
        no = int(input())
        arr.append(no)
    print("Your entered data is:", arr)

    max = Maximum(arr)
    print("Maximum number is:",max)

if __name__ == "__main__":
    main()


