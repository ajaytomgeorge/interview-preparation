# Heap Problems

## 1. K Largest Elements

### Problem Statement

Find the K largest elements in an array.

### Approach

Maintain a **min-heap of size K**:
- If heap size exceeds K → pop the smallest
- Heap always stores K largest seen so far

### Why It Works

The smallest among K largest stays at the top and gets removed when a larger element appears.

### Implementation

```python
import heapq

def k_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap

# Example
print(k_largest([3, 2, 1, 5, 6, 4], 2))  # [5, 6]
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N log K) |
| **Space** | O(K) |

---

## 2. K Smallest Elements

### Problem Statement

Find the K smallest elements in an array.

### Approach

Use a **max-heap of size K**. Since Python has only min-heap, store negative values.

### Why It Works

The largest among the K smallest gets removed when a smaller number appears.

### Implementation

```python
import heapq

def k_smallest(nums, k):
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return sorted([-x for x in max_heap])

# Example
print(k_smallest([3, 2, 1, 5, 6, 4], 2))  # [1, 2]
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N log K) |
| **Space** | O(K) |

---

## 3. Top K Frequent Elements

### Problem Statement

Return the K most frequent elements from an array.

### Approach

1. Count frequency of all elements using a dictionary
2. Use a min-heap (by frequency) of size K
3. Keep heap size ≤ K

### Implementation

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]

# Example
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
```

**Heap stores:** (frequency, number)

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N log K) |
| **Space** | O(K) |

---

## 4. Find Median from Data Stream

### Problem Statement

Design a data structure supporting:
- `addNum(num)` → add a number
- `findMedian()` → return median

### Approach (Classic Two-Heap Solution)

- **Max-heap** → left half (store negative values)
- **Min-heap** → right half
- Balance sizes so difference ≤ 1

### Why Two Heaps?

Median is the middle element(s). By maintaining two balanced heaps:
- Left half maximum accessible in O(1)
- Right half minimum accessible in O(1)
- Can find median without sorting

### Key Insights: Size Balancing

#### Why the sizes must be balanced

To compute the median:

**Case 1: Odd count**
```
Median = top of the larger heap
Example: [1, 2, 3] → left has 2, right has 1 → median = left[0] = 2
```

**Case 2: Even count**
```
Median = average of both heap tops
Example: [1, 2, 3, 4] → left has 2, right has 2 → median = (2 + 3) / 2
```

**Therefore, we must ensure:**
```
len(left) == len(right)        (even total count)
or
len(left) == len(right) + 1    (odd total count, left has 1 extra)
```

**Left heap is allowed to have ONE extra element** to handle odd-length streams naturally.

#### Why the +1 specifically?

```python
if len(self.left) > len(self.right) + 1:
    # This means: "Left heap has more than one extra element — that's illegal"
```

We allow:
```
len(left) = len(right) + 1  ✅  (odd count)
```

We forbid:
```
len(left) ≥ len(right) + 2  ❌  (would be ambiguous)
```

**Why?** Because:
- Median should be either:
  - Top of left (odd count)
  - Average of both tops (even count)
- If left has 2+ extra elements, median becomes ambiguous and calculation fails

#### Balancing Logic

```python
# Balance sizes: left should have at most 1 more element
if len(self.left) > len(self.right) + 1:
    # Left has too many, move one to right
    heapq.heappush(self.right, -heapq.heappop(self.left))
elif len(self.right) > len(self.left):
    # Right has more, move one to left
    heapq.heappush(self.left, -heapq.heappop(self.right))
```

This ensures:
- `len(left) == len(right)` or `len(left) == len(right) + 1` always holds
- Median calculation is unambiguous and correct

### Implementation

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max heap (negative values)
        self.right = []  # min heap

    def addNum(self, num):
        # Add to left (max heap)
        heapq.heappush(self.left, -num)

        # Ensure ordering: all left ≤ all right
        if self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance sizes: left should have at most 1 more element
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2

# Usage
mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())  # 1.0
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2.0
```

### Complexity Analysis

| Operation | Time |
|-----------|------|
| **addNum** | O(log N) |
| **findMedian** | O(1) |

---

## 5. IPO / Maximize Capital

### Problem Statement

Given:
- Current capital (starting money)
- List of projects with capital requirement and profit
- Can complete at most `k` projects

**Goal:** Maximize total capital

**Rules:**
- Can only start a project if current capital ≥ project's capital requirement
- After completing project, capital increases by profit
- Can always choose to stop

### Approach

1. **Sort projects by capital requirement**
2. **For each of k projects to complete:**
   - Find all affordable projects (capital requirement ≤ current capital)
   - Add their profits to a max-heap
   - Pick the project with maximum profit
   - Update capital
3. **Continue until k projects done or no affordable projects**

### Why This Is a Greedy Problem

#### Key Point: Capital is NOT Consumed

This is crucial to understand:

