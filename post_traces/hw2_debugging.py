'''
Mergesort using a random set of inputs
'''
import rand


def merge_sort(arr):
    '''
    Mergesort - recursive call
    '''
    if len(arr) == 1:
        return arr
    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    '''
    Combines elements in a sorted order
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1
    return merge_arr


arr_inp = rand.random_array([None] * 20)
arr_out = merge_sort(arr_inp)

print(arr_out)