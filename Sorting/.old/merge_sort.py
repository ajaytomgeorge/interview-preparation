# worst O(nlogn)
#best Ω(nologn)
# Remeainder selection insertion and bubble sort has O(n^2) compelxity
# Invariant of Merge Sort
# Invariant (statement)

# Before merging, both subarrays are already sorted.

# Merge-step invariant

# At every step of merging, the output array contains the smallest elements so far in sorted order.

# Explanation (simple)

# Merge Sort divides the array until single elements remain

# Merging always combines two sorted arrays into one sorted array

# The invariant guarantees the final merged array is sorted
from ensurepip import version
def merge_sort(arr):
    if len(arr) > 1:
        # split array
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left_arr index
        j = 0  # right_arr index
        k = 0  # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # copy remaining elements of left_arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # copy remaining elements of right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# test
arr_test = [2, 3, 5, 1, 7,     4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)


non mutating versiondef merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]
