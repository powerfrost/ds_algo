import math

def maximum_subarray_recursion(numlist,low,high):
    """
    This function takes an array of numbers, and find the sum of the maximum
    subarray in the list.
    Input: A list of real numbers; the beginning and the end of the part in the list.
    Output: Indices and sum.
    """
    if low == high: # base case
        return low,high,numlist[low]
    else:
        mid = (int(math.ceil(float(low + high)/2)))
        left_l,left_h,left_sum = maximum_subarray_recursion(numlist,low,mid - 1)
        right_l,right_h,right_sum = maximum_subarray_recursion(numlist,mid,high)
        cross_l,cross_h,cross_sum = max_crossing_array(numlist,low,mid,high)
        final = max(left_sum,right_sum,cross_sum)
        if left_sum == final:
            return left_l,left_h,left_sum
        elif right_sum == final:
            return right_l,right_h,right_sum
        else:
            return cross_l,cross_h,cross_sum

def max_crossing_array(sublist,low,mid,high):
    """
    This helper function tries to find the indices of a maximum subarray that
    crosses the midpoint, and return the sum.
    Input: A list of real numbers.
    Output: The indices of a maximum subarray that crosses the midpoint, together
    with its sum.
    """
    inf = float('inf')
    left_sum = -inf
    s = 0
    i = mid - 1
    # beware that i and j should be consistent with maximum_subarray configurations;
    # that is, if use ceiling, then (mid - 1) and mid; if using floor,
    # then mid and (mid + 1).
    while i >= low:
        s = s + sublist[i]
        if s > left_sum:
            left_sum = s
            left_index = i
        i -= 1
    right_sum = -inf
    s = 0
    j = mid
    while j <= high:
        s = s + sublist[j]
        if s > right_sum:
            right_sum = s
            right_index = j
        j += 1
    total = left_sum + right_sum
    return (left_index,right_index,total)

array = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]

print(maximum_subarray_recursion(array, 0, 15))
