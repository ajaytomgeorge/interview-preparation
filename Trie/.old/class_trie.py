2️⃣ Word Prefixes (Classic Trie)
Problem

Design a data structure that supports:

insert(word)

search(word)

startsWith(prefix)

Trie Node Structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

Key Insight

Prefix search is O(length of prefix)

Trie beats hash-set when prefix queries dominate

Common Follow-up

❓ How to optimize memory?
✔ Use array of size 26 instead of dict
✔ Use bitmask to represent children presence





1️⃣ Problem

We need a data structure that supports:

insert(word) → store a word

search(word) → check if word exists exactly

startsWith(prefix) → check if any word starts with given prefix

Why not just use a set?

Set gives exact word lookup in O(1) average

But prefix search is expensive in a set → you’d have to check every word

Trie solves prefix search efficiently:

Search/insert is O(length of word)

No need to scan all stored words

2️⃣ Trie Node Structure
class TrieNode:
    def __init__(self):
        self.children = {}  # dict of char -> TrieNode
        self.end = False    # True if a word ends here


children stores next characters

end marks word completion

3️⃣ Trie Structure
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

4️⃣ Example Usage
trie = Trie()
trie.insert("apple")
trie.search("apple")   # True
trie.search("app")     # False
trie.startsWith("app") # True
trie.insert("app")
trie.search("app")     # True


Trie after inserting "apple" and "app":

(root)
 └─ a
     └─ p
         └─ p*   <- "app" ends here
             └─ l
                 └─ e* <- "apple" ends here

5️⃣ Complexity
Operation	Time Complexity
insert(word)	O(L)
search(word)	O(L)
startsWith(pre)	O(L)

L = length of word or prefix

Space Complexity:

O(total characters stored)

Dict for children can be memory-heavy if many nodes

6️⃣ Memory Optimization

Use array of size 26 instead of dict

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # a-z
        self.end = False


Access: index = ord(ch) - ord('a')

Faster than dict, less memory overhead for each node