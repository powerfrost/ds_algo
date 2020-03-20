def msort(array):

    if len(array) < 2:
        return array

    mid = len(array)//2
    left = msort(array[:mid])
    right = msort(array[mid:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left)
    result.extend(right)

    return result

x = [6, 5, 4, 3, 2, 1]
print(msort(x))
