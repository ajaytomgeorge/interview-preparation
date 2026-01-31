# Sliding Window Problems

## 1. Fixed Window Size

### Problem Statement

Find the maximum sum of a subarray with a fixed window size.

### Examples

```
Input:    nums = [2, 1, 5, 1, 3, 2], window_size = 3
Output:   7 (subarray [5, 1, 3])

Explanation:
Windows:
- [2, 1, 5] = 8
- [1, 5, 1] = 7
- [5, 1, 3] = 9 ✓
- [1, 3, 2] = 6
```

### Algorithm

1. Calculate sum of first window
2. Slide the window by:
   - Adding new element from right
   - Removing element from left
3. Track the maximum sum

### Python Solution

```python
nums = [2, 1, 5, 1, 3, 2]
window_size = 3
window_sum = 0

# Calculate initial window sum
for i in range(window_size):
    window_sum += nums[i]

max_value = window_sum

# Slide the window
for i in range(window_size, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - window_size]
    max_value = max(max_value, window_sum)

print(max_value)  # Output: 9
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - Single pass with constant operations |
| **Space** | O(1) - Only using counters |

### Key Points

- Fixed size means window doesn't expand/contract
- Each element is visited exactly twice (added and removed once)
- Much faster than nested loop approach O(n*k)

---

## 2. Dynamic/Sliding Window

### Problem Statement

Find the length of the longest substring without repeating characters.

### Examples

```
Input:    "abcabcacbb"
Output:   3

Explanation:
- "abc" (length 3) ✓
- "bca" (length 3) ✓
- "cab" (length 3) ✓
- Longest valid: 3
```

### Algorithm

Use a **left and right pointer** with a dictionary tracking character positions:

1. Expand right pointer to include characters
2. If character already exists in current window:
   - Move left pointer to skip the previous occurrence
3. Track maximum window size encountered

### Python Solution

```python
from collections import defaultdict

input_data = "abcabcacbb"

left = 0
index_tracker = {}
max_value = 0

for right in range(len(input_data)):
    char = input_data[right]
    
    # If character exists and is within current window
    if char in index_tracker and index_tracker[char] >= left:
        # Move left pointer past the previous occurrence
        left = index_tracker[char] + 1

    # Update character's latest position
    index_tracker[char] = right
    
    # Update max length
    max_value = max(right - left + 1, max_value)

print(max_value)  # Output: 3
```

### Dry Run Example: "abcabcacbb"

```
right=0, char='a': left=0, index_tracker={'a':0}, max=1
right=1, char='b': left=0, index_tracker={'a':0,'b':1}, max=2
right=2, char='c': left=0, index_tracker={'a':0,'b':1,'c':2}, max=3

right=3, char='a': 'a' in window (index 0 >= left 0)
                   left = 0 + 1 = 1
                   index_tracker={'a':3,'b':1,'c':2}, max=3

right=4, char='b': 'b' in window (index 1 >= left 1)
                   left = 1 + 1 = 2
                   index_tracker={'a':3,'b':4,'c':2}, max=3

right=5, char='c': 'c' in window (index 2 >= left 2)
                   left = 2 + 1 = 3
                   index_tracker={'a':3,'b':4,'c':5}, max=3

... continues, max stays 3
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - Each character visited at most twice |
| **Space** | O(min(n, m)) - HashMap size (m = alphabet size) |

### Key Points

- **Left Pointer:** Shrinks window when duplicate found
- **Right Pointer:** Expands window to add characters
- **Index Tracking:** Stores position of last occurrence
- **Why >= left?:** Ensures duplicate is within current window

### Variations

1. **Longest substring with at most k distinct characters**
2. **Longest substring with exactly k distinct characters**
3. **Minimum window substring** (find window containing all target chars)

---

## Fixed vs Dynamic Window Comparison

| Aspect | Fixed Window | Dynamic Window |
|--------|--------------|----------------|
| **Size** | Constant | Changes based on condition |
| **Pointers** | One right pointer | Two pointers (left & right) |
| **Use Cases** | Max/min sum of k elements | Find optimal substring |
| **Complexity** | O(n) | O(n) |
| **Space** | O(1) | O(alphabet size) |

### Template for Sliding Window

```python
# FIXED WINDOW
for right in range(n):
    # Add element at right
    # Remove element at (right - k)
    # Check result

# DYNAMIC WINDOW
left = 0
for right in range(n):
    # Add element at right
    # Check condition
    while condition_violated:
        # Shrink from left
        left += 1
    # Update result
```

