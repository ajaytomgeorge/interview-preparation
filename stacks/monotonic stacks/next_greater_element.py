🧱 Monotonic Stack & Next Greater Element — Summary
📌 What is a Monotonic Stack?

A monotonic stack is a stack that keeps elements in a monotone order:

Increasing stack → elements in increasing order from bottom → top

Decreasing stack → elements in decreasing order from bottom → top

Why use it?

Efficiently find Next Greater / Next Smaller elements

Avoids O(N²) nested loops → solves in O(N)

Key idea:

Maintain candidates in a stack

When current element breaks the monotone order, pop from stack → current element is the answer for popped elements

📌 Problem: Next Greater Element (NGE)

Given an array, for each element, find the first greater element to its right.
If none exists → return -1.

Example:

Input	Output
[2,1,3]	[3,3,-1]
[4,5,2,10]	[5,10,10,-1]
💡 Key Idea / Algorithm

Initialize:

stack = []           # stores indices
result = [-1]*len(arr)  # default -1


Traverse array with index i:

While stack is not empty and arr[i] > arr[stack[-1]]:

Pop index idx = stack.pop()

result[idx] = arr[i]

Push current index i onto stack

After traversal, remaining indices in stack → -1 (no next greater element)

🧩 Python Code
def nextGreaterElement(arr):
    stack = []
    result = [-1] * len(arr)

    for i, val in enumerate(arr):
        while stack and val > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)

    return result

🔹 Dry Run Example: [2,1,3]
Step	Stack	Result	Explanation
0	[0]	[-1,-1,-1]	2 pushed, waiting for NGE
1	[0,1]	[-1,-1,-1]	1 pushed, waiting for NGE
2	[2]	[3,3,-1]	3 > 1 → result[1]=3, pop 1; 3>2→result[0]=3, pop 0
End	[2]	[3,3,-1]	2 has no NGE → -1
⏱ Complexity

Time: O(N) → each element pushed and popped at most once

Space: O(N) → stack stores indices

🎯 One-Line Exam Explanation

“A monotonic stack keeps candidates in decreasing order. For Next Greater Element, pop smaller elements when a bigger number comes, assign the popped indices their NGE, and push the current index.”