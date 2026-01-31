# Monotonic Stack Problems

## Next Greater Element (NGE)

### Problem Statement

Given an array, for each element, find the **first greater element to its right**.

If none exists → return `-1`.

### Examples

| Input | Output |
|-------|--------|
| `[2,1,3]` | `[3,3,-1]` |
| `[4,5,2,10]` | `[5,10,10,-1]` |
| `[1,2,3,4]` | `[2,3,4,-1]` |

### What is a Monotonic Stack?

A monotonic stack is a stack that keeps elements in a monotone order:

- **Increasing stack** → elements in increasing order from bottom → top
- **Decreasing stack** → elements in decreasing order from bottom → top

**Why use it?**
- Efficiently find Next Greater / Next Smaller elements
- Avoids O(N²) nested loops → solves in O(N)
- When current element breaks monotone order, pop from stack → current element is the answer

### Algorithm

**Initialize:**
```python
stack = []              # stores indices
result = [-1] * len(arr)  # default -1
```

**Traverse array with index i:**
```
While stack is not empty and arr[i] > arr[stack[-1]]:
  - Pop index idx = stack.pop()
  - result[idx] = arr[i]  ← current element is NGE for arr[idx]
  
Push current index i onto stack
```

**After traversal:** remaining indices in stack have NGE = -1

### Python Implementation

```python
def nextGreaterElement(arr):
    stack = []
    result = [-1] * len(arr)

    for i, val in enumerate(arr):
        while stack and val > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)

    return result

# Examples
print(nextGreaterElement([2, 1, 3]))      # [3, 3, -1]
print(nextGreaterElement([4, 5, 2, 10]))  # [5, 10, 10, -1]
```

### Dry Run Example: `[2, 1, 3]`

| Step | Element | Stack | Result | Explanation |
|------|---------|-------|--------|-------------|
| 0 | 2 | [0] | [-1,-1,-1] | 2 pushed, waiting for NGE |
| 1 | 1 | [0,1] | [-1,-1,-1] | 1 pushed, waiting for NGE |
| 2 | 3 | [2] | [3,3,-1] | 3 > 1 → result[1]=3, pop 1; 3>2 → result[0]=3, pop 0 |
| End | - | [2] | [3,3,-1] | Index 2 has no NGE → -1 |

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N) - each element pushed/popped at most once |
| **Space** | O(N) - stack stores indices |

**Why O(N)?**
- Each element is pushed once: O(N)
- Each element is popped at most once: O(N)
- Total: O(N) not O(N²)

### Why This Beats Nested Loop

#### ❌ Brute Force (Nested Loops)
```python
def nextGreaterElement_brute(arr):
    result = []
    for i in range(len(arr)):
        found = False
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                result.append(arr[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

# Time: O(N²)
# Space: O(1)
```

#### ✅ Monotonic Stack
```python
# Time: O(N)
# Space: O(N) for stack, but worth it!
```

### Variations

#### 1. **Next Smaller Element**
```python
def nextSmallerElement(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):  # Reverse direction
        while stack and arr[stack[-1]] > arr[i]:  # Change > to <
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result
```

#### 2. **Previous Greater Element**
```python
def previousGreaterElement(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:  # Change direction
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result
```

#### 3. **Circular Array**
For circular arrays, iterate twice:
```python
def nextGreaterCircular(arr):
    n = len(arr)
    stack = []
    result = [-1] * n

    for i in range(2 * n):
        while stack and arr[i % n] > arr[stack[-1] % n]:
            idx = stack.pop() % n
            result[idx] = arr[i % n]
        stack.append(i % n)

    return result
```

### Interview Tips

1. **Key Insight:** Monotonic stack reduces O(N²) to O(N)
2. **Index vs Value:** Store indices in stack, not values (need to update result array)
3. **When to Pop:** Only pop when current element breaks monotone order
4. **What Gets Assigned:** Popped element gets current element as its answer
5. **Edge Cases:**
   - All decreasing: all get -1
   - All increasing: last gets -1, others get next element
   - Empty array: return empty result

### One-Line Explanation

"A monotonic stack keeps candidates in decreasing order. For NGE, pop smaller elements when a bigger number comes, assign the popped elements their NGE, and push the current index."

### Real-World Applications

- **Stock Span Problem:** Days until price goes higher
- **Largest Rectangle:** Finding larger bar to the right
- **Trapping Rain Water:** Finding next higher elevation
- **Building Visibility:** Can building see next taller building
