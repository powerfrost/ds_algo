

array = [3, 2, 1]


for i in range(1, len(array)):

    # Assign key value
    key = array[i]

    # Assign prior index
    j = i - 1

    # While prior index is true, and key value is less than prior value
    while j >= 0 and key < array[j]:
        # Current value becomes prior value
        array[j+1] = array[j]
        # Prior index reduces by one
        j -= 1

    # Last prior index is replaced by key
    array[j+1] = key

    print(array)
