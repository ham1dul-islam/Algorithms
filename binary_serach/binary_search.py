def binary_search(list, item):
    # Low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(list) - 1

    # While you haven't narrowed it down to
    # one element ...     
    while low <=high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = list[mid]
        # Found the item.
        if guess == item:
            return mid
        # The guess was too high.
        if guess > item:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1
    # Item doesn't exist
    return None


def main():
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))  # 1
    print(binary_search(my_list, -1))  # None
    
if __name__ == "__main__":
    main()

    
    