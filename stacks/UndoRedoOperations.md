# Undo/Redo Operations

## Problem Statement

Design a text editor that supports undo and redo operations.

**Operations:**
- Type a character → adds to text
- Undo → reverts the last operation
- Redo → reapplies the last undone operation

**Goal:** Implement efficient undo/redo using stacks.

## Key Idea

Use **two stacks**:
- **Undo stack** → stores previous states or actions
- **Redo stack** → stores undone states or actions

**Rules:**
- Typing → push current state to undo stack, clear redo stack
- Undo → pop from undo stack, push current state to redo stack
- Redo → pop from redo stack, push current state to undo stack

## Example

```
Operations:

Type 'a' → text = "a"
Type 'b' → text = "ab"
Undo      → text = "a"
Redo      → text = "ab"
Type 'c' → text = "abc"  # clears redo stack
Undo      → text = "ab"
```

## Algorithm

**Initialize:**
```
undo_stack = []
redo_stack = []
current_text = ""
```

**Type a char:**
```
undo_stack.append(current_text)
current_text += char
redo_stack.clear()
```

**Undo:**
```
redo_stack.append(current_text)
current_text = undo_stack.pop()
```

**Redo:**
```
undo_stack.append(current_text)
current_text = redo_stack.pop()
```

## Python Implementation

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

## Dry Run Example

```python
editor = TextEditor()
editor.type('a')      # text = 'a'
editor.type('b')      # text = 'ab'
editor.undo()         # text = 'a'
editor.redo()         # text = 'ab'
editor.type('c')      # text = 'abc'
editor.undo()         # text = 'ab'
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Type | O(1) | O(1) per char |
| Undo | O(1) | — |
| Redo | O(1) | — |
| **Overall** | **O(1) per operation** | **O(N)** where N = total chars |

## Key Points

- Typing a new character clears the redo stack (no redo after new input)
- Both undo and redo are O(1)
- Space grows with each character typed
