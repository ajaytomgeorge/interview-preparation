# Linked List Pointer Problems

## Find Middle of Linked List

### Problem Statement

Given a singly linked list, find the middle node.

- If the list has even length, return the **second middle node**
- If the list has odd length, return the **middle node**

### Examples

```
List: 1 → 2 → 3 → 4 → 5
Middle: 3 (odd length)

List: 1 → 2 → 3 → 4
Middle: 3 (second middle for even length)

List: 1
Middle: 1
```

### Approach: Slow and Fast Pointers

Use two pointers:
- **Slow pointer:** moves 1 step at a time
- **Fast pointer:** moves 2 steps at a time

When fast pointer reaches the end, slow pointer is at the middle.

### Why This Works

**The relative position:**
- Fast pointer is always 2x distance from start as slow pointer
- When fast reaches end, slow is at distance n/2 → middle

### Python Implementation

```python
class Node:
    def __init__(self, data, right=None):
        self.data = data
        self.right = right  # Points to next node

def find_middle(head):
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.right:
        slow = slow.right
        fast = fast.right.right
    
    return slow  # slow is now at middle

# Build a linked list: 1 → 2 → 3 → 4 → 5
head = Node(1)
current = head
for i in range(2, 6):
    current.right = Node(i)
    current = current.right

# Find middle
middle = find_middle(head)
print("Middle value is", middle.data)  # Output: 3
```

### Complete Example with List Building

```python
class Node:
    def __init__(self, data, right=None):
        self.data = data
        self.right = right

# Build linked list
original_node = start_node = Node(1)
for i in range(2, 12):
    start_node.right = Node(i)
    start_node = start_node.right

# Find middle
slow = fast = original_node
previous = slow

while fast and fast.right:
    print("Slow at:", slow.data)
    print("Fast at:", fast.data)
    slow = slow.right
    fast = fast.right.right

print("Middle value is:", slow.data)
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - traverse to middle |
| **Space** | O(1) - only two pointers |

### Step-by-Step Execution

For list: `1 → 2 → 3 → 4 → 5`

| Iteration | Slow | Fast | Slow.data | Fast.data |
|-----------|------|------|-----------|-----------|
| Start | Node(1) | Node(1) | 1 | 1 |
| 1 | Node(2) | Node(3) | 2 | 3 |
| 2 | Node(3) | Node(5) | 3 | 5 |
| 3 | Node(4) | None | 4 | - |
| Exit | Node(3) | None | **3** | - |

### Why Not Use Length First?

**Alternative Approach (Less Efficient):**
```python
def find_middle_length_first(head):
    # First pass: count nodes
    length = 0
    current = head
    while current:
        length += 1
        current = current.right
    
    # Second pass: reach middle
    middle_pos = length // 2
    current = head
    for _ in range(middle_pos):
        current = current.right
    
    return current

# Time: O(n) + O(n/2) = O(n)
# Space: O(1)
```

**Why Slow/Fast is Better:**
- Single pass (more elegant)
- Two pointers (easier to visualize)
- Same time complexity but cleaner code

### Edge Cases

```python
# Single node
head = Node(1)
middle = find_middle(head)
print(middle.data)  # 1

# Two nodes
head = Node(1)
head.right = Node(2)
middle = find_middle(head)
print(middle.data)  # 2 (second middle)

# Empty list
head = None
middle = find_middle(head)
print(middle)  # None
```

### Related Operations

#### Print Linked List
```python
def print_list(head):
    current = head
    while current:
        print(current.data, end=" → ")
        current = current.right
    print("None")
```

#### Find Node at Position
```python
def find_node_at(head, position):
    current = head
    for _ in range(position):
        if not current:
            return None
        current = current.right
    return current
```

#### Split List at Middle
```python
def split_list(head):
    if not head or not head.right:
        return head, None
    
    slow = fast = head
    prev = None
    
    while fast and fast.right:
        prev = slow
        slow = slow.right
        fast = fast.right.right
    
    # Split: prev.right becomes None
    if prev:
        prev.right = None
    
    return head, slow
```

### Interview Tips

1. **Always Check for None:** Handle empty lists and end of list
2. **While Condition:** `while fast and fast.right` prevents null pointer errors
3. **Odd vs Even:** Fast pointer naturally handles both cases
4. **Fast Pointer Movement:** `fast = fast.right.right` (not `fast += 2`)
5. **Two Pointers Pattern:** Used in many linked list problems

### Common Mistakes

❌ **Mistake 1:** Forgetting to check `fast.right`
```python
while fast:  # WRONG: might access null.right
    slow = slow.right
    fast = fast.right.right  # Can crash!
```

✅ **Correct:**
```python
while fast and fast.right:  # Check both
    slow = slow.right
    fast = fast.right.right
```

❌ **Mistake 2:** Not handling None properly
```python
def find_middle(head):
    slow = fast = head
    # What if head is None?
```

✅ **Correct:**
```python
def find_middle(head):
    if not head:
        return None
    slow = fast = head
```

### Related Problems

1. **Find Middle of Linked List** ✓ (covered)
2. **Palindrome Linked List** - Check if list reads same forwards/backwards
3. **Merge Sort for Linked List** - Use middle finding + merge
4. **Reorder List** - Use middle + reverse + merge
5. **Remove Middle Node** - Find middle + delete it
