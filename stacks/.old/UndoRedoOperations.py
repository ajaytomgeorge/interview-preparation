📌 Problem Statement

Design a text editor that supports undo and redo operations.

Operations:

Type a character → adds to text

Undo → reverts the last operation

Redo → reapplies the last undone operation

Goal: Implement efficient undo/redo using stacks.

💡 Key Idea

Use two stacks:

Undo stack → stores previous states or actions

Redo stack → stores undone states or actions

Rules:

Typing → push current state to undo stack, clear redo stack

Undo → pop from undo stack, push current state to redo stack

Redo → pop from redo stack, push current state to undo stack

🔹 Example

Operations:

Type 'a' → text = "a"
Type 'b' → text = "ab"
Undo      → text = "a"
Redo      → text = "ab"
Type 'c' → text = "abc"  # clears redo stack
Undo      → text = "ab"

🧠 Algorithm

Initialize:

undo_stack = []
redo_stack = []
current_text = ""


Type a char →

undo_stack.append(current_text)

current_text += char

redo_stack.clear()

Undo →

redo_stack.append(current_text)

current_text = undo_stack.pop()

Redo →

undo_stack.append(current_text)

current_text = redo_stack.pop()

🧩 Python Implementation
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

🔹 Dry Run Example
editor = TextEditor()
editor.type('a')      # text = 'a'
editor.type('b')      # text = 'ab'
editor.undo()         # text = 'a'
editor.redo()         # text = 'ab'
editor.type('c')      # text = 'abc', redo stack cleared
editor.undo()         # text = 'ab'

⏱ Complexity

Time: O(1) per operation

Space: O(N) → stacks store text states

🎯 One-Line Exam Explanation

“We use two stacks: undo stack stores previous states, redo stack stores undone states. Typing clears redo. Undo/redo pops and pushes between stacks to manage states efficiently.”

Next, we can move to Monotonic Stack problems, starting with Next Greater Element, which is also very common in interviews.