# 🌳 Tree Types — Operations, Efficiency & Complexity

## 1️⃣ Core Tree Structures

| Tree Type | Subtype | Operations Allowed | Strengths (🙂) / Weaknesses (😬) | Time Complexity (Avg / Worst) | Space |
|-----------|---------|-------------------|--------------------------------|-------------------------------|-------|
| Binary Tree | — | Insert, Delete, Traverse | Simple 🙂 / No order 😬 | O(n) / O(n) | O(h) |
| BST | Unbalanced | Search, Insert, Delete | Ordered 🙂 / Can degrade 😬 | O(log n) / O(n) | O(h) |
| BST | Balanced | Search, Insert, Delete, Rotate | Guaranteed log time 🙂🙂 | O(log n) | O(log n) |

## 2️⃣ Balanced Binary Trees (BST Variants)

| Tree | Insert | Delete | Search | Rotation | Best At | Time (All Ops) | Space |
|------|--------|--------|--------|----------|---------|----------------|-------|
| AVL Tree | 🙂🙂 | 🙂🙂 | 🙂🙂🙂 | 🙂🙂🙂 | Fast lookups | O(log n) | O(log n) |
| Red-Black Tree | 🙂🙂🙂 | 🙂🙂🙂 | 🙂🙂 | 🙂🙂 | Fast updates | O(log n) | O(log n) |
| Splay Tree | 🙂🙂 | 🙂🙂 | 🙂🙂🙂* | 🙂🙂🙂 | Temporal locality | Amortized O(log n) | O(log n) |

*Worst case O(n), amortized O(log n)

## 3️⃣ Non-Binary Trees

| Tree Type | Children | Operations | Best Use Case | Time Complexity | Space |
|-----------|----------|-----------|---------------|-----------------|-------|
| N-ary Tree | N | Insert, Delete, Traverse | Hierarchical data | O(n) | O(h) |
| Trie Tree | Alphabet-based | Insert, Search, Prefix | String search | O(L) | High 😬 |

L = length of word

## 🔁 Traversal Algorithms (Applies to All Trees)

### DFS Traversals

| Traversal | Order | Best For | Time | Space |
|-----------|-------|----------|------|-------|
| Preorder | Root → Left → Right | Copy tree | O(n) | O(h) |
| Inorder | Left → Root → Right | Sorted BST output | O(n) | O(h) |
| Postorder | Left → Right → Root | Deletion | O(n) | O(h) |

### BFS Traversal

| Traversal | Order | Data Structure | Best For | Time | Space |
|-----------|-------|----------------|----------|------|-------|
| Level Order (BFS) | Level-by-level | Queue | Shortest path | O(n) | O(n) |

## 🧠 Ultra-Short Revision Table

| Tree | Ordered | Balanced | Fast Search | String Friendly |
|------|---------|----------|-------------|-----------------|
| Binary Tree | ❌ | ❌ | ❌ | ❌ |
| BST | ✅ | ❌ | 😬 | ❌ |
| AVL | ✅ | ✅ | 🙂🙂🙂 | ❌ |
| Red-Black | ✅ | ✅ | 🙂🙂 | ❌ |
| Splay | ✅ | Self | 🙂🙂🙂* | ❌ |
| Trie | ❌ | N/A | 🙂🙂🙂 | ✅ |

---

## 2. Reverse a Binary Tree

### Problem Statement

Invert a binary tree by swapping left and right children at every node.

### Examples

```
Original:           Reversed:
       1                  1
      / \                / \
     2   3              3   2
    / \                / \
   4   5              5   4
```

### Algorithm

For each node:
1. Recursively reverse left subtree
2. Recursively reverse right subtree
3. Swap left and right children

### Python Solution

```python
def reverse_tree(root):
    if not root:
        return
    
    # Reverse left subtree
    reverse_tree(root.left)
    
    # Reverse right subtree
    reverse_tree(root.right)
    
    # Swap children
    root.left, root.right = root.right, root.left

# Usage
print_inorder(root)
print("After reverse")
reverse_tree(root)
print_inorder(root)
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - visit each node once |
| **Space** | O(h) - recursion stack |

### Iterative Approach (Level-order)

```python
from collections import deque

