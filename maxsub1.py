
"""
Brute force method to maximum subarray problem
Page 69 of intro to algo
n^3 running time
"""

array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]

def n3(array):
    maxy = -1000

    for start in range(len(array)):
        for end in range(start, len(array)):
            sum_now = sum(array[start:end])
            maxy = max(sum_now, maxy)

    print(maxy, start, end)

# n3(array)

"""
Brute force method to maximum subarray problem
Page 69 of intro to algo
n^2 running time
"""

array = [1, 4, -9, 50, -50, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]

def n2(array):
    maxy = -1000
    for start in range(len(array)):
        sum_now = 0
        for j in range(start, len(array)):
            sum_now += array[j]
            maxy = max(sum_now, maxy)

    print(maxy)


"""
Kandar's algo to maximum subarray problem
n running time
"""

array = [1, 4, -9, 50, -50, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]


def n(array):

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


    print max_so_far, start, end

# n(array)
