Longest Valid Parentheses📌 Problem

Given a string containing only '(' and ')', find the length of the longest valid parentheses substring.

Valid substring:

Parentheses are balanced

Parentheses are properly nested

🔹 Examples
Input	Output	Explanation
"(()"	2	Longest valid = "()"
")()())"	4	Longest valid = "()()"
"((()))"	6	Entire string is valid
"()(()"	2	Longest valid = "()"
"(((())))"	8	Entire string is valid
💡 Key Idea

Use a stack to store indices (not characters)

Keep track of the base index for calculating lengths

Push -1 at start to handle:

Valid substrings starting at index 0

Length calculations when stack becomes empty

🧠 Algorithm

Initialize stack with -1

Initialize max_len = 0

Traverse the string with index i:

If '(' → push i to stack

If ')' → pop stack

If stack becomes empty → push current index (new base)

Else → max_len = max(max_len, i - stack[-1])

Return max_len

🧩 Python Code
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

🔹 Why -1 Exists

Acts as base index for valid substring starting at index 0

Example: "()" → length = 1 - (-1) = 2

Handles empty stack after unmatched ')'

Resets base index for the next potential valid substring

Simplifies calculation using formula length = i - stack[-1]

⏱ Complexity

Time: O(N) → traverse string once

Space: O(N) → stack stores indices

🎯 One-Line Explanation (Exam)

“We use a stack to track indices, push -1 as base, pop on ')', and calculate lengths using i - stack[-1] to find the longest valid substring.”

If you want, the next stack problem we can solve is:
Check Redundant Brackets (Valid Expression) — very useful after parentheses problems.

Do you want me to continue with that?