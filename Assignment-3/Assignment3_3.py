# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.

def Minimum(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < minmin:
            min = arr[i]
    return min

def main():
    input_num = int(input("Enter the number of elements"))
    arr = []
    for i in range(input_num):
        print("Enter element number", i + 1)
        no = int(input())
        arr.append(no)
    print("Your entered data is:", arr)

    min = Minimum(arr)
    print("Maximum number is:",min)

if __name__ == "__main__":
    main()


