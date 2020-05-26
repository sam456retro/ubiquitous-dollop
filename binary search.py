def binary_search(arr, low, high, x):  
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid  
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x)
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return -1

def main():
    arr = []
    h = int(input("enter the number of numbers you want in the array:  "))
    for i in range(0,h):
        ele = int(input("enter the " + str(i) +" element:  "))
        arr.append(ele)
    print("the array entered:  " + str(arr))
    x = int(input('enter the number you want to search:  '))
    result = binary_search(arr, 0, len(arr)-1, x) 
    if result != -1:
        print("the element searched is at " + str(result) + " index of the array entered")
    else:
        print("the element is not present in the array")


if True:
    main()
