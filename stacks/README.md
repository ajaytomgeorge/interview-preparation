# Stack Problems - Complete Collection

## 1. Valid Parentheses

### Problem Statement

Given a string containing only `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, check if the input string is valid.

**Valid if:**
- Every opening bracket has a matching closing bracket
- Brackets are closed in the correct order

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `"()[]{}"` | `True` | All brackets properly matched |
| `"(]"` | `False` | Mismatched brackets |
| `"({[]})"` | `True` | Proper nesting |

### Stack Idea

1. Use a stack to store opening brackets
2. On encountering a closing bracket:
   - Stack must not be empty
   - Top of stack must match the closing bracket
3. At the end, stack must be empty

### Algorithm

1. Create an empty stack
2. Traverse the string:
   - If opening bracket → push to stack
   - If closing bracket:
     - Stack empty → ❌ invalid
     - Pop stack and check if it matches
3. Stack empty at end → ✅ valid

### Python Code

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(N) |
| **Space** | O(N) |

### One-Line Explanation
"We use a stack to match opening and closing brackets while maintaining order."

### Common Mistakes
- Not checking empty stack before popping
- Forgetting to check leftover elements in stack

---

## 2. Decode String

### Problem Statement

Given an encoded string with the pattern `k[encoded_string]`, decode the string fully.

- `k` = number of repetitions
- `encoded_string` can contain letters or nested patterns

### Examples

| Input | Output |
|-------|--------|
| `"3[a]2[bc]"` | `"aaabcbc"` |
| `"3[a2[c]]"` | `"accaccacc"` |
| `"2[abc]3[cd]ef"` | `"abcabccdcdcdef"` |

### Key Idea

Use two stacks:
- **Count stack** → stores multipliers `k`
- **String stack** → stores previous strings

### Algorithm

1. Traverse characters:
   - **Digit** → build `k` (handle multi-digit numbers with `k = k * 10 + int(ch)`)
   - **`[`** → push current string and k, reset current string
   - **`]`** → pop count & previous string → append repeated substring
   - **Letter** → add to current string

### Why k = k * 10 + int(ch)?

Handles multi-digit numbers like `"12[a]"` or `"203[b]"`. Each new digit shifts previous k one decimal place left and adds the new digit.

Example: `"12[a]"`

| Step | k Calculation | Result |
|------|---------------|--------|
| `'1'` | `0*10 + 1 = 1` | `k = 1` |
| `'2'` | `1*10 + 2 = 12` | `k = 12` ✅ |

Without this formula, only the last digit would be counted → wrong answer.

### Python Solution

```python
def decodeString(s: str) -> str:
    count_stack = []
    string_stack = []
    current_string = ""
    k = 0

    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)   # handle multi-digit numbers
        elif ch == '[':
            count_stack.append(k)
            string_stack.append(current_string)
            current_string = ""
            k = 0
        elif ch == ']':
            count = count_stack.pop()
            prev_string = string_stack.pop()
            current_string = prev_string + current_string * count
        else:
            current_string += ch

    return current_string
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(N * maxK) where N = string length, maxK = max repeat count |
| **Space** | O(N) |

---

## 3. Longest Valid Parentheses

### Problem Statement

Given a string containing only `'('` and `')'`, find the length of the longest valid parentheses substring.

**Valid substring:**
- Parentheses are balanced
- Parentheses are properly nested

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `"(()"` | `2` | Longest valid = `"()"` |
| `")()())"` | `4` | Longest valid = `"()()"` |
| `"((()))"` | `6` | Entire string is valid |
| `"()(()"` | `2` | Longest valid = `"()"` |

### Key Idea

Use a stack to store **indices** (not characters). Keep track of the base index for calculating lengths.

**Why store indices?** We need to calculate the length of valid substrings, so we track positions rather than just brackets.

### Algorithm

1. Initialize stack with `-1` (base index for length calculation)
2. Initialize `max_len = 0`
3. Traverse the string with index `i`:
   - If `'('` → push `i` to stack
   - If `')'` → pop stack
     - If stack becomes empty → push current index (new base)
     - Else → `max_len = max(max_len, i - stack[-1])`
4. Return `max_len`

### Why -1 Exists?

- Acts as base index for valid substring starting at index 0
- Example: `"()"` → length = `1 - (-1) = 2`
- Handles empty stack after unmatched `')'`
- Resets base index for the next potential valid substring

