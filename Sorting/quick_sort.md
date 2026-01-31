# Quick Sort - Complete Guide

## Important Notes

- **Pivot selection is critical** - choices include first, middle, last element, or median of 3 small samples
- **Invariant of Quick Sort** - After partitioning around a pivot, the pivot is in its final sorted position, and all elements to the left are ≤ pivot, all elements to the right are > pivot
- **Partition invariant (Lomuto)** - During partitioning:
  - Left part: ≤ pivot
  - Middle: > pivot
  - Right part: unknown

---

## Quick Sort — Best Case

### Example Array
```
[4, 2, 6, 1, 3, 5, 7]
```

(or any array where the pivot always splits the array roughly in half)

### Why This is Best Case

- Pivot chosen ends up near the middle
- Each partition divides the array into two equal halves
- Recursion depth is log n

### Time Complexity
**O(n log n)**

---

## Quick Sort — Worst Case

### Example Arrays
```
[1, 2, 3, 4, 5, 6, 7]   (already sorted)
[7, 6, 5, 4, 3, 2, 1]   (reverse sorted)
```

(when pivot is chosen as first or last element)

### Why This is Worst Case

- Pivot is always the smallest or largest
- One subarray is empty, the other has size n−1
- Recursion depth becomes n

### Time Complexity
**O(n²)**

---

## One-Line Exam Summary (Very Important)

**"Best case: pivot divides array into equal halves → O(n log n)"**  
**"Worst case: pivot always smallest or largest → O(n²)"**

---

## Tip Examiners Love

**"Worst case occurs when the array is already sorted and the pivot is chosen as the first or last element."**

---

## Implementation 1: Lomuto Partition Scheme

```python
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


# Example
arr = [2, 8, 9, 3, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [2, 3, 5, 8, 9]
```

### How Lomuto Partition Works

1. Choose last element as pivot
2. Maintain index `i` of the last element in left partition
3. Scan through array:
   - If element ≤ pivot: increment i, swap with element at i
   - Otherwise: continue
4. Place pivot in final position by swapping with `arr[i+1]`
5. Return pivot index

---

## Implementation 2: Hoare Partition Scheme (Middle Element)

```python
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


# Example
arr = [2, 8, 9, 3, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [2, 3, 5, 8, 9]
```

### How Hoare Partition Works

1. Choose middle element as pivot
2. Use two pointers `i` and `j`:
   - `i` starts at low, moves right until finding element > pivot
   - `j` starts at high, moves left until finding element < pivot
3. Swap elements when both conditions met
4. Continue until pointers cross
5. Return crossing point

---

## Complexity Analysis

| Case | Time | Space |
|------|------|-------|
| **Best** | O(n log n) | O(log n) recursion |
| **Average** | O(n log n) | O(log n) recursion |
| **Worst** | O(n²) | O(n) recursion |
| **Space** | — | O(log n) to O(n) |

---

## Key Points for Interview

1. **Partition is the core** - correctly implemented partition determines correctness
2. **In-place sorting** - O(log n) to O(n) space (recursion stack only)
3. **Not stable** - equal elements may not maintain original order
4. **Quickest average case** - why it's called "quick"
5. **Cache-friendly** - good locality of reference
