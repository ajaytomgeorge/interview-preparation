# Hashmap Problems

## Two Sum Problem

### Problem Statement

Given an array of integers `nums` and an integer `target`, find the indices of the two numbers that add up to the target.

**Constraint:** Each element is used at most once.

### Examples

| Input Array | Target | Output |
|-------------|--------|--------|
| `[2, 3, 4, 5, 8, 9]` | `7` | `(0, 3)` or `(1, 2)` |
| `[2, 7, 11, 15]` | `9` | `(0, 1)` |

### Approach: Hash Map (One Pass)

Use a dictionary to store values we've seen. For each element, check if its complement exists in the map.

**Key Idea:**
- For target = 7 and current value = 2, we need complement = 5
- If we've already seen 5, we found our pair!

### Algorithm

1. Create an empty dictionary `num_tracker`
2. Iterate through the array:
   - Calculate `complement = target - value`
   - Check if `complement` exists in `num_tracker`
     - If yes → return indices
     - If no → add current value to `num_tracker`

### Python Solution

```python
def two_sum(nums, target):
    num_tracker = {}
    
    for idx, value in enumerate(nums):
        complement = target - value
        
        if complement in num_tracker:
            return (num_tracker[complement], idx)
        
        num_tracker[value] = idx
    
    return None

# Example
a = [2, 3, 4, 5, 8, 9]
target = 7

result = two_sum(a, target)
print(result)  # Output: (0, 3) or indices where values sum to target
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N) - Single pass through array |
| **Space** | O(N) - Hash map stores up to N elements |

### Why Hash Map is Better Than Brute Force

#### Brute Force (Nested Loops)
```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

# Time Complexity: O(N²)
# Space Complexity: O(1)
```

#### Hash Map Approach (This Solution)
```python
# Time Complexity: O(N)
# Space Complexity: O(N)
```

**Trade-off:** We use extra space to achieve better time complexity ✅

### Key Insights

1. **Hash Map Lookup:** Dictionary provides O(1) average lookup time
2. **Complement Strategy:** Instead of checking all pairs, we look for specific complements
3. **One Pass:** We solve it in a single iteration through the array
4. **Index Tracking:** Store indices, not just values, for accurate output

### Follow-up Questions

1. **What if multiple solutions exist?** Return all pairs or the first pair
2. **What if no solution exists?** Return `None` or `[-1, -1]`
3. **What about duplicate values in array?** Use index as secondary key in hash map
4. **Return values instead of indices?** Modify to store `num_tracker[value] = value`

### Edge Cases

```python
# Example 1: Two zeros sum to target 0
nums = [0, 0]
target = 0
# Output: (0, 1) ✅

# Example 2: Array with duplicates
nums = [3, 2, 4]
target = 6
# Output: (1, 2) - indices of 2 and 4

# Example 3: No solution
nums = [1, 2, 3]
target = 10
# Output: None
```

### Real-World Applications

- **E-commerce:** Finding products with specific combined price
- **Finance:** Finding transactions that match a total
- **Data Matching:** Pairing records from two datasets

---

## Related Problems to Practice

1. **3Sum** - Find three numbers that sum to target
2. **4Sum** - Find four numbers that sum to target
3. **Two Sum II** - Input array is sorted
4. **Two Sum III** - Design a data structure with `add()` and `find()` methods
