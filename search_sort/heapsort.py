

arr = [12, 11, 13, 5, 6, 7]


def heapify(array, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)

def heapSort(array):

    n = len(array)

    for i in range(n-1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array

print(heapSort(arr))
