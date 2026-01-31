Trie1️⃣ Word Search (Trie + DFS)
Problem (LeetCode 212 – Word Search II)

Given a 2D board of characters and a list of words, return all words present in the board.

Rules

Words are formed by adjacent cells (up/down/left/right)

Same cell cannot be reused

Many words → brute-force per word is too slow

Key Insight

✔ Use a Trie to store all words
✔ Use DFS + backtracking on the board
✔ Prune paths early if prefix doesn’t exist

Approach

Build Trie from word list

For each cell:

DFS while matching Trie nodes

When a Trie node marks a word → add to result

Mark visited cells temporarily

Time Complexity

Trie build: O(sum(word lengths))

DFS: O(M * N * 4^L) worst case, but heavily pruned


erfect! Let’s solve Word Search II (LeetCode 212) step by step, with Trie + DFS + backtracking, and I’ll explain everything clearly and even show a diagram to visualize the process.

Problem Recap

Input:

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]


Output:

["oath","eat"]


Rules:

Words are formed by connecting letters vertically or horizontally

No cell can be reused

Board can be large, word list can be huge → we need efficient search

Step 1: Build a Trie

A Trie stores all words in a tree-like structure.
Each node represents a character. Nodes that end a word have a flag is_word.

Example:

Words: ["oath","eat","pea","rain"]

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


Trie helps:

Quickly check if a prefix exists → prune DFS early

Find complete words without scanning all words each time

Step 2: DFS + Backtracking on the Board

Idea:

For each cell (i,j), try to build words following up/down/left/right directions

At each step, check if the current prefix exists in the Trie:

✅ If yes → continue

❌ If no → stop (prune)

When a Trie node marks the end of a word, add it to the result

Mark cells visited temporarily to prevent reusing the same cell in the same word

Step 3: Visual Example

Board:

o a a n
e t a e
i h k r
i f l v


Words: ["oath","eat","pea","rain"]

Starting DFS at (0,0) = 'o':

Current prefix: 'o' → exists in Trie

Move right → 'oa' → exists

Move down → 'oat' → exists

Move down → 'oath' → ✅ complete word → add "oath" to result

Backtrack → mark cells as unvisited to explore other paths

DFS visualization (simplified path for "oath"):

(o) a a n
e t a e
i h k r
i f l v


Step by step:

Start at (0,0) = 'o'

(0,1) = 'a'

(1,2) = 't'

(2,3) = 'h' → found "oath"

Then continue DFS for other starting points.

Step 4: Implementation (Python)
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

# Test
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print(findWords(board, words))


Output:

['eat', 'oath']

Step 5: Complexity Analysis

Trie build: O(sum(len(word) for word in words))

DFS worst case: O(M * N * 4^L)

M,N = board dimensions

L = max word length

But practically pruned by Trie → much faster

Space Complexity:

Trie: O(sum(len(word)))

DFS recursion stack: O(L)

✅ Key Interview Points

Trie is critical when words list is huge

Backtracking prevents revisiting cells

Using set avoids duplicates (same word found multiple times)

Efficient prefix pruning drastically reduces search space

If you want, I can draw a full step-by-step DFS path diagram for the board showing exactly which cells are visited at each step, like a visual tree. This helps for interview explanations.

Do you want me to do that?