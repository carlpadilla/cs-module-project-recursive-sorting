# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1

        else:
            merged_arr[k] = arrB[j]
            j += 1

        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_arr = len(arr) // 2
    left_arr = arr[:mid_arr]
    right_arr = arr[mid_arr:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    arr = merge(left_arr, right_arr)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

    left_start = start
    left_end = mid
    right_start = mid + 1
    right_end = end

    while left_start <= left_end and right_start <= right_end:
        if arr[left_start] <= arr[right_start]:
            left_start += 1
        else:
            temp = arr[right_start]
            index = right_start
            while index > left_start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[left_start] = temp
            left_start += 1
            left_end += 1
            right_start += 1

    return arr


def merge_sort_in_place(arr, l, r):

    mid = l + (r - l) // 2

    if len(arr) <= 1:
        return arr

    if r == l:
        return arr

    left_start = l
    left_end = mid
    right_start = mid + 1
    right_end = r

    merge_sort_in_place(arr, left_start, left_end)
    merge_sort_in_place(arr, right_start, right_end)

    merge_in_place(arr, left_start, left_end, right_end)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