def reverse_tree_iterative(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 3. Print Inorder Traversal

### Problem Statement

Print tree nodes in Inorder sequence: Left → Root → Right

### Algorithm

1. Recursively traverse left subtree
2. Print current node
3. Recursively traverse right subtree

### Python Solution

```python
def print_inorder(root):
    if not root:
        return
    
    print_inorder(root.left)      # Left
    print(root.data)               # Root
    print_inorder(root.right)      # Right

# Example
print_inorder(root)
# For BST, prints values in sorted order
```

### Output for Example Tree

```
Tree:
       10
      /  \
     5   20
    / \
   3   7

Inorder: 3, 5, 7, 10, 20 (sorted!)
```

### Key Property for BST

**For a valid BST, Inorder traversal produces sorted sequence.**

This can be used to verify if a tree is a BST:

```python
def is_bst_via_inorder(root):
    result = []
    inorder_collect(root, result)
    return result == sorted(result)

def inorder_collect(root, result):
    if not root:
        return
    inorder_collect(root.left, result)
    result.append(root.data)
    inorder_collect(root.right, result)
```

---

## Tree Traversal Methods

| Method | Order | Use Case |
|--------|-------|----------|
| **Inorder** | Left → Root → Right | BST sorted order |
| **Preorder** | Root → Left → Right | Tree copy, prefix expression |
| **Postorder** | Left → Right → Root | Tree deletion, postfix expression |
| **Level-order** | Level by level | Shortest path, BFS |

### All Traversals Example

```python
def preorder(root):
    if not root:
        return
    print(root.data)         # Root
    preorder(root.left)       # Left
    preorder(root.right)      # Right

def postorder(root):
    if not root:
        return
    postorder(root.left)      # Left
    postorder(root.right)     # Right
    print(root.data)          # Root

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## Key Concepts

### Binary Search Tree (BST)

- Left child < Parent < Right child
- Enables efficient searching, insertion, deletion (O(log n) average)
- Inorder traversal gives sorted order

### Tree Reversal

- Important for interview questions
- Two approaches: recursive (clean) or iterative (less stack space)

### Validation

Always check edge cases:
- Empty tree (None)
- Single node
- Unbalanced trees
- Trees with duplicate values

---

## Practice Problems

1. **Validate BST** ✓ (covered)
2. **Invert Binary Tree** ✓ (covered)
3. **Binary Tree Level Order Traversal**
4. **Maximum Path Sum**
5. **Lowest Common Ancestor**
6. **Symmetric Tree**
7. **Balanced Binary Tree**
8. **Vertical Order Traversal**


Big-picture intuition
Min Heap

“Always give me the smallest element, fast.”

A min heap is a complete binary tree where:

Every parent ≤ its children

The minimum element is always at the root

It does not keep things fully sorted.

Binary Search Tree (BST)

“Let me keep everything ordered.”

A BST maintains this invariant:

Left subtree < node < right subtree

This means an in-order traversal gives sorted data.

Structural difference
Min Heap

Shape: Complete binary tree

Order: Only parent-child ordering

Siblings have no defined order

BST

Shape: Arbitrary (can be skewed)

Order: Full ordering across the tree

Structure depends on insertion order


so in min heap , same element can be under both left sub childraan and right subchildren

Yep — exactly right ✅
That’s one of the key things that trips people up about heaps.

Short answer

In a min heap:

✔️ The same value (or equal values) can appear in both left and right subtrees
✔️ There is NO ordering rule between siblings or subtrees

The only rule is:

Parent ≤ children

That’s it. Nothing more.

Concrete example

This is a valid min heap:

        2
       / \
      5   5
     / \   \
    5   8   5


Here:

Same element (5) appears:

Left subtree

Right subtree

Multiple levels

Totally fine 👍

Why this is allowed

A heap does not care about:

Left vs right ordering

Global sorting

Where equal elements go

It only enforces a local condition:

parent <= child


So these are all valid parent–child relationships:

2 → 5

5 → 5

5 → 8

Compare with BST (important contrast)

In a Binary Search Tree, this would be illegal depending on policy:

        5
       / \
      5   5   ❌ (ambiguous ordering)


BSTs must define:

“duplicates go left” or

“duplicates go right”

Heaps don’t care — duplicates are free to live anywhere.

Even more subtle point

Two heaps with the same elements can look very different structurally and still both be valid:

Heap A:

    1
   / \
  3   2


Heap B:

    1
   / \
  2   3


Both are valid min heaps.

Mental model (helps a lot)

Think of a min heap as:

A tournament bracket where the smallest always wins to the top

It doesn’t matter how players are arranged — only that the winner bubbles up.

TL;DR

✔️ Same element can appear in both left and right subtrees

✔️ Duplicates are allowed freely

❌ No global ordering

✔️ Only parent ≤ children rule
