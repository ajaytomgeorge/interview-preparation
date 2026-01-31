# Greedy Algorithms

Collection of greedy algorithm problems where locally optimal choices lead to global optima.

## When Does Greedy Work?

### Questions to Ask

| Question | Property |
|----------|----------|
| Can I make a locally best choice now without reconsidering it later? | Greedy choice property |
| Can the remaining problem be solved optimally independent of what I chose? | Optimal substructure |
| Can I prove by contradiction that choosing differently would never improve the result? | Greedy correctness proof |

### Tips & Heuristics

- **Fractions allowed** → greedy often works (like fractional knapsack)
- **Order matters** → greedy may work (like interval scheduling)
- **Discrete choices/combinatorial** → greedy may fail (like 0/1 knapsack, non-canonical coin change)

### Quick Reference: Greedy Success Rate

| Problem | Greedy Works? | Why/Why Not |
|---------|---------------|-----------|
| **Fractional Knapsack** | ✅ | Value/weight ratio → locally optimal leads to global |
| **0/1 Knapsack** | ❌ | Locally best ratio may block higher total value |
| **Activity Selection** | ✅ | Earliest finish leaves more room for future |
| **Coin Change (canonical)** | ✅ | Largest coin first works |
| **Coin Change (non-canonical)** | ❌ | Largest coin first may fail |
| **Jump Game** | ✅ | Tracking farthest reachable index works |
| **Gas Station** | ✅ | Total sufficiency + restart strategy |
| **Job Sequencing** | ✅ | Highest profit first, schedule late |

### Exam Shortcut

**Greedy works when:** You can pick the best option now and the rest of the problem can still be solved optimally.

**Otherwise:** Use DP or backtracking.

---

## 1. Activity Selection

### Problem Statement

Given n activities with start and end times, select the **maximum number of non-overlapping activities**.

### Examples

```
Activities: [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]

Selected: [(1,4), (5,7), (8,11), (12,14)]
Count: 4 activities
```

### Greedy Approach

**Sort by end time, then always pick the activity that ends earliest:**
- This leaves maximum room for future activities
- Locally optimal choice (earliest end) → globally optimal

### Algorithm

```
1. Sort activities by end time
2. Select first activity
3. For each remaining activity:
   - If start time ≥ previous end time:
     - Select this activity
     - Update previous end time
4. Return selected activities
```

### Implementation

```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end:
            selected.append(activities[i])
            last_end = end
    
    return selected

# Example
activities = [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]
print(len(activity_selection(activities)))  # 4
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n log n) - sorting dominates |
| **Space** | O(1) or O(n) for result |

---

## 2. Jump Game

### Problem Statement

Given array where each element is max jump length, determine if you can reach the last index.

### Examples

```
Input:  [2, 3, 1, 1, 4]
Output: True (jump 1 step to index 1, then 3 steps to index 4)

Input:  [3, 2, 1, 0, 4]
Output: False (always reach index 3 with 0, can't jump further)
```

### Greedy Approach

Track the **maximum index reachable so far**:
- If current index > max reachable → impossible
- Update max reachable as we go
- If max reachable ≥ last index → we can reach it

### Implementation

```python
def canJump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        # Current index unreachable
        if i > max_reach:
            return False
        
        # Update max reachable
        max_reach = max(max_reach, i + nums[i])
        
        # Can reach end
        if max_reach >= len(nums) - 1:
            return True
    
    return max_reach >= len(nums) - 1

# Examples
print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([3, 2, 1, 0, 4]))  # False
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - single pass |
| **Space** | O(1) |

### Why Greedy Works

Greedy choice: **Never jump less than we can**. By maximizing reach at each step, we make it as likely as possible to reach the end.

---

## 3. Coin Change (Greedy Failed)

### Problem Statement

Given coin denominations, find **minimum coins** for amount.

### Why Greedy Fails

```
Coins: [1, 3, 4]
Amount: 6

Greedy: Pick 4 (max) → need 2×1 → total 3 coins
Optimal: 3 + 3 → total 2 coins ✓
```

**Greedy doesn't always work!** Use **Dynamic Programming** instead (see DP folder).

---

## 4. Gas Station

### Problem Statement

Given gas and cost at each station, find **starting station to complete circuit**.
- Can only drive if current gas ≥ cost
- Each station gives gas, then costs gas to reach next

### Examples

```
Gas:  [1, 2, 3, 4, 5]
Cost: [3, 4, 5, 1, 2]

Output: 3 (start at index 3)
```

### Greedy Approach

**If total gas ≥ total cost, a solution exists.** Find it greedily:
- Track current gas
- If we can't reach next station, start from next station
- The first position where we reset is the answer

### Implementation

```python
def canCompleteCircuit(gas, cost):
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    # No solution if insufficient gas
    if total_gas < total_cost:
        return -1
    
    current_gas = 0
    start = 0
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        # Can't reach next station from current start
        if current_gas < 0:
            start = i + 1
            current_gas = 0
    
    return start

# Example
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))  # 3
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## 5. Job Sequencing to Maximize Profit

### Problem Statement

Given jobs with deadline and profit, select jobs to **maximize profit** where each job takes 1 unit time and can't miss deadline.

### Examples

```
Jobs: [(10,5), (40,4), (30,3), (20,2)]  # (profit, deadline)

