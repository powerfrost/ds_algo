def bubbleSort(array):

    n = len(array)
    for i in range(len(array)):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


arr = [5, 4, 3, 2, 1]

print(bubbleSort(arr))
