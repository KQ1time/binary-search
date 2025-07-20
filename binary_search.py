# Binary search

def binary_search(array, item):
    high = len(array) - 1
    low = 0
    while low <= high:
        middle = (high + low) // 2
        if item > array[middle]:
            low = middle + 1
        elif item < array[middle]:
            high = middle - 1
        else:
            return middle
    return -1