---

---

## 3. Permutation in String

### Problem Statement

Given two strings `s1` and `s2`, return `True` if any permutation of `s1` is a **substring** of `s2`.

**Key Insight:** A permutation is the same characters in different order. We need to find if any rearrangement of s1 appears as a substring in s2.

### Examples

```
Input:    s1 = "ab", s2 = "eidbaooo"
Output:   True
Explanation: "ba" is a permutation of "ab" and appears in s2

Input:    s1 = "ab", s2 = "abab"
Output:   True
Explanation: "ab" is a permutation of itself and appears in s2

Input:    s1 = "ab", s2 = "a"
Output:   False
Explanation: No substring of s2 has length 2
```

### Algorithm: Fixed Window with Frequency Matching

1. **Window size** = length of s1 (fixed)
2. **Character frequency** of s1 should match window in s2
3. **Slide window** through s2 and compare frequencies

### Python Solution

```python
def permutationInString(s1, s2):
    if len(s1) > len(s2):
        return False
    
    # Frequency count of s1
    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    
    # Window size = len(s1)
    window_size = len(s1)
    
    # Initialize window with first substring of s2
    window_count = {}
    for i in range(window_size):
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1
    
    # Check if first window matches
    if window_count == s1_count:
        return True
    
    # Slide window through s2
    for i in range(window_size, len(s2)):
        # Add new character from right
        new_char = s2[i]
        window_count[new_char] = window_count.get(new_char, 0) + 1
        
        # Remove character from left
        old_char = s2[i - window_size]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
        
        # Check if current window matches
        if window_count == s1_count:
            return True
    
    return False

# Examples
print(permutationInString("ab", "eidbaooo"))  # True
print(permutationInString("ab", "abab"))      # True
print(permutationInString("ab", "a"))         # False
```

### Optimized Solution (Array-based)

```python
def permutationInString_optimized(s1, s2):
    if len(s1) > len(s2):
        return False
    
    # Count characters in s1 (26 letters)
    s1_count = [0] * 26
    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
    
    # Window for s2
    window = [0] * 26
    for i in range(len(s2)):
        # Add new character
        window[ord(s2[i]) - ord('a')] += 1
        
        # Remove leftmost character if window > len(s1)
        if i >= len(s1):
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        # Check if match
        if i >= len(s1) - 1 and window == s1_count:
            return True
    
    return False
```

### Using Counter (Pythonic Approach)

```python
from collections import Counter

def permutationInString_counter(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_count = Counter(s1)
    window = Counter()
    left = 0
    
    for right in range(len(s2)):
        window[s2[right]] += 1
        
        # Keep window size equal to len(s1)
        if right - left + 1 > len(s1):
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
        
        # Check if window matches s1
        if window == s1_count:
            return True
    
    return False

# Examples
print(permutationInString_counter("ab", "eidbaooo"))  # True
print(permutationInString_counter("ab", "abab"))      # True
print(permutationInString_counter("ab", "a"))         # False
```

**Advantages of Counter:**
- More Pythonic and readable
- Counter is optimized for frequency counting
- Less code, more intention-clear
- Automatically handles missing keys (returns 0)

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(len(s2) × 26) = O(len(s2)) |
| **Space** | O(1) - Fixed size arrays/dicts (26 letters) |

### Dry Run Example: s1="ab", s2="eidbaooo"

```
s1_count: {'a': 1, 'b': 1}

i=0,1: window="ei" → {'e':1, 'i':1} ≠ s1_count
i=2: window="id" → {'i':1, 'd':1} ≠ s1_count
i=3: window="db" → {'d':1, 'b':1} ≠ s1_count
i=4: window="ba" → {'b':1, 'a':1} = s1_count ✓ Return True
```

### Key Points

- **Fixed window:** Window size is always len(s1)
- **Frequency matching:** Compare character frequencies instead of strings
- **Early termination:** Return true as soon as match found
- **Edge case:** If s1 longer than s2, impossible

---

## 4. Fruit Into Baskets

### Problem Statement

You're at a tree farm with an orchard represented as an array. Each position has a fruit type. You start from any tree and can move right, but **can only carry 2 different types of fruit** at once.

**Goal:** Find the **maximum number of fruits** you can collect.

