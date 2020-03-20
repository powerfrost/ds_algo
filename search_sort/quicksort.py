

def partition(array, low, high):

    pivot = high
    i = low - 1

    for j in range(low, high):
        if array[j] <= array[pivot]:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[pivot] = array[pivot], array[i+1]
    return i+1


array = [4, 5, 6, 7, 1, 3]

def quickSort(array, low, high):

    if low < high:

        pivot = partition(array, low, high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)

quickSort(array, 0, len(array)-1)

print(array)



# This code is contributed by Mohit Kumra
