# Word Search II (Trie + DFS)

## Problem (LeetCode 212 – Word Search II)

Given a 2D board of characters and a list of words, return all words present in the board.

### Rules
- Words are formed by adjacent cells (up/down/left/right)
- Same cell cannot be reused
- Many words → brute-force per word is too slow

## Key Insight

✔ Use a **Trie** to store all words  
✔ Use **DFS + backtracking** on the board  
✔ **Prune paths** early if prefix doesn't exist  

## Approach

1. Build Trie from word list
2. For each cell:
   - DFS while matching Trie nodes
   - When a Trie node marks a word → add to result
   - Mark visited cells temporarily
3. Time Complexity: O(M * N * 4^L) worst case, but heavily pruned

---

## Problem Recap

### Input

```python
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]
```

### Output

```python
["oath","eat"]
```

### Rules
- Words are formed by connecting letters vertically or horizontally
- No cell can be reused
- Board can be large, word list can be huge → we need efficient search

---

## Step 1: Build a Trie

A Trie stores all words in a tree-like structure.  
Each node represents a character. Nodes that end a word have a flag `is_word`.

### Example

**Words:** `["oath","eat","pea","rain"]`

```
Trie:
(root)
├─ o
│  └─ a
│     └─ t
│        └─ h*   <- '*' marks end of word "oath"
├─ e
│  └─ a
│     └─ t*      <- "eat"
├─ p
│  └─ e
│     └─ a*      <- "pea"
└─ r
   └─ a
      └─ i
         └─ n*   <- "rain"
```

**Trie helps:**
- Quickly check if a prefix exists → prune DFS early
- Find complete words without scanning all words each time

---

## Step 2: DFS + Backtracking on the Board

**Idea:**
- For each cell `(i,j)`, try to build words following up/down/left/right directions
- At each step, check if the current prefix exists in the Trie:
  - ✅ If yes → continue
  - ❌ If no → stop (prune)
- When a Trie node marks the end of a word, add it to the result
- Mark cells visited temporarily to prevent reusing the same cell in the same word

---

## Step 3: Visual Example

**Board:**
```
o a a n
e t a e
i h k r
i f l v
```

**Words:** `["oath","eat","pea","rain"]`

### Starting DFS at (0,0) = 'o'

1. Current prefix: `'o'` → exists in Trie ✔
2. Move right → `'oa'` → exists ✔
3. Move down → `'oat'` → exists ✔
4. Move down → `'oath'` → ✅ complete word → add "oath" to result
5. Backtrack → mark cells as unvisited to explore other paths

### DFS visualization (simplified path for "oath")

```
(o) a a n
e   t a e
i   h k r
i   f l v

Start at (0,0) = 'o'
→ (0,1) = 'a'
→ (1,2) = 't'  (Move down-left via nearby indices)
→ (2,3) = 'h' → found "oath"
```

---

## Step 4: Implementation (Python)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    rows, cols = len(board), len(board[0])
    res = set()  # use set to avoid duplicates

    def dfs(r, c, node, path):
        if node.is_word:
            res.add(path)
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        tmp = board[r][c]
        if tmp not in node.children:
            return
        board[r][c] = '#'  # mark visited
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            dfs(r+dr, c+dc, node.children[tmp], path+tmp)
        board[r][c] = tmp  # unmark

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "")
    
    return list(res)
```

### Test

```python
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print(findWords(board, words))
```

### Output

```
['eat', 'oath']
```

---

## Step 5: Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| **Trie build** | O(sum(len(word) for word in words)) |
| **DFS worst case** | O(M * N * 4^L) |
| **DFS practical** | Much faster due to Trie pruning |
| **Space - Trie** | O(sum(len(word))) |
| **Space - DFS recursion** | O(L) |

Where:
- M, N = board dimensions
- L = max word length

---

## ✅ Key Interview Points

1. **Trie is critical** when words list is huge
2. **Backtracking** prevents revisiting cells
3. **Using set** avoids duplicates (same word found multiple times)
4. **Efficient prefix pruning** drastically reduces search space
5. DFS is combined with backtracking to explore all paths while maintaining the invariant that no cell is used twice in one word
