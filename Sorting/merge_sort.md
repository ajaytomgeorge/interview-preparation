# Merge Sort - Complete Guide

## Important Notes

- **Worst case:** O(n log n)
- **Best case:** Ω(n log n)
- **Remainder:** Insertion, bubble sort, and selection sort have O(n²) complexity

## Invariant of Merge Sort

### Statement
Before merging, both subarrays are already sorted.

### Merge-Step Invariant
At every step of merging, the output array contains the smallest elements so far in sorted order.

### Explanation
1. Merge Sort divides the array until single elements remain
2. Merging always combines two sorted arrays into one sorted array
3. The invariant guarantees the final merged array is sorted

---

## Python Implementation (Mutating Version)

```python
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


# Test
arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)  # Output: [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
```

---

## Python Implementation (Non-Mutating Version)

```python
def merge_sort(arr):
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


# Test
arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
print(arr)  # Original unchanged: [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
```

---

## Complexity Analysis

| Case | Time | Space |
|------|------|-------|
| **Best** | O(n log n) | O(n) |
| **Average** | O(n log n) | O(n) |
| **Worst** | O(n log n) | O(n) |

### Why O(n log n)?

**Recursion depth:** log n levels

**Work per level:** n operations (comparing and merging)

**Total:** log n × n = **O(n log n)**

---

## Key Characteristics

| Property | Value |
|----------|-------|
| **Stable** | ✅ Yes |
| **In-place** | ❌ No (needs O(n) extra space) |
| **Adaptive** | ❌ No (always n log n) |
| **Comparison-based** | ✅ Yes |

---

## Comparison with Other Sorts

| Algorithm | Time | Space | Stable | In-Place |
|-----------|------|-------|--------|----------|
| **Merge Sort** | O(n log n) | O(n) | ✅ Yes | ❌ No |
| **Quick Sort** | O(n log n) avg | O(log n) | ❌ No | ✅ Yes |
| **Heap Sort** | O(n log n) | O(1) | ❌ No | ✅ Yes |
| **Bubble Sort** | O(n²) | O(1) | ✅ Yes | ✅ Yes |
| **Insertion Sort** | O(n²) | O(1) | ✅ Yes | ✅ Yes |

---

## Step-by-Step Example

### Input
```
[2, 3, 5, 1]
```

### Divide Phase
```
[2, 3, 5, 1]
    ↓
[2, 3]    [5, 1]
    ↓        ↓
[2] [3]  [5] [1]
```

### Merge Phase
```
[2] [3]  [5] [1]
  ↓        ↓
[2, 3]  [1, 5]
    ↓
[1, 2, 3, 5]
```

---

## When to Use Merge Sort

✅ **Use Merge Sort when:**
- Stability is required
- Guaranteed O(n log n) is needed
- Working with linked lists (no random access)
- External sorting (data too large for memory)

❌ **Avoid Merge Sort when:**
- Space is limited (O(n) extra space is expensive)
- In-place sorting is required
- Average case is more important than worst case

---

## Mental Model

**Merge Sort:** "Divide and conquer: split into halves, sort recursively, then merge sorted halves."
