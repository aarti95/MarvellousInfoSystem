
def Addition(list):
    sum =0
    for i in range(len(list)):
        sum =sum +list[i]
    return sum
def main():
    input_num = int(input("Enter the number of elements"))
    arr=[]
    # List = list_prime(input_num)arr = []
    for i in range(input_num):
        print("Enter element number", i + 1)
        no = int(input())
        arr.append(no)

    print("Your entered data is:", arr)

    output = Addition(arr)
    print("Addition of list is ",output)

if __name__ == "__main__":
    main()


