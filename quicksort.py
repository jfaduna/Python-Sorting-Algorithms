from random import randint
import time

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    execution_start = time.time()
    quicksort(array)
    execution_time = time.time() - execution_start

    print(f"Execution Time: {execution_time}")