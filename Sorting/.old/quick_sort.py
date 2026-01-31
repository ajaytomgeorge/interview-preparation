# pivot is the important
# some first middle and last element, some use medium of of 3 small sample


# Lomudo Parition

# Invariant of Quick Sort
# Invariant (statement)

# After partitioning around a pivot, the pivot is in its final sorted position,
# and all elements to the left are ≤ pivot, all elements to the right are > pivot.

# Explanation (simple)

# Partition rearranges the array so the pivot is correctly placed

# Quick Sort then recursively sorts the left and right subarrays

# The invariant ensures correctness at every recursive step

# Partition invariant (Lomuto)

# During partitioning:

# Left part  ≤ pivot
# Middle     > pivot
# Right part unknown


Quick Sort — Best Case
Example array
[4, 2, 6, 1, 3, 5, 7]


(or any array where the pivot always splits the array roughly in half)

Why this is best case

Pivot chosen ends up near the middle

Each partition divides the array into two equal halves

Recursion depth is log n

Time Complexity
O(n log n)

Quick Sort — Worst Case
Example arrays
[1, 2, 3, 4, 5, 6, 7]   (already sorted)


or

[7, 6, 5, 4, 3, 2, 1]   (reverse sorted)


(when pivot is chosen as first or last element)

Why this is worst case

Pivot is always the smallest or largest

One subarray is empty, the other has size n−1

Recursion depth becomes n

Time Complexity
O(n²)

One-line exam summary (very important)

Best case: pivot divides array into equal halves → O(n log n)
Worst case: pivot always smallest or largest → O(n²)

Tip examiners love

Mention this line if you can:

“Worst case occurs when the array is already sorted and the pivot is chosen as the first or last element.”



def partition(arr, low, high):
    pivot = arr[high]          # last element as pivot
    i = low - 1                # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1               # pivot index


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)   # left subarray
        quick_sort(arr, pi + 1, high)  # right subarray


arr = [2, 8, 9, 3, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)\


    Middle element
    ✅ Quick Sort (Middle element as pivot — Hoare Partition)
def partition(arr, low, high):
    pivot = arr[(low + high) // 2]   # middle element as pivot
    i = low - 1
    j = high + 1

    while True:
        # move i to the right
        i += 1
        while arr[i] < pivot:
            i += 1

        # move j to the left
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # pointers crossed
        if i >= j:
            return j

        # swap out-of-place elements
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)