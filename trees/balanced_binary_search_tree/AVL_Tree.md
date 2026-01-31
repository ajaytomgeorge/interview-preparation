# AVL Trees - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Properties](#properties)
3. [Time Complexity](#time-complexity)
4. [Rotations](#rotations)
5. [Insertion](#insertion)
6. [Deletion](#deletion)
7. [Search](#search)
8. [Python Implementation](#python-implementation)
9. [Examples](#examples)

---

## Introduction

An **AVL Tree** is a self-balancing Binary Search Tree (BST) named after its inventors **Adelson-Velsky and Landis**. It automatically maintains balance during insertion and deletion operations to ensure optimal search performance.

### Key Concept
- For every node, the difference in height between the left and right subtree (called the **balance factor**) must be at most 1
- Balance Factor (BF) = height(left subtree) - height(right subtree)
- Valid Balance Factors: -1, 0, +1
- If |BF| > 1, the tree performs rotations to rebalance itself

---

## Properties

1. **Binary Search Tree Property**: Left child < Parent < Right child
2. **Balance Property**: |height(left) - height(right)| ≤ 1 for every node
3. **Self-Balancing**: Automatically rebalances on insert/delete
4. **Height**: O(log n) guaranteed for n nodes
5. **No duplicate values** (typically in standard implementation)

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|-----------|
| Search    | O(log n) | O(log n)  |
| Insert    | O(log n) | O(log n)  |
| Delete    | O(log n) | O(log n)  |
| Space     | O(n)    | O(n)      |

**Note**: Unlike regular BST where worst case is O(n), AVL guarantees O(log n) for all operations.

---

## Rotations

Rotations are performed when the balance factor becomes ±2. There are 4 main types:

### 1. Left-Left Case (LL) - Right Rotation
When: BF = 2 and left subtree's BF ≥ 0
```
    z                                      y 
   / \                                   /   \
  y   T4      Right Rotate(z)          x      z
 / \          --------->              / \    / \
x   T3                               T1  T2 T3 T4
/ \
T1 T2
```

### 2. Right-Right Case (RR) - Left Rotation
When: BF = -2 and right subtree's BF ≤ 0
```
  x                                            y
   \                                          / \
    y         Left Rotate(x)                x   z
     \        --------->                   / \   \
      z                                   T1 T2  T3
     / \
    T2 T3
```

### 3. Left-Right Case (LR) - Left-Right Rotation
When: BF = 2 and left subtree's BF ≤ -1
```
    z                               z                           y
   / \                            /   \                        /   \
  x   T4  Left Rotate(x)         y    T4  Right Rotate(z)    x     z
   \      --------->            / \       --------->        / \   / \
    y                          x   T3                      T1 T2 T3 T4
   / \
  T1 T3

First: Left rotate on x, then right rotate on z
```

### 4. Right-Left Case (RL) - Right-Left Rotation
When: BF = -2 and right subtree's BF ≥ 1
```
  x                                x                              y
   \                                \                            /   \
    z         Right Rotate(z)        y         Left Rotate(x)   x     z
   /          --------->              \        --------->      / \   / \
  y                                     z                     T1 T2 T3 T4
 / \
T1 T2

First: Right rotate on z, then left rotate on x
```

---

## Insertion

**Algorithm:**
1. Insert as in normal BST
2. Update heights for ancestors
3. Calculate balance factor for each ancestor
4. If any ancestor has |BF| > 1, perform rotations

### Insertion Cases Summary

| Case | Condition | Rotation |
|------|-----------|----------|
| LL | BF(node) = 2, BF(left) ≥ 0 | Right Rotation |
| RR | BF(node) = -2, BF(right) ≤ 0 | Left Rotation |
| LR | BF(node) = 2, BF(left) < 0 | Left-Right Rotation |
| RL | BF(node) = -2, BF(right) > 0 | Right-Left Rotation |

---

## Deletion

**Algorithm:**
1. Delete as in normal BST
2. Update heights for ancestors
3. Calculate balance factor for each ancestor
4. If any ancestor has |BF| > 1, perform rotations
5. **Important**: Unlike insertion, deletion may require multiple rotations

---

## Search

**Algorithm:**
Standard BST search:
1. Start at root
2. If target equals current node, return node
3. If target < current node, search in left subtree
4. If target > current node, search in right subtree
5. If no node found, return None

Time Complexity: **O(log n)** guaranteed

---

## Python Implementation

```python
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.balance_factor = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        """Get height of a node"""
        if node is None:
            return 0
        return node.height
    
    def get_balance_factor(self, node):
        """Calculate balance factor"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """Update node's height based on children"""
        if node is None:
            return
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
        node.balance_factor = self.get_balance_factor(node)
    
    # ============ ROTATIONS ============
    
    def right_rotate(self, y):
        """Perform right rotation"""
        #     y                    x
        #    / \                  / \
        #   x   T3      =>       T1  y
        #  / \                      / \
        # T1 T2                    T2 T3
        
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        """Perform left rotation"""
        #     x                      y
        #      \                    / \
        #       y         =>       x   T3
        #      / \                / \
        #     T1  T3            T1  T2
        
        y = x.right
        T1 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T1
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    # ============ INSERTION ============
    
    def insert(self, value):
        """Insert a value into the AVL tree"""
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Recursive insertion with balancing"""
        # Step 1: Perform normal BST insertion
        if node is None:
            return AVLNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values - ignore or handle as needed
            return node
        
        # Step 2: Update height and balance factor
        self.update_height(node)
        
        # Step 3: Get balance factor
        balance = self.get_balance_factor(node)
        
        # Step 4: Check if node is unbalanced and perform rotations
        
        # LEFT-LEFT CASE
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        # RIGHT-RIGHT CASE
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        
        # LEFT-RIGHT CASE
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # RIGHT-LEFT CASE
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    # ============ DELETION ============
    
    def delete(self, value):
        """Delete a value from the AVL tree"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Recursive deletion with balancing"""
        if node is None:
            return None
        
        # Step 1: Perform normal BST deletion
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get inorder successor
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        if node is None:
            return None
        
        # Step 2: Update height and balance factor
        self.update_height(node)
        
        # Step 3: Get balance factor
        balance = self.get_balance_factor(node)
        
        # Step 4: Check if node is unbalanced and perform rotations
        
        # LEFT-LEFT CASE
        if balance > 1:
            if self.get_balance_factor(node.left) >= 0:
                return self.right_rotate(node)
            else:
                # LEFT-RIGHT CASE
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        # RIGHT-RIGHT CASE
        if balance < -1:
            if self.get_balance_factor(node.right) <= 0:
                return self.left_rotate(node)
            else:
                # RIGHT-LEFT CASE
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        
        return node
    
    def _find_min(self, node):
        """Find node with minimum value"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # ============ SEARCH ============
    
    def search(self, value):
        """Search for a value in the AVL tree"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Recursive search"""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    # ============ UTILITY FUNCTIONS ============
    
    def inorder(self):
        """Inorder traversal"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print tree structure"""
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value) + 
                  f" (H:{node.height}, BF:{node.balance_factor})")
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, level + 1, "L: ")
                else:
                    print(" " * ((level + 1) * 4) + "L: None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R: ")
                else:
                    print(" " * ((level + 1) * 4) + "R: None")
```

---

## Examples

### Example 1: Insertion with LEFT-LEFT Rotation

```
Insert values: 10, 5, 3

Step 1: Insert 10
    10

Step 2: Insert 5
    10
   /
  5

Step 3: Insert 3 (triggers LEFT-LEFT case)
Before Rotation:
    10 (BF=2, left=5, BF=1 ≥ 0) -> LEFT-LEFT
   /
  5
 /
3

After RIGHT ROTATION:
    5
   / \
  3   10
```

### Example 2: Insertion with RIGHT-RIGHT Rotation

```
Insert values: 10, 20, 30

Step 1: Insert 10
    10

Step 2: Insert 20
    10
      \
       20

Step 3: Insert 30 (triggers RIGHT-RIGHT case)
Before Rotation:
    10 (BF=-2, right=20, BF=-1 ≤ 0) -> RIGHT-RIGHT
      \
       20
         \
          30

After LEFT ROTATION:
      20
     /  \
    10   30
```

### Example 3: Insertion with LEFT-RIGHT Rotation

```
Insert values: 10, 5, 7

Step 1-2: Insert 10, 5
    10
   /
  5

Step 3: Insert 7 (triggers LEFT-RIGHT case)
Before Rotations:
    10 (BF=2, left=5, BF=-1 < 0) -> LEFT-RIGHT
   /
  5
   \
    7

After LEFT ROTATION on left child:
    10
   /
  7
 /
5

After RIGHT ROTATION on root:
    7
   / \
  5   10
```

### Example 4: Insertion with RIGHT-LEFT Rotation

```
Insert values: 10, 20, 15

Step 1-2: Insert 10, 20
    10
      \
       20

Step 3: Insert 15 (triggers RIGHT-LEFT case)
Before Rotations:
    10 (BF=-2, right=20, BF=1 > 0) -> RIGHT-LEFT
      \
       20
      /
     15

After RIGHT ROTATION on right child:
    10
      \
       15
         \
          20

After LEFT ROTATION on root:
      15
     /  \
    10   20
```

### Example 5: Complete Insertion Sequence

```python
# Create tree and insert values
avl = AVLTree()
values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27]

for val in values:
    avl.insert(val)
    print(f"Inserted {val}")

print("\nInorder traversal:", avl.inorder())
# Output: [5, 10, 15, 25, 27, 30, 50, 60, 75, 80]

# Search examples
print("Search 27:", avl.search(27))  # True
print("Search 100:", avl.search(100))  # False

# Delete examples
avl.delete(25)
print("After deleting 25:", avl.inorder())
```

### Example 6: Deletion with Rebalancing

```
Tree:
      50
     /  \
    30   70
   / \
  20  40

Delete 20:
      50
     /  \
    40   70
   /

Rebalance (RIGHT-RIGHT case):
      50
     /  \
    40   70

Then continues up...
```

---

## Key Takeaways

1. **Always Balanced**: AVL trees maintain O(log n) height guarantee
2. **4 Rotation Cases**: LL, RR, LR, RL cover all imbalance scenarios
3. **Insertion**: Single rotation usually needed
4. **Deletion**: May need multiple rotations (unlike insertion)
5. **Performance**: Guaranteed O(log n) for all operations
6. **Trade-off**: More rotations on modification, faster searches
7. **Use Cases**: 
   - Database indexes
   - File systems
   - When search operations are frequent
   - When you need guaranteed logarithmic performance

---

## Common Interview Questions

1. **Q: How many rotations are needed for insertion?**
   - A: At most one rotation (at the first unbalanced node)

2. **Q: Can deletion require multiple rotations?**
   - A: Yes, deletion might trigger cascading rotations up the tree

3. **Q: How is AVL different from Red-Black trees?**
   - A: AVL is more balanced (stricter), Red-Black allows more flexibility

4. **Q: What's the maximum height of an AVL tree with n nodes?**
   - A: Height ≈ 1.44 * log₂(n+1)

5. **Q: When to use AVL over Red-Black tree?**
   - A: When searches are much more frequent than insertions/deletions
