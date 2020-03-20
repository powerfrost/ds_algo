




def insertion(array):

    for i in range(1, len(array)):

        key = array[i]
        j = i - 1

        while j > -1 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array


array = [3, 2, 1]
print(insertion(array))
