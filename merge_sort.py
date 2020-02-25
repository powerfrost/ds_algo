def msort(array):

    #  This section breaks down the array

    # Base case
    # If length of array is less than 2, return
    if len(array) < 2:
        return array
    # Define middle of the array
    # Define left of the array and call msort to break it down further
    # Define right of the array and call msort to break it down further
    mid = len(array)//2
    left = msort(array[:mid])
    right = msort(array[mid:])
    result = []

    # Define an empty array called result


    # This section builds the array back up
    # While loop with conditions that left and right are both bigger than zero
        # If left is bigger than right
        # Add right index zero to result
        # Remove index zero on right
        # Else
        # Add left to result
        # Remove index zero on left

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)

    result += left
    result += right

    return result

    # Add left to result
    # Add right to result

x = [6, 5, 4, 3, 2, 1]
print(msort(x))