**Rules:**
- Start anywhere
- Move only right
- Pick fruits sequentially
- Can only hold 2 distinct fruit types
- If new fruit type encountered: must drop all of one type first

### Examples

```
Input:    [1, 0, 1, 4, 1, 4, 1, 2, 3]
Output:   5
Explanation: Pick [1, 4, 1, 4, 1] (types 1 and 4, starting at index 1)

Input:    [0, 1, 2, 2]
Output:   3
Explanation: Pick [1, 2, 2] (types 1 and 2, starting at index 1)

Input:    [1, 2, 3, 2, 2]
Output:   4
Explanation: Pick [2, 3, 2, 2] (types 2 and 3, starting at index 1)
```

### Algorithm: Dynamic Sliding Window

This is a **dynamic window** problem where window size changes:
- **Expand right:** Collect fruits while ≤ 2 types
- **Shrink left:** When 3rd type encountered, remove from left until only 2 types remain

### Python Solution

```python
def totalFruit(fruits):
    left = 0
    fruit_count = {}  # Track count of each fruit type in window
    max_fruits = 0
    
    for right in range(len(fruits)):
        # Add fruit at right pointer
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        
        # If more than 2 types, shrink window from left
        while len(fruit_count) > 2:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1
        
        # Current window is valid (≤ 2 types)
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits

# Examples
print(totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))  # 5
print(totalFruit([0, 1, 2, 2]))                  # 3
print(totalFruit([1, 2, 3, 2, 2]))               # 4
```

### Dry Run Example: [1, 0, 1, 4, 1, 4, 1, 2, 3]

```
right=0, fruit=1: {1:1}, left=0, size=1, max=1
right=1, fruit=0: {1:1, 0:1}, left=0, size=2, max=2
right=2, fruit=1: {1:2, 0:1}, left=0, size=3, max=3
right=3, fruit=4: {1:2, 0:1, 4:1} (3 types - shrink)
  Remove fruits[0]=1: {1:1, 0:1, 4:1} still 3
  Remove fruits[1]=0: {1:1, 4:1} now 2 types
  left=2, size=(3-2+1)=2, max=3
right=4, fruit=1: {1:2, 4:1}, left=2, size=3, max=3
right=5, fruit=4: {1:2, 4:2}, left=2, size=4, max=4
right=6, fruit=1: {1:3, 4:2}, left=2, size=5, max=5 ✓
right=7, fruit=2: {1:3, 4:2, 2:1} (3 types - shrink)
  Remove fruits[2]=1: {1:2, 4:2, 2:1} still 3
  Remove fruits[3]=4: {1:2, 4:1, 2:1} still 3
  Remove fruits[4]=1: {1:1, 4:1, 2:1} still 3
  Remove fruits[5]=4: {1:1, 2:1} now 2 types
  left=6, size=(7-6+1)=2, max=5
right=8, fruit=3: {1:1, 2:1, 3:1} (3 types - shrink)
  Remove fruits[6]=1: {2:1, 3:1} now 2 types
  left=7, size=(8-7+1)=2, max=5
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - Each fruit visited once by each pointer |
| **Space** | O(1) - At most 3 entries in dictionary (2 basket types + temporary) |

### Why Sliding Window Works Here

**Key Property:** When a 3rd fruit type appears:
- We can't just move right pointer
- We must move left pointer until only 2 types remain
- This is the definition of a "dynamic window"

### Key Points

- **Fruit types ≤ 2:** Always maintain this constraint
- **Dictionary tracking:** Stores fruit type → count in current window
- **Shrink from left:** Remove left fruit until ≤ 2 types
- **Maximum at each step:** Update max after ensuring valid window

### Similar Pattern

This is similar to "**Longest Substring with At Most K Distinct Characters**":
- Replace "fruits" with "characters"
- Replace "2 baskets" with "k"
- Same algorithm applies!

### Generalized Template

```python
def atMostKFruits(fruits, k):
    """Find longest subarray with at most k distinct elements"""
    left = 0
    fruit_count = {}
    max_length = 0
    
    for right in range(len(fruits)):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        
        while len(fruit_count) > k:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

## Practice Variations

1. **Longest Substring Without Repeating Characters** ✓ (covered)
2. **Max Consecutive Ones III** - Find max consecutive 1s with at most k flips
3. **Minimum Window Substring** - Find smallest window with all target characters
4. **Permutation in String** ✓ (covered)
5. **Fruit Into Baskets** ✓ (covered)
