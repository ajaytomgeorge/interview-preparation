# Heap Sort - Complete Analysis

## Important Discussion: Heap Operations vs Heapsort

### Why Heap Operations are O(log n)?

A binary heap is a complete binary tree.

**Height of the tree:**
$$\log_2 n$$

**So:**
- `push` (sift up) → worst case climbs the height → O(log n)
- `pop` (sift down) → worst case descends the height → O(log n)

---

## Heapsort Complexity (Important Correction!)

Many people think heapsort is:
```
n inserts × log n = n log n
```

But that's **not** how heapsort is actually done.

### Actual Heapsort Steps

**Step 1: Build heap — O(n)** ❗
```
heapify(array)
```

**Why?** Most nodes are near the bottom. Very few nodes can move log n levels.  
The total cost sums to **O(n)**.

(This is a classic "feels like log n but isn't" result.)

**Step 2: Extract max/min n times**

Each extraction:
- swap root with last element → O(1)
- sift down → O(log n)

**Total:** n × log n

### Final Complexity

$$\text{Heapsort} = O(n) + O(n \log n) = O(n \log n)$$

---

## How Heap Sort Differs From Merge Sort

| Algorithm | Why n log n | Reason |
|-----------|-----------|--------|
| **Merge sort** | log n levels × n work per level | Recursion depth × merge work |
| **Heap sort** | n removals × log n per removal | n operations × heap height |
| **Quicksort (avg)** | log n depth × n partition work | Recursion depth × partition work |

---

## Memory & Stability Tradeoff

| Property | Merge Sort | Heap Sort |
|----------|-----------|----------|
| **Time** | n log n | n log n |
| **Extra memory** | O(n) | O(1) |
| **Stable** | ✅ Yes | ❌ No |
| **Cache-friendly** | ✅ Yes | ❌ No |
| **Worst case** | Always n log n | Always n log n |

---

## Method A vs Method B: Building a Heap

### ❌ Method A: Insert Elements One By One (NOT actual heapsort)

```python
for each element:
    heap_push(x)   → O(log n)
```

**Cost of building:** n × log n = n log n  
**Cost of sorting:** n × log n = n log n  
**Total:** n log n + n log n = 2n log n → **O(n log n)** ✔️ Correct, but inefficient

### ✅ Method B: Heapify (Actual Heapsort - Recommended)

```
build heap in-place (bottom-up)
```

**Cost:** O(n)  
**Cost of extracting:** n × log n = n log n  
**Total:** **O(n log n)** ✔️ More efficient

---

## Two Ways to Build Heap

| Approach | Time | Use Case |
|----------|------|----------|
| **Bottom-up (in-place)** | O(n) | Heapsort (actual) |
| **Top-down (insert one by one)** | O(n log n) | Priority queue insertions |

---

## Python Implementation

```python
def heapify(arr, n, i):
    """Maintain heap property by moving element down"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """Sort array using heap sort"""
    n = len(arr)

    # Step 1: Build max heap (bottom-up) - O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap - O(n log n)
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        heapify(arr, i, 0)

    return arr


# Test
arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))  # Output: [5, 6, 7, 11, 12, 13]
```

---

## Complexity Analysis

| Case | Time | Space |
|------|------|-------|
| **Best** | O(n log n) | O(1) |
| **Average** | O(n log n) | O(1) |
| **Worst** | O(n log n) | O(1) |

---

## Key Conceptual Insights

1. **Heapify is O(n)** - not n log n! This is crucial.
2. **Extraction is n log n** - removing n times, each costs log n
3. **Total is n log n** - because O(n) + O(n log n) = O(n log n)
4. **Not stable** - equal elements lose original order
5. **In-place** - no extra array needed (unlike merge sort)

---

## Mental Model

**Heapsort:** "Build a tree maintaining order, then extract roots one by one"

Compare with:
- **Merge sort:** "Split space, then merge linearly"
- **Quicksort:** "Partition and pray"
