🧱 Decode String — Summary
📌 Problem Statement

Given an encoded string with the pattern:

k[encoded_string]


k = number of repetitions

encoded_string can contain letters or nested patterns

Decode the string fully and return it

Examples:

Input	Output
"3[a]2[bc]"	"aaabcbc"
"3[a2[c]]"	"accaccacc"
"2[abc]3[cd]ef"	"abcabccdcdcdef"
💡 Key Idea

Use two stacks:

Count stack → stores multipliers k

String stack → stores previous strings

Traverse characters:

Digit → build k (handle multi-digit numbers)

'[' → push current string and k, reset current string

']' → pop count & previous string → append repeated substring

Letter → add to current string

🔹 Why k = k * 10 + int(ch)

Handles multi-digit numbers like "12[a]" or "203[b]"

Each new digit shifts previous k one decimal place left and adds the new digit

Example: "12[a]"

Step	k Calculation
'1'	0*10 + 1 = 1
'2'	1*10 + 2 = 12 ✅

Without k * 10 + int(ch), only last digit would be counted → wrong answer.

🧩 Python Solution
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

⏱ Complexity

Time: O(N * maxK) → N = string length, maxK = max repeat count

Space: O(N) → stacks store previous strings and counts

🎯 One-Line Exam Explanation

“We use two stacks: one for counts and one for previous strings. Digits are accumulated using k = k*10 + int(ch) to handle multi-digit numbers. On ']', we repeat the current string and append it to the previous string.”