### Python Code

```python
def longestValidParentheses(s: str) -> int:
    stack = [-1]  # base index for length calculation
    max_len = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:  # ch == ')'
            stack.pop()
            if not stack:
                stack.append(i)  # new base after unmatched ')'
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(N) |
| **Space** | O(N) |

---

## 4. Undo/Redo Operations

### Problem Statement

Design a text editor that supports undo and redo operations.

**Operations:**
- Type a character → adds to text
- Undo → reverts the last operation
- Redo → reapplies the last undone operation

### Key Idea

Use two stacks:
- **Undo stack** → stores previous states or actions
- **Redo stack** → stores undone states or actions

### Rules

- **Typing** → push current state to undo stack, clear redo stack
- **Undo** → pop from undo stack, push current state to redo stack
- **Redo** → pop from redo stack, push current state to undo stack

### Example

```
Operations:
Type 'a'    → text = "a"
Type 'b'    → text = "ab"
Undo        → text = "a"
Redo        → text = "ab"
Type 'c'    → text = "abc"     # clears redo stack
Undo        → text = "ab"
```

### Python Implementation

```python
class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.text = ""

    def type(self, char):
        self.undo_stack.append(self.text)
        self.text += char
        self.redo_stack.clear()  # new operation clears redo

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text
```

### Dry Run Example

```python
editor = TextEditor()
editor.type('a')      # text = 'a'
editor.type('b')      # text = 'ab'
editor.undo()         # text = 'a'
editor.redo()         # text = 'ab'
editor.type('c')      # text = 'abc', redo stack cleared
editor.undo()         # text = 'ab'
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(1) per operation |
| **Space** | O(N) |

---

## 5. Redundant Brackets

### Problem Statement

Given an algebraic expression containing brackets and operators (`+`, `-`, `*`, `/`), check if it contains redundant brackets.

**Redundant brackets:** Brackets that do not change the result.

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `"((a+b))"` | `True` | Extra brackets around a+b |
| `"(a+(b))"` | `True` | Brackets around b unnecessary |
| `"(a+b*(c-d))"` | `False` | All brackets needed for precedence |
| `"a+(b+c)"` | `False` | No redundant brackets |

### Key Idea

Use a stack to store characters. When encountering a closing `)`:
- Check elements inside the brackets
- If no operator is found → redundant
- Otherwise → brackets are necessary

### Algorithm

1. Initialize empty stack
2. Traverse the expression character by character:
   - If `ch != ')'` → push to stack
   - If `ch == ')'` → pop until `'('`
     - Track if an operator exists inside
     - If no operator → redundant → return `True`
3. If traversal finishes without finding redundancy → return `False`

### Python Code

```python
def hasRedundantBrackets(expr: str) -> bool:
    stack = []

    for ch in expr:
        if ch == ')':
            top = stack.pop()
            operator_found = False

            # check characters inside brackets
            while top != '(':
                if top in '+-*/':
                    operator_found = True
                top = stack.pop()

            if not operator_found:
                return True  # redundant brackets found
        else:
            stack.append(ch)

    return False
```

### Dry Run Example: `"((a+b))"`

```
Stack starts empty

Process '('  → stack = ['(']
Process '('  → stack = ['(', '(']
Process 'a'  → stack = ['(', '(', 'a']
Process '+'  → stack = ['(', '(', 'a', '+']
Process 'b'  → stack = ['(', '(', 'a', '+', 'b']

Process ')' → pop until '(':
  b → + → a → '('
  Operator found? ✅ Yes → not redundant

Next ')' → pop until '(':
  (
  Operator found inside? ❌ No → redundant → return True
```

### Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(N) |
| **Space** | O(N) |

### Tips

Redundant brackets usually appear around:
- Single variable: `(a)`
- Expression already enclosed: `((a+b))`

---

## Summary Table

| Problem | Approach | Time | Space |
|---------|----------|------|-------|
| Valid Parentheses | Stack + Mapping | O(N) | O(N) |
| Decode String | Two Stacks | O(N×maxK) | O(N) |
| Longest Valid Parentheses | Index Stack | O(N) | O(N) |
| Undo/Redo | Dual Stacks | O(1) | O(N) |
| Redundant Brackets | Stack + Operators | O(N) | O(N) |
