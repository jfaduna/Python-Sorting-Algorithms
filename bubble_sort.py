from random import randint
import time


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
        if sorted:
            break

if __name__ == "__main__":
    ARRAY_LENGTH = 10000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    execution_start = time.time()
    bubble_sort(array)
    execution_time = time.time() - execution_start

    print(f"Execution Time: {execution_time:}")
