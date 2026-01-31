# Stack Problem 1: Valid Parentheses

## Problem Statement

Given a string containing only:
- `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`

Check if the input string is valid.

**Valid if:**
- Every opening bracket has a matching closing bracket
- Brackets are closed in the correct order

## Examples

| Input | Output | Note |
|-------|--------|------|
| `"()[]{}"` | `True` | Simple valid case |
| `"(]"` | `False` | Mismatch |
| `"({[]})"` | `True` | Properly nested |

## Stack Idea

Use a stack:
- Push opening brackets
- On closing bracket:
  - Stack must not be empty
  - Top of stack must match the closing bracket

## Algorithm

1. Create an empty stack
2. Traverse the string:
   - If opening bracket → push to stack
   - If closing bracket:
     - Stack empty → ❌ invalid
     - Pop stack and check match
3. At the end:
   - Stack empty → ✅ valid
   - Else → ❌ invalid

## Python Code (Exam Ready)

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

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(N) |
| **Space** | O(N) |

## One-Line Explanation (Exam)

"We use a stack to match opening and closing brackets while maintaining order."

## Common Mistakes

- ❌ Not checking empty stack before popping
- ❌ Forgetting to check leftover elements in stack
