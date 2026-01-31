# Coding Round Practice Questions - Complete Guide

This is a comprehensive collection of **LeetCode-style coding problems** organized by data structures and algorithms, with detailed explanations, code solutions, and complexity analysis.

## 📚 Table of Contents

### Core Data Structures & Algorithms

1. **[Binary Search](binary_search/)** - Searching in sorted arrays
2. **[Hash Maps](Hashmap/)** - Two sum and efficient lookups
3. **[Stacks](stacks/)** - Valid parentheses, decode strings, next greater element
4. **[Dynamic Programming](DP/)** - 0/1 Knapsack, minimum coins
5. **[Graphs](Graphs/)** - BFS, DFS graph traversal
6. **[Trees](trees/)** - BST validation, tree inversion
7. **[Sliding Window](Sliding%20Window/)** - Substring problems with fixed/dynamic windows
8. **[Pointers](Pointers/)** - Two-pointer techniques, anagrams, linked lists
9. **[Heaps](Heaps/)** - K-largest elements, median stream, IPO
10. **[Tries](Trie/)** - Prefix trees, word search in 2D board

---

## 📂 Directory Structure

```
coding-problems/
├── binary_search/
│   ├── README.md              # Sorted array searches
│   ├── binary_search.py
│   ├── boolean_binary_search.py
│   └── ...
│
├── stacks/
│   ├── README.md              # Complete stack problems
│   ├── valid_paranthesis.py
│   ├── DecodeString.py
│   ├── monotonic_stacks/
│   │   └── next_greater_element.py
│   └── ...
│
├── DP/
│   ├── README.md              # Dynamic programming
│   ├── 01knapsack.py
│   └── minimum_coins.py
│
├── Graphs/
│   ├── README.md              # Graph traversal
│   ├── bfs.py
│   ├── dfs.py
│   └── ...
│
├── Trees/
│   ├── README.md              # Binary tree problems
│   ├── binaryTreeisBSTcheck.py
│   └── ...
│
└── [More folders...]
```

---

## 🎯 Topics Overview

### Binary Search
- Standard binary search on sorted arrays
- First true position detection
- Rotated array search
- Time: O(log n) | Space: O(1)

### Hash Maps
- **Two Sum Problem** - Find two numbers summing to target
- Efficient O(1) lookups for complement matching
- Time: O(n) | Space: O(n)

### Stacks
- **Valid Parentheses** - Check bracket matching
- **Decode String** - Decode encoded patterns with counts
- **Longest Valid Parentheses** - Maximum valid substring
- **Undo/Redo System** - Dual stack state management
- **Redundant Brackets** - Check unnecessary brackets
- Time: O(n) | Space: O(n)

### Monotonic Stacks
- **Next Greater Element** - Find next larger element to right
- Reduces nested loop O(n²) to O(n)
- Time: O(n) | Space: O(n)

### Dynamic Programming
- **0/1 Knapsack** - Maximize value with weight constraint (pseudo-polynomial)
- **Minimum Coins** - Find minimum coins for amount (unbounded variant)
- Time: O(n×W) | Space: O(n×W) or O(W)

### Graphs
- **BFS** - Level-order traversal, shortest path in unweighted graphs
- **DFS** - Deep traversal, cycle detection, topological sort
- Time: O(V + E) | Space: O(V)

### Trees
- **BST Validation** - Check if tree satisfies BST property
- **Tree Inversion** - Swap left/right children recursively
- **Inorder Traversal** - Produces sorted order for BST
- Time: O(n) | Space: O(h) where h = height

### Sliding Window
- **Fixed Window** - Max sum of k-length subarray
- **Dynamic Window** - Longest substring without repeating chars
- Time: O(n) | Space: O(1) or O(alphabet)

### Pointers
- **Two Sum Anagrams** - Character frequency matching
- **Find Anagrams** - Identify anagram words from list
- **Linked List Middle** - Slow/fast pointers find middle
- Time: O(n) | Space: O(1) or O(26)

