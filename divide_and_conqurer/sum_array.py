def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sum_recursive(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_recursive(arr[1:])

def main():
    print(sum([1,2,3,4,5]))  # 15
    print(sum([1,2,3,4,5,6,7,8,9,10]))  # 55
    print(sum_recursive([1,2,3,4,5]))  # 15
    print(sum_recursive([1,2,3,4,5,6,7,8,9,10]))  # 55    
    return

if __name__ == "__main__":
    main()