
"""
Brute force method to maximum subarray problem
Page 69 of intro to algo
n^2 running time
"""

array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]

maxy = -1000

for i in range(len(array)):
    sum = 0
    for j in range(i, len(array)):
        sum += array[j]
        if sum > maxy:
            maxy = sum
            start = i
            end = j
            
print(maxy, start, end)
