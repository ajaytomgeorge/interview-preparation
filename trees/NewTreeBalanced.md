# Check if Binary Tree is Balanced

## Problem Statement

Given a binary tree, check if it is **height-balanced**.

A binary tree is height-balanced if:
- The left and right subtrees of every node have heights that differ by **at most 1**
- Both left and right subtrees are also height-balanced

---

## Example

```
        10
       /  \
      20   30
     / \
    40  60

Is balanced? Check each node:
- Node 40: height = 1 (leaf)
- Node 60: height = 1 (leaf)  
- Node 20: |height(40) - height(60)| = |1 - 1| = 0 ≤ 1 ✅
- Node 30: height = 1 (leaf)
- Node 10: |height(20) - height(30)| = |2 - 1| = 1 ≤ 1 ✅

Answer: True (tree is balanced)
```

---

## Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## Solution 1: Recursive Height Calculation (Simple)

```python
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def height(node):
    """Calculate the height of a tree"""
    if node is None:
        return 0
    
    # Height = 1 + max of left height and right heights
    return 1 + max(height(node.left), height(node.right))

def isBalanced(root):
    """Check if the binary tree is height-balanced"""
    if root is None:
        return True
    
    # Get the height of left and right sub trees
    lHeight = height(root.left)
    rHeight = height(root.right)
    
    # Check if height difference is at most 1
    if abs(lHeight - rHeight) > 1:
        return False
    
    # Recursively check the left and right subtrees
    return isBalanced(root.left) and isBalanced(root.right)
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n²) - height calculated multiple times |
| **Space** | O(h) - recursion stack, h = height |

**Why O(n²)?** For each node, we recalculate the height of its subtrees.

---

## Solution 2: Optimized with Single Pass (Better)

```python
def isBalancedOptimized(root):
    """
    Check if tree is balanced while calculating height in one pass.
    Returns (is_balanced, height) tuple
    """
    def helper(node):
        if node is None:
            return (True, 0)
        
        left_balanced, left_height = helper(node.left)
        if not left_balanced:
            return (False, 0)
        
        right_balanced, right_height = helper(node.right)
        if not right_balanced:
            return (False, 0)
        
        # Check if current node is balanced
        is_balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return (is_balanced, height)
    
    balanced, _ = helper(root)
    return balanced
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) - visit each node once |
| **Space** | O(h) - recursion stack |

**Why O(n)?** Each node is visited exactly once.

---

## Test Case

```python
if __name__ == "__main__":
    # Representation of input tree:
    #            10
    #           / \
    #          20   30
    #         /  \
    #        40   60
    
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    
    print("Balanced?" if isBalanced(root) else "Not Balanced")
    # Output: Balanced?
    
    print("Optimized:" if isBalancedOptimized(root) else "Not Balanced")
    # Output: Optimized
```

---

## Examples

### Example 1: Balanced Tree

```
      1
     / \
    2   3
   / \
  4   5
```

**Check:** 
- Node 2: |height(4) - height(5)| = 0 ≤ 1 ✅
- Node 3: leaf (height = 1)
- Node 1: |height(2) - height(3)| = |2 - 1| = 1 ≤ 1 ✅

**Result:** Balanced ✅

### Example 2: Unbalanced Tree

```
      1
     /
    2
   /
  3
```

**Check:**
- Node 1: |height(2) - height(None)| = |2 - 0| = 2 > 1 ❌

**Result:** Not Balanced ❌

---

## Key Points

- **Height-balanced** means height difference ≤ 1 at **every node**
- Not just the root
- Use optimized O(n) solution for interviews
- Early termination if subtree is unbalanced

---

## Common Mistakes

- ❌ Only checking the root node
- ❌ Recalculating heights multiple times (Solution 1 inefficiency)
- ❌ Forgetting to recursively check subtrees

---

## Follow-up Questions

1. **Modify the tree to be balanced** - What nodes would you remove/add?
2. **Find the unbalanced node** closest to the root - What's the algorithm?
3. **Self-balancing trees** - AVL, Red-Black trees (automatically maintain balance)
