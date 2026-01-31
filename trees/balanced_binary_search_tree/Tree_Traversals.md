# Tree Traversals - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Types of Traversals](#types-of-traversals)
3. [DFS Traversals](#dfs-traversals)
4. [BFS Traversal](#bfs-traversal)
5. [Time & Space Complexity](#time--space-complexity)
6. [Python Implementation](#python-implementation)
7. [Visual Examples](#visual-examples)
8. [LeetCode Interview Problems](#leetcode-interview-problems)
9. [Interview Q&A](#interview-qa)

---

## Introduction

A **tree traversal** is a process of visiting all the nodes in a tree in a specific order. Different traversals are useful for different problems, and understanding when to use each is crucial for interviews.

### Why Tree Traversals Matter
- Foundation for many tree problems
- Building block for complex algorithms
- Frequently asked in interviews
- Critical for tree analysis and manipulation

### Tree Structure Used Throughout
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Types of Traversals

### Classification

```
Tree Traversals
│
├── Depth-First Search (DFS)
│   ├── Pre-order (Root, Left, Right)
│   ├── In-order (Left, Root, Right)
│   └── Post-order (Left, Right, Root)
│
├── Breadth-First Search (BFS)
│   └── Level-order (Queue-based)
│
└── Other
    ├── Vertical Order Traversal
    ├── Diagonal Traversal
    └── Zig-Zag Traversal
```

---

## DFS Traversals

### 1. In-Order Traversal (Left-Root-Right)

**Definition**: Visit left subtree → Visit root → Visit right subtree

**Characteristic**: For **Binary Search Trees**, in-order traversal gives **sorted sequence**

**Example**:
```
      1
     / \
    2   3

In-order: 2 1 3
```

**Use Cases**:
- Get sorted sequence from BST
- Find predecessor/successor
- Validate BST

### 2. Pre-Order Traversal (Root-Left-Right)

**Definition**: Visit root → Visit left subtree → Visit right subtree

**Characteristic**: Root is always first, useful for **tree serialization**

**Example**:
```
      1
     / \
    2   3

Pre-order: 1 2 3
```

**Use Cases**:
- Serialization/copying tree
- Getting prefix expression
- Finding root-first path

### 3. Post-Order Traversal (Left-Right-Root)

**Definition**: Visit left subtree → Visit right subtree → Visit root

**Characteristic**: Root is always last, useful for **deletion** and **tree height**

**Example**:
```
      1
     / \
    2   3

Post-order: 2 3 1
```

**Use Cases**:
- Delete tree (process children first)
- Calculate height/depth
- Postfix expression

---

## BFS Traversal

### Level-Order Traversal (Breadth-First)

**Definition**: Visit all nodes at depth k before visiting nodes at depth k+1

**Characteristic**: Uses **Queue** data structure, perfect for **level-based** problems

**Example**:
```
      1
     / \
    2   3
   / \
  4   5

Level-order: 1 2 3 4 5 (or [[1], [2,3], [4,5]])
```

**Use Cases**:
- Get levels of tree
- Serialize tree level by level
- Find all nodes at distance k
- Binary tree right view

---

## Time & Space Complexity

| Traversal | Time | Space | Notes |
|-----------|------|-------|-------|
| In-order | O(n) | O(h) | h = height, O(n) for skewed |
| Pre-order | O(n) | O(h) | h = height, O(n) for skewed |
| Post-order | O(n) | O(h) | h = height, O(n) for skewed |
| Level-order | O(n) | O(w) | w = max width |

**Where:**
- n = number of nodes
- h = height of tree
- w = maximum width (max nodes at any level)

---

## Python Implementation

### Complete Node Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper to build tree from list (for examples)
def build_tree(values):
    """Build tree from level-order list. None = null node"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            left_val = values[i]
            if left_val is not None:
                node.left = TreeNode(left_val)
            queue.append(node.left) if node.left else None
            i += 1
        if i < len(values):
            right_val = values[i]
            if right_val is not None:
                node.right = TreeNode(right_val)
            queue.append(node.right) if node.right else None
            i += 1
    return root
```

### 1. In-Order Traversal

#### Recursive Approach
```python
def inorder_recursive(root):
    """In-order traversal - recursive"""
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)        # Left
        result.append(node.val)    # Root
        traverse(node.right)       # Right
    
    traverse(root)
    return result

# Time: O(n), Space: O(h)
```

#### Iterative Approach (Using Stack)
```python
def inorder_iterative(root):
    """In-order traversal - iterative using stack"""
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None, pop from stack
        current = stack.pop()
        result.append(current.val)
        
        # Visit right subtree
        current = current.right
    
    return result

# Time: O(n), Space: O(h)
```

#### Morris Traversal (O(1) Space!)
```python
def inorder_morris(root):
    """In-order traversal - Morris (threaded tree) - O(1) space"""
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find predecessor (rightmost in left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Thread exists, remove it
                result.append(current.val)
                predecessor.right = None
                current = current.right
    
    return result

# Time: O(n), Space: O(1)
```

### 2. Pre-Order Traversal

#### Recursive Approach
```python
def preorder_recursive(root):
    """Pre-order traversal - recursive"""
    result = []
    
    def traverse(node):
        if not node:
            return
        result.append(node.val)    # Root
        traverse(node.left)        # Left
        traverse(node.right)       # Right
    
    traverse(root)
    return result

# Time: O(n), Space: O(h)
```

#### Iterative Approach (Using Stack)
```python
def preorder_iterative(root):
    """Pre-order traversal - iterative using stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Time: O(n), Space: O(h)
```

#### Morris Traversal
```python
def preorder_morris(root):
    """Pre-order traversal - Morris (threaded tree) - O(1) space"""
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create thread, add current (pre-order)
                result.append(current.val)
                predecessor.right = current
                current = current.left
            else:
                # Thread exists, remove it
                predecessor.right = None
                current = current.right
    
    return result

# Time: O(n), Space: O(1)
```

### 3. Post-Order Traversal

#### Recursive Approach
```python
def postorder_recursive(root):
    """Post-order traversal - recursive"""
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)        # Left
        traverse(node.right)       # Right
        result.append(node.val)    # Root
    
    traverse(root)
    return result

# Time: O(n), Space: O(h)
```

#### Iterative Approach (Using Two Stacks)
```python
def postorder_iterative_two_stacks(root):
    """Post-order traversal - iterative using two stacks"""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result

# Time: O(n), Space: O(n)
```

#### Iterative Approach (Using One Stack)
```python
def postorder_iterative_one_stack(root):
    """Post-order traversal - iterative using one stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    last_visited = None
    
    while stack:
        current = stack[-1]
        
        # If current is leaf or both children visited
        if not current.left and not current.right:
            result.append(current.val)
            stack.pop()
            last_visited = current
        elif last_visited and (last_visited == current.left or 
                               last_visited == current.right):
            # Children already visited
            result.append(current.val)
            stack.pop()
            last_visited = current
        else:
            # Push children in reverse order (right first)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    
    return result

# Time: O(n), Space: O(h)
```

### 4. Level-Order Traversal (BFS)

#### Basic Level-Order
```python
def levelorder(root):
    """Level-order traversal - returns flat list"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Time: O(n), Space: O(w) where w = max width
```

#### Level-Order with Level Information
```python
def levelorder_with_levels(root):
    """Level-order traversal - returns levels as separate lists"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for i in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Time: O(n), Space: O(w)
```

#### Optimized with deque
```python
from collections import deque

def levelorder_optimized(root):
    """Level-order traversal - optimized with deque"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Time: O(n), Space: O(w)
```

---

## Visual Examples

### Example 1: Complete Tree

```
        1
       / \
      2   3
     / \
    4   5

In-order:   4 2 5 1 3
Pre-order:  1 2 4 5 3
Post-order: 4 5 2 3 1
Level-order: [[1], [2,3], [4,5]]
```

### Example 2: Skewed Tree (Left)

```
    1
   /
  2
 /
3

In-order:   3 2 1
Pre-order:  1 2 3
Post-order: 3 2 1
Level-order: [[1], [2], [3]]
```

### Example 3: Skewed Tree (Right)

```
1
 \
  2
   \
    3

In-order:   1 2 3
Pre-order:  1 2 3
Post-order: 3 2 1
Level-order: [[1], [2], [3]]
```

### Example 4: Complex Tree

```
          1
       /     \
      2       3
     / \     /
    4   5   6
   /     \
  7       8

In-order:       7 4 2 5 8 1 6 3
Pre-order:      1 2 4 7 5 8 3 6
Post-order:     7 4 8 5 2 6 3 1
Level-order:    [[1], [2,3], [4,5,6], [7,8]]
```

---

## LeetCode Interview Problems

### Problem 1: Binary Tree Inorder Traversal (LeetCode 94)

**Difficulty**: Medium | **Frequency**: ⭐⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

**Example**:
```
Input: root = [1,null,2]
    1
     \
      2
Output: [1,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

**Solution 1: Recursive**
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result

# Time: O(n), Space: O(h) - recursion stack
```

**Solution 2: Iterative (Stack)**
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result

# Time: O(n), Space: O(h)
```

**Solution 3: Morris (Optimal Space)**
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        current = root
        
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    result.append(current.val)
                    predecessor.right = None
                    current = current.right
        
        return result

# Time: O(n), Space: O(1)
```

---

### Problem 2: Binary Tree Level Order Traversal (LeetCode 102)

**Difficulty**: Medium | **Frequency**: ⭐⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

**Example**:
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

**Solution: BFS with Queue**
```python
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

# Time: O(n), Space: O(w) - width of tree
```

**Key Points**:
- Track level size before processing
- Process all nodes at current level in one iteration
- Append children to queue for next level

---

### Problem 3: Binary Tree Preorder Traversal (LeetCode 144)

**Difficulty**: Easy | **Frequency**: ⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

**Example**:
```
Input: root = [1,null,2]
    1
     \
      2
Output: [1,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

**Solution 1: Recursive**
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result

# Time: O(n), Space: O(h)
```

**Solution 2: Iterative (Stack)**
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result

# Time: O(n), Space: O(h)
```

---

### Problem 4: Binary Tree Postorder Traversal (LeetCode 145)

**Difficulty**: Easy | **Frequency**: ⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the postorder traversal of its nodes' values.

**Example**:
```
Input: root = [1,null,2]
    1
     \
      2
Output: [2,1]
```

**Solution 1: Recursive**
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        
        dfs(root)
        return result

# Time: O(n), Space: O(h)
```

**Solution 2: Iterative (One Stack)**
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        last_visited = None
        
        while stack:
            current = stack[-1]
            
            if not current.left and not current.right:
                result.append(current.val)
                stack.pop()
                last_visited = current
            elif last_visited and (last_visited == current.left or 
                                   last_visited == current.right):
                result.append(current.val)
                stack.pop()
                last_visited = current
            else:
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        
        return result

# Time: O(n), Space: O(h)
```

---

### Problem 5: Binary Tree Right Side View (LeetCode 199)

**Difficulty**: Medium | **Frequency**: ⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Example**:
```
Input: root = [1,2,3,null,5,null,4]
    1
   / \
  2   3
   \   \
    5   4
Output: [1,3,4]

Explanation: From right side, you see: 1 (root) -> 3 (right of level) -> 4 (right)
```

**Solution: Level-Order BFS**
```python
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Add to result if it's the last node of level
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# Time: O(n), Space: O(w)
```

**Alternative: DFS Approach**
```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # If at new level, add to result
            if level == len(result):
                result.append(node.val)
            
            # Visit right first (to encounter rightmost first)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result

# Time: O(n), Space: O(h)
```

---

### Problem 6: Binary Tree Zigzag Level Order Traversal (LeetCode 103)

**Difficulty**: Medium | **Frequency**: ⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (alternating left-to-right and right-to-left).

**Example**:
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: [[3],[20,9],[15,7]]

Explanation: 
Level 0: 3 (left to right)
Level 1: 20, 9 (right to left - reversed)
Level 2: 15, 7 (left to right)
```

**Solution: BFS with Reverse**
```python
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse if right to left
            if not left_to_right:
                current_level.reverse()
            
            result.append(current_level)
            left_to_right = not left_to_right
        
        return result

# Time: O(n), Space: O(w)
```

---

### Problem 7: Maximum Depth of Binary Tree (LeetCode 104)

**Difficulty**: Easy | **Frequency**: ⭐⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, return its maximum depth. Maximum depth is the number of nodes along the longest path from root to farthest leaf node.

**Example**:
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: 3

Input: root = [1,null,2]
    1
     \
      2
Output: 2
```

**Solution 1: DFS Recursive**
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time: O(n), Space: O(h)
```

**Solution 2: DFS with Post-order**
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            return 1 + max(left_depth, right_depth)
        
        return dfs(root)

# Time: O(n), Space: O(h)
```

**Solution 3: BFS Level-Order**
```python
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

# Time: O(n), Space: O(w)
```

---

### Problem 8: Path Sum (LeetCode 112)

**Difficulty**: Easy | **Frequency**: ⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

**Example**:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,1], targetSum = 22
       5
      / \
     4   8
    /   / \
   11  13  4
  / \      \
 7   2      1

Output: true
Explanation: Path 5->4->11->2 sums to 22

Path Sum: 5+4+11+2 = 22 ✓
```

**Solution 1: DFS Recursive**
```python
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val
            
            # Check if leaf and sum matches
            if not node.left and not node.right:
                return current_sum == targetSum
            
            # Check left and right subtrees
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, 0)

# Time: O(n), Space: O(h)
```

**Solution 2: DFS Iterative (Stack-based)**
```python
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]
        
        while stack:
            node, current_sum = stack.pop()
            
            if not node:
                continue
            
            current_sum += node.val
            
            # Check if leaf and sum matches
            if not node.left and not node.right and current_sum == targetSum:
                return True
            
            if node.right:
                stack.append((node.right, current_sum))
            if node.left:
                stack.append((node.left, current_sum))
        
        return False

# Time: O(n), Space: O(h)
```

---

### Problem 9: Binary Tree Level Order Traversal II (LeetCode 107)

**Difficulty**: Easy | **Frequency**: ⭐⭐

**Problem Statement**:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values (i.e., from left to right, level by level starting from leaf to root).

**Example**:
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: [[15,7],[9,20],[3]]

(Reversed from normal level-order)
```

**Solution: BFS with Reverse**
```python
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result[::-1]  # Reverse the result

# Time: O(n), Space: O(w)
```

---

### Problem 10: Validate Binary Search Tree (LeetCode 98)

**Difficulty**: Medium | **Frequency**: ⭐⭐⭐⭐⭐

**Problem Statement**:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

**Example**:
```
Input: root = [2,1,3]
     2
    / \
   1   3
Output: true

Input: root = [5,1,4,null,null,3,6]
     5
    / \
   1   4
      / \
     3   6
Output: false
Explanation: 4 should not have child 3 which is < 5
```

**Solution 1: In-order Traversal (Sorted Check)**
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # In BST, in-order traversal should be strictly increasing
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        
        return True

# Time: O(n), Space: O(n)
```

**Solution 2: Range Validation (Optimal)**
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Validate left: all values must be < node.val
            # Validate right: all values must be > node.val
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

# Time: O(n), Space: O(h)
```

**Solution 3: Iterative with Stack**
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, min_val, max_val = stack.pop()
            
            if not node:
                continue
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            stack.append((node.right, node.val, max_val))
            stack.append((node.left, min_val, node.val))
        
        return True

# Time: O(n), Space: O(h)
```

---

## Interview Q&A

### Q1: What's the difference between DFS and BFS?

**A:**
| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack | Queue |
| Order | Depth first | Level-first |
| Memory | Can be less for wide trees | Can be more for wide trees |
| When to use | Height, paths, backtracking | Shortest path, levels |
| Traversals | In-order, Pre-order, Post-order | Level-order |

---

### Q2: When would you use each traversal?

**A:**
- **In-order**: Get sorted sequence from BST, LCA problems
- **Pre-order**: Serialize tree, create copy of tree
- **Post-order**: Delete tree, calculate height, postfix expressions
- **Level-order**: Levels, shortest path, printing by levels

---

### Q3: How many ways can you implement in-order traversal?

**A:**
Three main approaches:
1. **Recursive**: Most intuitive, O(h) space for call stack
2. **Iterative (Stack)**: More explicit, same O(h) space
3. **Morris**: O(1) space using threading, most efficient but complex

**Quick Comparison**:
```
Recursive:  Simple, clean, but stack space implicit
Iterative:  Explicit control, same space usage
Morris:     Hardest to understand, but O(1) space
```

---

### Q4: Why is level-order traversal useful?

**A:**
- Processes tree level by level (breadth-first)
- Perfect for problems asking about levels, width, or vertical distance
- Uses queue (simpler than recursion stack management)
- Easy to track depth/level information
- Can solve many "at distance k" type problems

---

### Q5: Explain Morris Traversal and when to use it

**A:**
**Morris Traversal** is an advanced technique using threading:

**Advantages:**
- O(1) space complexity (vs O(h) for normal iterative)
- Still O(n) time complexity
- Modifies tree temporarily (creates threads)

**When to use:**
- Space is critical constraint
- Large trees with limited memory
- Interview to show advanced knowledge

**Drawback:**
- Modifies tree structure temporarily
- More complex to implement
- Not needed for most practical purposes

---

### Q6: Can you convert recursive traversal to iterative without using explicit stack?

**A:**
Yes, using **Morris Traversal**. Example for in-order:

```python
def inorder_morris(root):
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find predecessor (rightmost in left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Thread exists, process and remove
                result.append(current.val)
                predecessor.right = None
                current = current.right
    
    return result
```

---

### Q7: What's time and space complexity for all traversals?

**A:**

| Traversal | Time | Space | Notes |
|-----------|------|-------|-------|
| In-order Recursive | O(n) | O(h) | Stack |
| In-order Iterative | O(n) | O(h) | Explicit stack |
| In-order Morris | O(n) | O(1) | Threading |
| Pre-order Recursive | O(n) | O(h) | Stack |
| Pre-order Iterative | O(n) | O(h) | Stack |
| Pre-order Morris | O(n) | O(1) | Threading |
| Post-order Recursive | O(n) | O(h) | Stack |
| Post-order Iterative | O(n) | O(h) | Stack |
| Level-order (BFS) | O(n) | O(w) | w = max width |

**h = tree height, w = maximum width at any level**

---

### Q8: For a skewed tree (n nodes), what's the space complexity?

**A:**
- Recursive/Iterative: O(n) because height = n
- Morris: O(1) still
- Level-order: O(1) because width = 1 at each level

---

### Q9: How to find if path exists with given sum?

**A:**
Use DFS pre-order traversal with accumulating sum:

```python
def hasPathSum(root, target):
    def dfs(node, current_sum):
        if not node:
            return False
        
        current_sum += node.val
        
        # Check if leaf node
        if not node.left and not node.right:
            return current_sum == target
        
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)
```

---

### Q10: Difference between symmetric tree checking - recursive vs iterative?

**A:**
**Recursive** (Cleaner):
```python
def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                isMirror(left.left, right.right) and 
                isMirror(left.right, right.left))
    
    return isMirror(root.left, root.right)
```

**Iterative** (Explicit queue):
```python
def isSymmetric(root):
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        
        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False
        
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    
    return True
```

---

## Summary Table

### All Traversals Quick Reference

```python
# IN-ORDER: Left → Root → Right (Gives sorted for BST)
recursive:  traverse(node.left); process(node); traverse(node.right)
stack:      while loop to go left first, then process, then right

# PRE-ORDER: Root → Left → Right (Serialization)
recursive:  process(node); traverse(node.left); traverse(node.right)
stack:      push right first, then left (so left processed first)

# POST-ORDER: Left → Right → Root (Deletion)
recursive:  traverse(node.left); traverse(node.right); process(node)
stack:      track last_visited to know when to process

# LEVEL-ORDER: Level by level (BFS)
queue:      process all at level n before level n+1
deque:      use popleft() for O(1) operations
```

---

## Key Takeaways

1. **Know all 5 traversal types** - DFS (3 types) + BFS
2. **Multiple implementations** - Recursive, iterative, Morris
3. **Space vs Time** - Morris saves space but is complex
4. **Understand when to use each** - Different problems need different traversals
5. **LeetCode mastery** - Practice above 10 problems repeatedly
6. **Interview readiness** - Be able to code all variants quickly
7. **Edge cases** - Empty tree, single node, skewed trees
8. **Optimization** - Use deque for BFS, know Morris for advanced candidates

---

## Practice Problems List

**Easy (Foundation)**:
- LeetCode 94: Binary Tree Inorder Traversal
- LeetCode 144: Binary Tree Preorder Traversal
- LeetCode 145: Binary Tree Postorder Traversal
- LeetCode 104: Maximum Depth of Binary Tree
- LeetCode 101: Symmetric Tree

**Medium (Core)**:
- LeetCode 102: Binary Tree Level Order Traversal
- LeetCode 103: Binary Tree Zigzag Level Order Traversal
- LeetCode 107: Binary Tree Level Order Traversal II
- LeetCode 199: Binary Tree Right Side View
- LeetCode 112: Path Sum

**Medium (Advanced)**:
- LeetCode 98: Validate Binary Search Tree
- LeetCode 236: Lowest Common Ancestor
- LeetCode 129: Sum Root to Leaf Numbers
- LeetCode 437: Path Sum III
- LeetCode 113: Path Sum II

**Hard (Expert)**:
- LeetCode 124: Binary Tree Maximum Path Sum
- LeetCode 297: Serialize and Deserialize Binary Tree
- LeetCode 572: Subtree of Another Tree
- LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
- LeetCode 889: Construct Binary Tree from Preorder and Postorder Traversal