### Heaps
- **K Largest Elements** - Min-heap of size k
- **K Smallest Elements** - Max-heap of size k
- **Top K Frequent** - Frequency counting + heap
- **Median Stream** - Two balanced heaps
- **IPO/Capital** - Greedy project selection
- **K Closest Points** - Distance-based heap
- Time: O(n log k) | Space: O(k)

### Tries
- **Trie Data Structure** - Prefix tree for efficient string operations
- **Word Search II** - Find words in 2D board using Trie + DFS
- Time: O(length) for insert/search | Space: O(total chars)

---

## 💡 Key Patterns

### Pattern 1: Two Pointers
```
Problems: Two Sum, Anagrams, Linked List Middle
Idea: Use two pointers moving at different speeds or directions
Benefit: Reduces space for tracking multiple values
```

### Pattern 2: Sliding Window
```
Problems: Max subarray sum, Longest substring
Idea: Maintain a window that expands/contracts
Benefit: O(n) solution instead of O(n²) nested loops
```

### Pattern 3: Monotonic Stack
```
Problems: Next Greater Element, Largest Rectangle
Idea: Stack maintains elements in monotone order
Benefit: Efficient when brute force would be nested loops
```

### Pattern 4: Heap-Based Greedy
```
Problems: K-largest, IPO, Task scheduling
Idea: Always pick locally optimal (via heap)
Benefit: Achieves global optimum for certain problems
```

### Pattern 5: DP State Reduction
```
Problems: Knapsack, Coin Change
Idea: Current state depends on previous states
Benefit: Transform exponential (2^n) to polynomial (n×W)
```

### Pattern 6: Tree Recursion
```
Problems: BST validation, Tree inversion
Idea: Process left, node, right (or variations)
Benefit: Natural match for tree structure
```

### Pattern 7: Graph Traversal
```
Problems: Find path, connectivity
Idea: BFS for shortest path, DFS for deep exploration
Benefit: Systematic exploration without missing nodes
```

---

## 🔢 Complexity Cheat Sheet

| Algorithm | Best | Avg | Worst | Space |
|-----------|------|-----|-------|-------|
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Hash Lookup | O(1) | O(1) | O(n) | O(n) |
| Stack Op | O(1) | O(1) | O(1) | O(n) |
| Heap Insert | O(1) | O(log n) | O(log n) | O(n) |
| Heap Extract | O(log n) | O(log n) | O(log n) | - |
| Graph BFS/DFS | O(V+E) | O(V+E) | O(V+E) | O(V) |
| Tree Traversal | O(n) | O(n) | O(n) | O(h) |
| DP Knapsack | O(n×W) | O(n×W) | O(n×W) | O(W) |
| Trie Search | O(m) | O(m) | O(m) | O(n) |

Where: V=vertices, E=edges, n=size, W=capacity, m=length, h=height

---

## 🚀 Quick Start

### Pick Your Topic
- Start with Binary Search if weak on searching
- Learn Stacks before Trees (foundational)
- Master Sliding Window before Graphs
- Do DP last (builds on other concepts)

### Solve in Order
1. Read problem statement
2. Identify pattern (see Key Patterns above)
3. Check complexity requirements
4. Review code solution
5. Run through examples
6. Understand edge cases

### Interview Preparation
1. **Understanding Phase:** Know WHY not just HOW
2. **Coding Phase:** Clean, readable, commented code
3. **Complexity Phase:** Discuss time/space tradeoffs
4. **Testing Phase:** Cover edge cases explicitly
5. **Discussion Phase:** Alternative approaches

---

## 📊 Problem Difficulty Distribution

| Difficulty | Count | Topics |
|------------|-------|--------|
| **Easy** | ~15 | Binary Search, Stacks, Two Pointers |
| **Medium** | ~20 | DP, Graphs, Trees, Heaps, Tries |
| **Hard** | ~8 | Advanced DP, Word Search, IPO |

