# Trie - Word Prefixes (Classic Trie)

## Problem

Design a data structure that supports:
- `insert(word)` - store a word
- `search(word)` - check if word exists exactly
- `startsWith(prefix)` - check if any word starts with given prefix

## Why Not Just Use a Set?

- Set gives exact word lookup in O(1) average
- But **prefix search is expensive** in a set → you'd have to check every word
- **Trie solves prefix search efficiently:**
  - Search/insert is O(length of word)
  - No need to scan all stored words

---

## Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # dict of char -> TrieNode
        self.end = False    # True if a word ends here
```

**Explanation:**
- `children` stores next characters
- `end` marks word completion

---

## Trie Structure

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

---

## Example Usage

```python
trie = Trie()
trie.insert("apple")
trie.search("apple")   # True
trie.search("app")     # False (not a complete word)
trie.startsWith("app") # True (prefix exists)
```

---

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| **insert(word)** | O(len(word)) | O(len(word)) |
| **search(word)** | O(len(word)) | O(1) |
| **startsWith(prefix)** | O(len(prefix)) | O(1) |

---

## Key Insight

Prefix search is O(length of prefix) - **much better than scanning all words!**

---

## Common Follow-up Questions

### ❓ How to optimize memory?

**Option 1:** Use array of size 26 instead of dict
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # a-z only
        self.end = False
```

**Trade-off:** Uses more memory but faster lookup for English letters.

**Option 2:** Use bitmask to represent children presence
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.mask = 0  # bitmask for which children exist
```
