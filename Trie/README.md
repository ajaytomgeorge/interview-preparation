# Trie (Prefix Tree) Problems

## 1. Trie Data Structure

### Problem Statement

Design a data structure that supports:
- `insert(word)` → store a word
- `search(word)` → check if word exists exactly
- `startsWith(prefix)` → check if any word starts with given prefix

### Why Not Just Use a Set?

A set gives exact word lookup in O(1) average, but prefix search is expensive (you'd have to check every word).

**Trie solves this efficiently:**
- Search/insert is O(length of word)
- No need to scan all stored words

### Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # dict of char -> TrieNode
        self.end = False        # True if a word ends here
```

- `children` stores next characters
- `end` marks word completion

### Trie Implementation

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end
    
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

### Example Usage

```python
trie = Trie()
trie.insert("apple")
trie.search("apple")       # True
trie.search("app")         # False
trie.startsWith("app")     # True
trie.insert("app")
trie.search("app")         # True
```

### Trie Visualization

After inserting "apple" and "app":

```
(root)
 └─ a
     └─ p
         └─ p*   <- "app" ends here (end=True)
             └─ l
                 └─ e* <- "apple" ends here (end=True)
```

### Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| insert(word) | O(L) | O(L) per node |
| search(word) | O(L) | - |
| startsWith(prefix) | O(L) | - |

Where L = length of word or prefix

**Overall Space:** O(total characters stored)

### Memory Optimization

Use array of size 26 instead of dictionary:

```python
class TrieNodeOptimized:
    def __init__(self):
        self.children = [None] * 26  # a-z only
        self.end = False

    # Access: index = ord(ch) - ord('a')
    # Faster than dict, less memory overhead
```

### Advantages of Trie

1. **Prefix queries:** Find all words with given prefix efficiently
2. **Spell checker:** Quick prefix matching
3. **Autocomplete:** Fast prefix-based suggestions
4. **IP routing:** Longest prefix matching
5. **T9 input:** Mobile phone predictive text

---

## 2. Word Search II (Trie + DFS + Backtracking)

### Problem Statement

Given a 2D board of characters and a list of words, return all words present in the board.

**Rules:**
- Words are formed by adjacent cells (up/down/left/right)
- Same cell cannot be reused in one word
- Many words → brute-force per word is too slow

### Key Insight

✔ Use a Trie to store all words  
✔ Use DFS + backtracking on the board  
✔ Prune paths early if prefix doesn't exist in Trie

### Example

```
Board:
o a a n
e t a e
i h k r
i f l v

Words: ["oath","pea","eat","rain"]

Output: ["oath","eat"]
```

### Algorithm

1. **Build Trie** from word list
2. **For each cell** on board:
   - Start DFS
   - Match characters with Trie nodes
   - Mark visited cells temporarily
   - When Trie node marks end of word → add to result
3. **Backtrack** by unmarking visited cells

### Implementation

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
    res = set()  # Use set to avoid duplicates

    def dfs(r, c, node, path):
        # Found a complete word
        if node.is_word:
            res.add(path)
        
        # Out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        tmp = board[r][c]
        
        # Prefix doesn't exist in Trie
        if tmp not in node.children:
            return
        
        # Mark as visited
        board[r][c] = '#'
        
        # Explore all 4 directions
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(r+dr, c+dc, node.children[tmp], path+tmp)
        
        # Unmark (backtrack)
        board[r][c] = tmp

    # Start DFS from each cell
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "")
    
    return list(res)

# Test
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print(findWords(board, words))
# Output: ['eat', 'oath']
```

### DFS Path Example for "oath"

```
Start at (0,0) = 'o'
    ↓
Move to (0,1) = 'a' → prefix "oa" exists in Trie
    ↓
Move to (1,1) = 't' → prefix "oat" exists in Trie
    ↓
Move to (2,3) = 'h' → prefix "oath" marks word end ✅
    
Add "oath" to result
Backtrack and explore other paths
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Trie Build** | O(sum of word lengths) |
| **DFS Worst** | O(M × N × 4^L) |
| **Practical** | Much faster due to Trie pruning |

Where:
- M, N = board dimensions
- L = max word length

### Key Interview Points

1. **Trie is Critical:** When word list is huge, Trie dramatically reduces search space
2. **Backtracking:** Mark cells visited temporarily, then unmark for other paths
3. **Set for Duplicates:** Prevents returning same word multiple times
4. **Early Pruning:** Most powerful optimization - stop if prefix doesn't exist
5. **Time Tradeoff:** More space for Trie saves enormous time in DFS

### Why This Solution is Efficient

❌ **Bad Approach:** For each word, DFS entire board - O(N × M × L)  
✅ **Trie Approach:** Build Trie once, prune impossible paths during DFS

The Trie acts as a filter - we only explore paths that could form actual words.

---

## Key Concepts Summary

| Concept | Purpose | Complexity |
|---------|---------|-----------|
| **Trie** | Prefix storage & matching | O(L) per operation |
| **DFS** | Explore board paths | O(4^L) worst, pruned by Trie |
| **Backtracking** | Undo choices & explore alternatives | Implicit in DFS |
| **Visited Set** | Prevent cell reuse | O(1) lookup |

### Follow-up Questions

1. **How to optimize memory?** Use array instead of dict for children
2. **Handle case sensitivity?** Convert to lowercase during insertion/search
3. **Large word list?** Build Trie once, reuse for multiple boards
4. **Find longest word?** Track maximum length during DFS

---

## Related Problems

1. **Valid Word Square**
2. **Regex Pattern Matching**
3. **Implement Magic Dictionary**
4. **Palindrome Pairs**
5. **Replace Words**