---

## 🎓 Learning Path

### Week 1-2: Fundamentals
- [ ] Binary Search (all variants)
- [ ] Hash Maps basics
- [ ] Stacks and Queues

### Week 3-4: Intermediate
- [ ] Sliding Window
- [ ] Trees (traversal, BST)
- [ ] Graph basics (BFS/DFS)

### Week 5-6: Advanced
- [ ] Heaps (all 6 problems)
- [ ] Dynamic Programming
- [ ] Tries and Word problems

### Week 7-8: Integration
- [ ] Monotonic Stacks
- [ ] Combined patterns (e.g., Trie+DFS)
- [ ] Mock interviews with problems

---

## 💻 Code Examples

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Two Sum with Hash Map
```python
def two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [seen[complement], nums.index(num)]
        seen[num] = len(nums) - 1 - nums[::-1].index(num)
    return []
```

### Valid Parentheses
```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

---

## ⚡ Performance Tips

1. **Avoid Repeated Calculations:** Use memoization in recursion
2. **Choose Right Data Structure:** Hash map for O(1) lookup
3. **Early Termination:** Stop as soon as answer found
4. **In-place Operations:** Modify input when possible (if allowed)
5. **Pre-sort When Needed:** O(n log n) sort can enable O(n) solution

---

## 🔗 Additional Resources

### Pattern Recognition
- Identify if problem needs:
  - Searching → Binary Search
  - Finding pairs → Hash Map
  - Brackets → Stack
  - Best k items → Heap
  - Prefix matching → Trie
  - Graph relationship → BFS/DFS
  - Optimization → DP

### Common Mistakes
- Off-by-one errors in binary search
- Not checking empty data structures before accessing
- Forgetting to handle None/null in pointers
- Not considering edge cases (single element, empty input)
- Misunderstanding when greedy works

---

## 📝 Template for Solutions

```python
def solve(input_data):
    """
    Problem: [Name]
    Approach: [Method]
    Time: O(?) Space: O(?)
    """
    # Edge cases
    if not input_data or len(input_data) == 0:
        return []
    
    # Main logic
    result = []
    # ... implementation ...
    
    # Return result
    return result

# Test
if __name__ == "__main__":
    assert solve(test_input1) == expected_output1
    assert solve(test_input2) == expected_output2
    print("All tests passed!")
```

---

## 🎯 Next Steps

1. **Pick a topic** from the directory
2. **Read the README** for that topic
3. **Study the approach** and algorithm
4. **Review example code**
5. **Implement yourself** without looking
6. **Test on variations** and edge cases
7. **Move to next problem**

---

## 📞 Quick Reference

### When to use what?
- **Need O(1) lookup?** → Hash Map
- **Need ordered structure?** → Tree or sorted list
- **Need to process sequentially?** → Stack or Queue
- **Need k-best items?** → Heap
- **Need pattern matching?** → Trie or Regex
- **Need shortest path?** → BFS
- **Need all paths?** → DFS
- **Need optimization?** → DP
- **Need to search sorted?** → Binary Search

---

## ✅ Checklist Before Interview

- [ ] Can solve each problem in ~20 minutes
- [ ] Can explain approach in simple terms
- [ ] Know time/space complexity by heart
- [ ] Can code without looking at solution
- [ ] Understand why pattern works
- [ ] Can modify for variations
- [ ] Handle all edge cases
- [ ] Test with provided examples

---

## 📈 Success Metrics

| Goal | Target |
|------|--------|
| Problems solved | 40+ |
| Average accuracy | 90%+ |
| Average time | <30 min per problem |
| Edge cases caught | 95%+ |
| Explanation clarity | Interview-ready |

---

**Happy Coding! 🚀** Feel free to fork, modify, and share this resource.

For each topic, navigate to the respective folder and read the detailed README with examples, explanations, and code solutions.
