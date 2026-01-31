# Pointer Problems

## 1. Check Anagrams

### Problem Statement

Two strings are anagrams if they contain the same characters with the same frequencies (in any order).

**Examples:**
- `"listen"` and `"silent"` → Anagrams ✓
- `"hello"` and `"world"` → Not anagrams ✗
- `"abc"` and `"def"` → Not anagrams ✗

### Approach: Character Frequency Counting

Use a dictionary to count character frequencies in the first string, then verify the second string has the same frequencies.

### Algorithm

1. Check if lengths are equal (anagrams must have same length)
2. Build frequency map for first string
3. For each character in second string:
   - Decrement its count in the map
   - If count goes negative or character not found → not an anagram
4. Return true if all characters matched

### Python Solution

```python
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    # Build frequency map for s1
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    # Verify s2 matches
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True

# Examples
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) where n = length of strings |
| **Space** | O(1) to O(26) for lowercase English (constant) |

### Alternative: Using Counter

```python
from collections import Counter

def are_anagrams_simple(s1, s2):
    return Counter(s1) == Counter(s2)
```

**Tradeoff:** Simpler code but creates two separate Counter objects.

---

## 2. Find All Anagrams of a Word

### Problem Statement

Given a word and a list of words, find all words in the list that are anagrams of the given word.

### Examples

```
word = "listen"
word_list = ["silent", "hello", "enlist", "world", "inlets"]

Output: ["silent", "enlist", "inlets"]
```

### Algorithm

1. Build frequency map for the target word
2. For each word in the list:
   - Compare its frequency map with target
   - Add to result if they match

### Python Solution

```python
def find_anagrams(word, word_list):
    def freq_map(s):
        m = {}
        for ch in s:
            m[ch] = m.get(ch, 0) + 1
        return m

    target = freq_map(word)
    result = []

    for w in word_list:
        if freq_map(w) == target:
            result.append(w)

    return result

# Example
word_list = ["silent", "hello", "enlist", "world", "inlets"]
print(find_anagrams("listen", word_list))  
# Output: ["silent", "enlist", "inlets"]
```

### Optimized Version with Counter

```python
from collections import Counter

def find_anagrams_optimized(word, word_list):
    target = Counter(word)
    return [w for w in word_list if Counter(w) == target]
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n × m) where n = list length, m = avg word length |
| **Space** | O(1) for each frequency map (alphabet size) |

---

## 3. Longest Common Substring Using Pointers

### Problem Statement

Find the length of the longest substring that appears in both strings.

### Examples

```
s1 = "abcdexyzde"
s2 = "abcdefg"

Common substrings: "abc", "abcde" (longest = 5)
```

### Two-Pointer Approach

Use two pointers, one for each string, to track common characters:

```python
def longest_common_substring(s1, s2):
    max_length = 0
    
    # Try starting from each position in s1
    for i in range(len(s1)):
        for j in range(len(s2)):
            length = 0
            # Match characters from position i and j
            while (i + length < len(s1) and 
                   j + length < len(s2) and 
                   s1[i + length] == s2[j + length]):
                length += 1
            max_length = max(max_length, length)
    
    return max_length
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n × m × k) where n, m = string lengths, k = common substring |
| **Space** | O(1) |

---

## Key Insights for Pointer Problems

| Problem | Key Idea | Approach |
|---------|----------|----------|
| **Anagrams** | Char frequency match | Dictionary counting |
| **Find Anagrams** | Compare all words | Frequency map comparison |
| **Longest Common** | Expand from each position | Nested pointers |

### Common Patterns

1. **Frequency Counting:** For matching characters/patterns
2. **Two Pointer Comparison:** For parallel traversal
3. **Hash Maps:** For O(1) lookups instead of nested loops

### Interview Tips

- Always check length equality first for anagrams
- Consider sorted string as alternative: `sorted(s1) == sorted(s2)`
- Use Counter from collections for cleaner code
- Discuss space-time tradeoffs with interviewer

---

## Related Problems

1. **Valid Anagram** ✓ (covered above)
2. **Group Anagrams** - Partition list into anagram groups
3. **Find Anagram Mappings** - Find correspondence between anagrams
4. **Palindrome Permutation** - Check if string can be rearranged to palindrome
5. **Uncommon from Two Sentences** - Find unique characters between strings