- **Capital is a constraint, not a cost**
- It represents an eligibility/qualification threshold
- Capital is **NOT spent** when doing a project
- After completing a project, capital **only increases** by profit

**Think of it like:**
```
You need at least $10,000 in savings to start a business
But you don't lose that $10,000 — you just need to have it
After completion: you gain profit
Capital only increases
```

#### Why Greedy Works

With the property that `capital_new = capital_old + profit`:

1. **At each step,** pick the most profitable affordable project
2. **This choice is locally optimal** → increases capital for next iteration
3. **Local optima = global optima** ✅

The greedy strategy: **maximize capital gain at each step** leads to maximum final capital.

#### Why Greedy Would Fail If Capital Were Consumed

If capital were consumed: `capital_new = capital_old - requirement + profit`

Then it would become:
- A knapsack / scheduling problem
- Possibly NP-hard
- **Greedy would fail**

**Example where consuming capital breaks greedy:**

```
capital = 10
Project A: requirement=10, profit=1
Project B: requirement=5, profit=6

Greedy picks A first (affordable) → capital = 1
Can't afford B (needs 5) → total = 1 ❌

Optimal: Pick B first → capital = 11
Then pick A → capital = 12 ✅
```

But with non-consumed capital, greedy always works because we can always do a profitable project once we have enough capital.

### Implementation

```python
import heapq

def findMaximizedCapital(k, initial_capital, profits, capital):
    # Sort projects by capital requirement
    projects = list(zip(capital, profits))
    projects.sort()
    
    current_capital = initial_capital
    max_heap = []  # Store negative profits (for max heap)
    i = 0
    
    for _ in range(k):
        # Add all affordable projects to heap
        while i < len(projects) and projects[i][0] <= current_capital:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1
        
        # If no affordable projects, stop
        if not max_heap:
            break
        
        # Do the most profitable project
        current_capital += -heapq.heappop(max_heap)
    
    return current_capital

# Example
project_to_complete = 3
current_capital = 0
profits = [1, 2, 3]
capitals = [0, 1, 2]

result = findMaximizedCapital(project_to_complete, current_capital, profits, capitals)
print(result)  # Output: 6
# Explanation: Complete all 3 projects: 0 → 1 → 3 → 6
```

### Example Walkthrough

```
k=3, initial_capital=0
Projects: [(0,1), (1,2), (2,3)]

Iteration 1:
  current_capital = 0
  affordable: (0,1)
  max_heap = [-1]
  pick profit 1 → current_capital = 1

Iteration 2:
  current_capital = 1
  affordable: (1,2)
  max_heap = [-2]
  pick profit 2 → current_capital = 3

Iteration 3:
  current_capital = 3
  affordable: (2,3)
  max_heap = [-3]
  pick profit 3 → current_capital = 6

Result: 6
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N log N + k log N) - Sort + k heap operations |
| **Space** | O(N) for heap and sorted array |

---

## 6. K Closest Points to Origin

### Problem Statement

Find K closest points to origin (0, 0).

### Approach

1. Use a **max-heap of size K** (ordered by distance)
2. For each point:
   - Calculate distance from origin
   - Add to heap
   - If heap exceeds K, remove farthest point
3. Return remaining K points

### Implementation

```python
import heapq

def k_closest(points, k):
    max_heap = []

    for x, y in points:
        dist = x*x + y*y  # No need for sqrt (ordering is same)
        heapq.heappush(max_heap, (-dist, (x, y)))
        
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for dist, point in max_heap]

# Example
print(k_closest([[1,3], [−2,2], [2,−2], [0,1]], 2))
# Output: [[2,-2], [0,1]] or similar
```

### Why Not Use sqrt()?

Distance ordering is the same as distance² ordering. Since sqrt is expensive, we skip it.

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N log K) |
| **Space** | O(K) |

---

## Heap Strategy Summary

| Problem | Heap Type | Purpose |
|---------|-----------|---------|
| **K Largest** | Min-heap size K | Keep K largest, discard smallest |
| **K Smallest** | Max-heap size K | Keep K smallest, discard largest |
| **K Frequent** | Min-heap by frequency | Same as K Largest |
| **Median Stream** | Two heaps | Balanced split |
| **IPO** | Max-heap by profit | Greedy: always pick best |
| **K Closest** | Max-heap by distance | Keep K closest |

### When to Use Min-Heap vs Max-Heap

- **Min-heap of size K:** Find K largest (top element is smallest of them)
- **Max-heap of size K:** Find K smallest (top element is largest of them)

This is counterintuitive but efficient - we maintain opposite heap type to efficiently remove "worst" element.

---

## Interview Tips

1. **Heap Property:** Always understand what heap stores (frequency, profit, distance, etc.)
2. **Size Constraint:** Always check if heap exceeds K before popping
3. **Negation for Max-Heap:** Python heapq is min-heap, so negate for max behavior
4. **Complexity:** Recognize O(N log K) pattern for K-element heap problems
5. **Real-world:** Heaps used in OS scheduling, network routing, priority queues
