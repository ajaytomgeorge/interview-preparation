# Binary Search Problems

## 1. Basic Binary Search

### Problem Statement
Given a sorted array, find if a target value exists in the array.

### Solution

```python
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(input_list) - 1
target = 11

while start <= end:
    mid = (end + start) // 2
    print(mid)
    if input_list[mid] == target:
        print("found")
        break
    if input_list[mid] < target:
        start = mid + 1
    if input_list[mid] > target:
        end = mid - 1
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

---

## 2. Boolean Binary Search (First True Position)

### Problem Statement
Find the first occurrence of `True` in a boolean array containing `False` values followed by `True` values.

### Explanation
This is a variant of binary search that finds the leftmost position of a specific value. It's useful for finding the first occurrence of a condition.

### Solution

```python
input_data = [False, False, True, True, True]

start = 0 
end = len(input_data) - 1
last_true = 0

while start <= end:
    mid = (start + end) // 2
    if input_data[mid] == False:
        start = mid + 1
    if input_data[mid] == True:
        end = mid - 1
        last_true = mid

print(last_true)
```

**Use Case:** Finding the first position where a condition becomes true  
**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

---

## 3. Mock Binary Search with Syntax Issues

### Problem Statement
Demonstrates common binary search patterns with various edge cases.

### Solution

```python
# Standard binary search with target
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
end = len(input_list) - 1
target = 11

while low < end:
    mid = (low + end) // 2
    if target == input_list[mid]:
        print("found break")
        break
    if target < input_list[mid]:
        end = mid - 1
    if target > input_list[mid]:
        low = mid + 1

print("NOT FOUND")

# Rotated array search
input_list = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
low = 0
end = len(input_list) - 1
target = 3

while low < end:
    mid = (low + end) // 2
    if target == input_list[mid]:
        print("Found")
    if input_list[low] < input_list[mid]:
        if input_list[low] <= target < input_list[mid] :
            end = mid - 1
        else:
            low = mid + 1
    else:
        if input_list[mid] < target <= input_list[end] :
            low = mid + 1
        else:
            end = mid - 1
```

---

## 4. Search in Rotated Array

### Problem Statement
Find a target element in a rotated sorted array efficiently.

### Explanation
A rotated sorted array is split at a pivot point. We need to determine which half is sorted and then decide which way to search.

- If left half is sorted and target is in that range → search left
- Otherwise → search right
- If right half is sorted and target is in that range → search right
- Otherwise → search left

### Solution

```python
def search_rotated_array(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

**Key Insight:** Always identify which half is sorted first  
**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

---

## Key Takeaways

1. **Standard Binary Search:** Works on sorted arrays - O(log n) time
2. **Boundary Search:** Finding first/last occurrence of a value
3. **Rotated Array:** Determine which half is sorted, then apply logic
4. **Applicability:** Binary search is pseudo-polynomial and works best with bounded search spaces
