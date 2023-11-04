from random import randint
import time


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array    

if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    execution_start = time.time()
    insertion_sort(array)
    execution_time = time.time() - execution_start

    print(f"Execution Time: {execution_time:}")
