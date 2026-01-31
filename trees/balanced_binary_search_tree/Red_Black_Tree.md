# Red-Black Trees - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Properties](#properties)
3. [Time Complexity](#time-complexity)
4. [Color Rules](#color-rules)
5. [Insertion](#insertion)
6. [Deletion](#deletion)
7. [Search](#search)
8. [Python Implementation](#python-implementation)
9. [Examples](#examples)

---

## Introduction

A **Red-Black Tree** is a self-balancing Binary Search Tree where each node is colored either red or black. These color constraints ensure that the tree remains approximately balanced during insertions and deletions. 

### Key Concept
- Each node has a color: RED or BLACK
- These colors follow specific rules to maintain balance
- Red-Black trees are slightly less balanced than AVL trees but require fewer rotations
- Used in many practical applications (std::map in C++, TreeMap in Java, etc.)

### When to Use Red-Black Trees
- When insertions/deletions happen frequently
- When you need predictable, faster modifications than AVL
- Slightly fewer rotations compared to AVL
- More flexible than strict AVL balance

---

## Properties

1. **Binary Search Tree Property**: Left child < Parent < Right child
2. **Root is BLACK**: The root node is always black
3. **All leaves are BLACK**: None nodes are considered black (NIL nodes)
4. **No two red nodes adjacent**: If a node is red, both children must be black
5. **Black height consistent**: Every path from node to descendants has same number of black nodes
6. **Leaf NIL nodes are BLACK**

### Red-Black Tree Invariants

Let's denote:
- **Black-Height (BH)**: Number of black nodes on path from node to leaf (excluding node itself)
- **Red-Black Height**: Number of nodes from node to leaf

Rules:
- Property 1: Every node is RED or BLACK
- Property 2: Root is BLACK
- Property 3: All NIL leaves are BLACK
- Property 4: If node is RED, both children are BLACK
- Property 5: All paths from node to descendants have same number of BLACK nodes

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|-----------|
| Search    | O(log n) | O(log n)  |
| Insert    | O(log n) | O(log n)  |
| Delete    | O(log n) | O(log n)  |
| Space     | O(n)    | O(n)      |

**Advantage over BST**: Guaranteed O(log n) for all operations
**Advantage over AVL**: Fewer rotations on insertions/deletions

---

## Color Rules

### Rules for Coloring

```
Valid Configuration:
       BLACK(10)
      /         \
    RED(5)      RED(15)
    /   \       /    \
  BLK   BLK   BLK    BLK

Invalid Configuration:
       RED(10)  ❌ Root cannot be RED
      /        \
    RED(5)    BLACK(15)  ❌ Red parent has red child
```

### Black-Height Example

```
        BLACK(10)          <- Black height = 3
       /          \
    RED(5)      BLACK(15)
    /   \           /
  BLK   BLK       RED(20)
                   /    \
                 BLK    BLK

All paths from 10 to any leaf:
- 10->5->NIL: 2 black nodes (10, NIL)
- 10->15->20->NIL: 3 black nodes (10, 15, NIL)
```

---

## Insertion

### Insertion Cases

After inserting a new node as RED (to minimize violations):

#### Case 1: Uncle is RED
- Recolor parent and uncle to BLACK
- Recolor grandparent to RED
- Move problem up to grandparent

```
      G(B)                    G(R)
     /    \                  /    \
   P(R)  U(R)    =>       P(B)  U(B)
   /                      /
 N(R)                   N(R)
```

#### Case 2: Uncle is BLACK (Triangle)
- Rotate to make LINE pattern
- Then apply Case 3

```
      G(B)                  G(B)
     /    \                /    \
   P(R)  U(B)    =>      N(R)  U(B)
     \                   /
     N(R)              P(R)
```

#### Case 3: Uncle is BLACK (Line)
- Rotate grandparent
- Recolor parent (BLACK) and grandparent (RED)

```
      G(B)                   P(B)
     /    \                 /    \
   P(R)  U(B)    =>      N(R)   G(R)
   /                            \
 N(R)                          U(B)
```

#### Case 4: New node is root
- Simply recolor to BLACK

---

## Deletion

### Deletion Cases

Deletion is complex in Red-Black trees. If deleted node is RED, no violations occur. If BLACK, we need to handle:

#### Case 1: Sibling is RED
- Rotate parent
- Swap colors of parent and sibling
- Convert to case 2, 3, or 4

```
    P(B)                    S(B)
   /    \    Rotate        /    \
 N(B)  S(R)    =>        P(R)   SR(B)
        / \              /  \
      SL  SR           N(B) SL
```

#### Case 2: Sibling is BLACK with BLACK children
- Recolor sibling to RED
- Move problem to parent

```
    P(B/R)                P(B/R)
   /      \      =>      /      \
 N(B)   S(B)          N(B)    S(R)
        / \                  / \
      SL  SR              SL  SR
     B    B              B    B
```

#### Case 3: Sibling is BLACK, far nephew is BLACK, close nephew is RED
- Rotate sibling
- Swap colors
- Convert to case 4

```
    P(any)                P(any)
   /      \      =>      /      \
 N(B)   S(B)          N(B)    SR(B)
        / \                  /
      SL  SR               S(R)
     R    B               / \
                        SL  NIL
                       B
```

#### Case 4: Sibling is BLACK with RED far nephew
- Rotate parent
- Adjust colors

```
    P(C)                    S(C)
   /    \      Rotate      /    \
 N(B)  S(B)     =>       P(any) SR(B)
        / \              /  \
      SL  SR          N(B)  SL
     any  R          B      any
```

---

## Search

**Algorithm:**
Standard BST search (colors don't affect search):

```python
def search(value):
    current = root
    while current is not None:
        if value == current.value:
            return True
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    return False
```

Time Complexity: **O(log n)** guaranteed

---

## Python Implementation

```python
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

class RBNode:
    def __init__(self, value):
        self.value = value
        self.color = Color.RED  # New nodes are always RED
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.nil = RBNode(None)  # Sentinel NIL node
        self.nil.color = Color.BLACK
        self.root = self.nil
    
    # ============ ROTATIONS ============
    
    def left_rotate(self, x):
        """Perform left rotation"""
        #     x                      y
        #      \                    / \
        #       y         =>       x   T3
        #      / \                / \
        #     T1  T3            T1  T2
        
        y = x.right
        x.right = y.left
        
        if y.left != self.nil:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def right_rotate(self, y):
        """Perform right rotation"""
        #     y                    x
        #    / \                  / \
        #   x   T3      =>       T1  y
        #  / \                      / \
        # T1 T2                    T2 T3
        
        x = y.left
        y.left = x.right
        
        if x.right != self.nil:
            x.right.parent = y
        
        x.parent = y.parent
        
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x
    
    # ============ INSERTION ============
    
    def insert(self, value):
        """Insert a value into the Red-Black tree"""
        node = RBNode(value)
        node.left = self.nil
        node.right = self.nil
        
        parent = None
        current = self.root
        
        # Find correct position
        while current != self.nil:
            parent = current
            if node.value < current.value:
                current = current.left
            elif node.value > current.value:
                current = current.right
            else:
                # Duplicate - ignore
                return
        
        node.parent = parent
        
        if parent == None:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        
        node.color = Color.RED
        self._insert_fixup(node)
    
    def _insert_fixup(self, node):
        """Fix Red-Black tree properties after insertion"""
        while node.parent is not None and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                # CASE 1: Uncle is RED
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    # CASE 2: Uncle is BLACK (Triangle)
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    
                    # CASE 3: Uncle is BLACK (Line)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                
                # CASE 1: Uncle is RED
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    # CASE 2: Uncle is BLACK (Triangle)
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    
                    # CASE 3: Uncle is BLACK (Line)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.left_rotate(node.parent.parent)
        
        self.root.color = Color.BLACK
    
    # ============ DELETION ============
    
    def delete(self, value):
        """Delete a value from the Red-Black tree"""
        node = self._search_node(self.root, value)
        if node == self.nil:
            return  # Value not found
        
        self._delete_node(node)
    
    def _delete_node(self, node):
        """Internal deletion"""
        node_to_fixup = None
        node_to_fixup_parent = None
        
        # Case 1: Node has at most one child
        if node.left == self.nil:
            node_to_fixup = node.right
            node_to_fixup_parent = node.parent
            self._transplant(node, node.right)
        elif node.right == self.nil:
            node_to_fixup = node.left
            node_to_fixup_parent = node.parent
            self._transplant(node, node.left)
        else:
            # Case 2: Node has two children
            # Find successor (minimum in right subtree)
            successor = self._find_min(node.right)
            
            if successor.parent != node:
                node_to_fixup = successor.right
                node_to_fixup_parent = successor.parent
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            else:
                node_to_fixup = successor.right
                node_to_fixup_parent = successor
            
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color
        
        # Fix up if we removed a BLACK node
        if node.color == Color.BLACK and node_to_fixup != self.nil:
            self._delete_fixup(node_to_fixup)
    
    def _delete_fixup(self, node):
        """Fix Red-Black tree properties after deletion"""
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                
                # CASE 1: Sibling is RED
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                
                # CASE 2: Sibling is BLACK with two BLACK children
                if (sibling.left.color == Color.BLACK and 
                    sibling.right.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    # CASE 3: Sibling is BLACK, far child is BLACK
                    if sibling.right.color == Color.BLACK:
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    
                    # CASE 4: Sibling is BLACK, far child is RED
                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                
                # CASE 1: Sibling is RED
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                
                # CASE 2: Sibling is BLACK with two BLACK children
                if (sibling.right.color == Color.BLACK and 
                    sibling.left.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    # CASE 3: Sibling is BLACK, far child is BLACK
                    if sibling.left.color == Color.BLACK:
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    
                    # CASE 4: Sibling is BLACK, far child is RED
                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        
        node.color = Color.BLACK
    
    def _transplant(self, u, v):
        """Replace u with v in tree"""
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    # ============ SEARCH ============
    
    def search(self, value):
        """Search for a value"""
        return self._search_node(self.root, value) != self.nil
    
    def _search_node(self, node, value):
        """Search and return node"""
        current = node
        while current != self.nil:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return self.nil
    
    def _find_min(self, node):
        """Find node with minimum value"""
        current = node
        while current.left != self.nil:
            current = current.left
        return current
    
    # ============ UTILITY FUNCTIONS ============
    
    def inorder(self):
        """Inorder traversal"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node != self.nil:
            self._inorder_recursive(node.left, result)
            result.append((node.value, node.color.name))
            self._inorder_recursive(node.right, result)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print tree structure with colors"""
        if node is None:
            node = self.root
        
        if node != self.nil:
            color_str = node.color.name
            print(" " * (level * 4) + prefix + str(node.value) + 
                  f" ({color_str})")
            if node.left != self.nil or node.right != self.nil:
                if node.left != self.nil:
                    self.print_tree(node.left, level + 1, "L: ")
                else:
                    print(" " * ((level + 1) * 4) + "L: NIL(BLACK)")
                if node.right != self.nil:
                    self.print_tree(node.right, level + 1, "R: ")
                else:
                    print(" " * ((level + 1) * 4) + "R: NIL(BLACK)")
    
    def verify_properties(self):
        """Verify Red-Black tree properties (for testing)"""
        if self.root.color != Color.BLACK:
            return False, "Root is not BLACK"
        
        def check_node(node):
            if node == self.nil:
                return True, 1
            
            # Check RED-RED violation
            if node.color == Color.RED:
                if node.left.color == Color.RED or node.right.color == Color.RED:
                    return False, -1
            
            left_valid, left_bh = check_node(node.left)
            if not left_valid:
                return False, -1
            
            right_valid, right_bh = check_node(node.right)
            if not right_valid:
                return False, -1
            
            # Check black height consistency
            if left_bh != right_bh:
                return False, -1
            
            if node.color == Color.BLACK:
                return True, left_bh + 1
            else:
                return True, left_bh
        
        valid, _ = check_node(self.root)
        return valid, "All properties satisfied" if valid else "Properties violated"
```

---

## Examples

### Example 1: Basic Insertion (Case 1 - Uncle is RED)

```
Insert: 10
    10(B)

Insert: 5
    10(B)
    /
   5(R)

Insert: 15
    10(B)
   /    \
  5(R)  15(R)

Insert: 3 (triggers Case 1)
Before fixup:
     10(B)           Uncle(15) is RED
    /    \
  5(R)   15(R)
  /
3(R)

After fixup (recolor):
      10(R)
     /    \
   5(B)   15(B)
   /
  3(R)

Fix root:
      10(B)
     /    \
   5(B)   15(B)
   /
  3(R)
```

### Example 2: Insertion with Rotation (Case 3 - Uncle is BLACK, Line)

```
Insert: 10, 20, 30

Insert 10:
    10(B)

Insert 20:
    10(B)
      \
      20(R)

Insert 30 (triggers Case 3):
Before fixup:
    10(B)        Uncle(NIL) is BLACK, Line pattern
      \
      20(R)
        \
        30(R)  <- Red-Red violation

Rotate left (20->30):
    10(B)
      \
      20(R) <- Recolor to BLACK
        \
        30(R) -> Keep RED

After recolor:
      20(B)
     /    \
   10(B) 30(R)

```

### Example 3: Deletion Case 1 (Sibling is RED)

```
Tree:
      10(B)
     /    \
   5(B)  15(B)
   / \   /
 3  7  12

Delete 3 (if it was BLACK):
      10(B)
     /    \
   5(B)  15(B)
    \    /
    7   12

If sibling is RED and node is BLACK:
- Rotate parent
- Recolor
- Convert to other cases
```

### Example 4: Complete Insertion Sequence

```python
# Create tree and insert values
rbt = RedBlackTree()
values = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27]

for val in values:
    rbt.insert(val)
    print(f"Inserted {val}")

print("\nInorder traversal:", rbt.inorder())
# Output: [(5, 'RED'), (10, 'RED'), (15, 'BLACK'), ...]

# Verify properties
valid, msg = rbt.verify_properties()
print(f"Valid RB Tree: {valid} - {msg}")

# Search examples
print("Search 27:", rbt.search(27))  # True
print("Search 100:", rbt.search(100))  # False

# Print tree structure
rbt.print_tree()

# Delete examples
rbt.delete(25)
print("\nAfter deleting 25:")
rbt.print_tree()
```

### Example 5: Color Changes During Insertion

```
Sequence of insertions: 7, 3, 18, 10, 22, 8, 11, 26

Step 1: Insert 7
    7(B)

Step 2: Insert 3
    7(B)
   /
  3(R)

Step 3: Insert 18
    7(B)
   /    \
  3(R)  18(R)

Step 4: Insert 10 (uncle 18 is RED - Case 1)
Before:       After recolor:    After root fix:
    7(B)           7(R)              7(B)
   /    \         /    \            /    \
  3(R)  18(R)    3(B)  18(B)       3(B)  18(B)
    \              \
    10(R)          10(R)
```

---

## Comparison: Red-Black vs AVL

| Aspect | Red-Black Tree | AVL Tree |
|--------|---|---|
| Balance | Less strict | More strict |
| Height | O(log n), height ≤ 2ln(n+1) | O(log n), height ≈ 1.44*log(n) |
| Rotations on Insert | 1 (amortized) | 1 |
| Rotations on Delete | O(log n) (worst) | O(log n) (worst) |
| Search Performance | O(log n) | O(log n) |
| Rebalancing | Faster (fewer ops) | More careful |
| Typical Use | Databases, Maps | File systems |
| Implementation | More complex | Simpler |
| Color Changes | Frequent | N/A |

---

## Key Takeaways

1. **5 Properties**: RED, BLACK, root BLACK, no RED-RED, consistent black-height
2. **Insertion**: Always insert as RED, then fix violations
3. **3 Insertion Cases**: Uncle RED, Uncle BLACK (triangle), Uncle BLACK (line)
4. **Deletion**: Complex with 4 cases based on sibling color
5. **Rotation**: Used to maintain balance, less frequently than might be needed
6. **Black-Height**: Critical property maintaining balance
7. **Use Cases**:
   - Java's TreeMap
   - C++ std::map
   - Linux kernel scheduling
   - Database indexing

---

## Common Interview Questions

1. **Q: Why are new nodes always inserted as RED?**
   - A: To minimize violations; inserting BLACK might violate black-height property

2. **Q: How many black nodes are guaranteed on every path?**
   - A: At least floor(height/2) because red nodes break the height

3. **Q: Can a Red-Black tree have all RED nodes except leaves?**
   - A: No, no two RED nodes can be adjacent (parent-child)

4. **Q: Why is Red-Black preferred over AVL in practical systems?**
   - A: Fewer rotations during modifications, simpler rebalancing logic

5. **Q: What is black-height and why does it matter?**
   - A: It ensures balanced tree; all paths have same black-height, guaranteeing O(log n) height

6. **Q: Can deletion require multiple rotations?**
   - A: Yes, unlike insertion which needs at most 1 rotation, deletion can require O(log n)