Selected: Job1 (profit 40, deadline 4), Job3 (profit 20, deadline 2)
Profit: 60
```

### Greedy Approach

1. Sort jobs by profit (descending)
2. For each job, schedule it as late as possible before deadline
3. If slot available → schedule it

### Implementation

```python
def jobSequencing(jobs):
    # Sort by profit descending
    jobs.sort(key=lambda x: x[0], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    
    # -1 means slot is empty
    schedule = [-1] * (max_deadline + 1)
    
    total_profit = 0
    
    for profit, deadline in jobs:
        # Try to schedule at deadline or earlier
        for slot in range(deadline, 0, -1):
            if schedule[slot] == -1:
                schedule[slot] = (profit, deadline)
                total_profit += profit
                break
    
    return total_profit

# Example
jobs = [(10,5), (40,4), (30,3), (20,2)]
print(jobSequencing(jobs))  # Profit sum
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n²) in worst case |
| **Space** | O(n) for schedule |

---

## 6. Huffman Coding

### Problem Statement

Build optimal **variable-length prefix codes** for characters based on frequency, minimizing average code length.

### Concept

- Frequent characters → shorter codes
- Rare characters → longer codes
- No code is prefix of another

### Example

```
Characters: a(5), b(9), c(12), d(13), e(16), f(45)

Huffman Tree:
                    (100)
                    /     \
                f:45       (55)
                           /   \
                       (25)     (30)
                       /  \      /   \
                  c:12   d:13  (14)  e:16
                                / \
                           a:5     b:9

Final Huffman Tree with Codes:
                    (100)
                    /     \
               f:45(0)     (55)(1)
                           /     \
                      (25)(10)    (30)(11)
                      /   \        /    \
                 c:12(100) d:13(101) (14)(110) e:16(111)
                                    /    \
                               a:5(1100) b:9(1101)
```

### Algorithm

1. Create leaf node for each character
2. While more than one node:
   - Pick two nodes with minimum frequency
   - Create parent node with sum frequency
   - Add parent back to queue
3. Root is top of final tree

### Implementation

```python
import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffmanCoding(chars, freqs):
    heap = [Node(freq, char) for char, freq in zip(chars, freqs)]
    heapq.heapify(heap)
    
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, parent)
    
    root = heap[0]
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=""):
        if node.char:
            codes[node.char] = code
        else:
            if node.left:
                generate_codes(node.left, code + "0")
            if node.right:
                generate_codes(node.right, code + "1")
    
    generate_codes(root)
    return codes

# Example
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freqs = [5, 9, 12, 13, 16, 45]
codes = huffmanCoding(chars, freqs)
print(codes)  # Huffman codes
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n log n) - heap operations |
| **Space** | O(n) - tree nodes |

---

## 7. Knapsack (Fractional)

### Problem Statement

Pack items with weights and values into bag of capacity W, allowing **fractions of items**.

**Note:** This is fractional knapsack (greedy works). For 0/1 knapsack, use DP.

### Greedy Approach

Greedily pick items with **highest value-to-weight ratio**:

```python
def fractionalKnapsack(weight, value, capacity):
    # Calculate ratio and sort
    items = [(value[i]/weight[i], weight[i], value[i]) for i in range(len(weight))]
    items.sort(reverse=True)
    
    total_value = 0
    remaining = capacity
    
    for ratio, w, v in items:
        if w <= remaining:
            total_value += v
            remaining -= w
        else:
            # Take fraction
            total_value += ratio * remaining
            break
    
    return total_value
```

---

## When to Use Greedy

| Problem | Greedy | Reason |
|---------|--------|--------|
| **Activity Selection** | ✅ | Earliest end optimal |
| **Jump Game** | ✅ | Max reach at each step |
| **Gas Station** | ✅ | Total sufficiency + restart |
| **Job Scheduling** | ✅ | Highest profit first |
| **Fractional Knapsack** | ✅ | Best ratio prioritized |
| **Coin Change** | ❌ | Counterexample exists |
| **0/1 Knapsack** | ❌ | Use DP instead |

---

## Key Greedy Insights

1. **Sort first:** Usually need to sort by some criterion
2. **Local optimal:** Make best choice at each step
3. **Proof needed:** Verify greedy actually works for problem
4. **Counterexamples:** Always try to break the greedy approach
5. **Alternative:** If greedy fails, try DP or backtracking

---

## Related Problems

1. **Activity Selection** ✓
2. **Jump Game** ✓
3. **Gas Station** ✓
4. **Job Sequencing** ✓
5. **Huffman Coding** ✓
6. **Interval Scheduling** - Similar to activity selection
7. **Minimum Platforms** - Train station scheduling
8. **Fractional Knapsack** ✓
