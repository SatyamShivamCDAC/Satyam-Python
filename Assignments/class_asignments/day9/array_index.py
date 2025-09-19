while(True):
    arr = [1,2,3,4,5,6,7]

    index = int(input("write an index of array to be accessed : "))
    if(index>=len(arr)):
        print("Lenght of array is 7")
        continue
    print(arr[index])

    c = int(input('Press 1 to continue and 0 to exit : '))
    if (c == 0):
        break