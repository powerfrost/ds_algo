def maxSubArraySum(array):

    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0

    for i in range(len(array)):
        if array[i] > array[i] + max_ending_here:
            max_ending_here = array[i]
            start = end = i
            max_so_far = max(max_so_far, max_ending_here)
        else:
            max_ending_here += array[i]
            end = i
            max_so_far = max(max_so_far, max_ending_here)


    return max_so_far, start, end

array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]



print(maxSubArraySum(array))
