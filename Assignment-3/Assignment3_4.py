# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.

def Search(arr,num_search):
    freq = 0
    for i in range(0,len(arr)):
        if arr[i] != num_search:
            freq = freq + 1
    return brr

def main():
    input_num = int(input("Enter the number of elements"))
    arr = []
    for i in range(input_num):
        print("Enter element number", i + 1)
        no = int(input())
        arr.append(no)
    print("Your entered data is:", arr)

    num_search = int(input("Enter element to search in the list"))

    output = Search(arr, num_search)
    print("Frequency of element ", output)

if __name__ == "__main__":
    main()


