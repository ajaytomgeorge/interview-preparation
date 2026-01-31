# Stack Problem: Check Redundant Brackets

## Problem Statement

Given an algebraic expression containing brackets and operators (`+`, `-`, `*`, `/`), check if it contains **redundant brackets**.

**Redundant brackets:** Brackets that do not change the result.

- Example: `"((a+b))"` → redundant
- Example: `"(a+(b*c))"` → not redundant

## Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `"((a+b))"` | `True` | Extra brackets around `a+b` |
| `"(a+(b))"` | `True` | Brackets around `b` unnecessary |
| `"(a+b*(c-d))"` | `False` | All brackets needed for precedence |
| `"a+(b+c)"` | `False` | No redundant brackets |

## Key Idea

Use a stack to store characters.

When encountering a closing `)`:
- Check elements inside the brackets
- If no operator is found → redundant
- Else → brackets are necessary

Push everything else onto the stack.

## Algorithm (Step by Step)

1. Initialize empty stack
2. Traverse the expression character by character:
   - If `ch != ')'` → push to stack
   - If `ch == ')'` → pop until `'('`
     - Track if an operator exists inside
     - If no operator inside → redundant → return `True`
3. If traversal finishes without finding redundancy → return `False`

## Python Code

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

## Dry Run Example: "((a+b))"

```
Stack starts empty

Process '('   → stack = ['(']
Process '('   → stack = ['(', '(']
Process 'a'   → stack = ['(', '(', 'a']
Process '+'   → stack = ['(', '(', 'a', '+']
Process 'b'   → stack = ['(', '(', 'a', '+', 'b']

Process ')'   → pop until '(':
  - b → (not operator)
  - + → operator_found = True ✅
  - a → (not operator)
  - '(' → stop

Next ')' → pop until '(':
  - '(' → stop (nothing popped)
  
operator_found = False → redundant → return True ✅
```

## Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(N) |
| **Space** | O(N) → stack stores characters |

## One-Line Exam Explanation

"We use a stack and check each pair of brackets: if no operator exists inside, the brackets are redundant."

## Tip

Redundant brackets usually appear around:
- Single variable: `(a)`
- Expression already enclosed: `((a+b))`
