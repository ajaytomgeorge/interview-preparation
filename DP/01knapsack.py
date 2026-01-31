🧠 0/1 Knapsack — Complete Exam Summary
📌 Problem Statement

You are given:

n items

Each item has:

wt[i] → weight

val[i] → value

A knapsack with maximum capacity W

👉 Goal:
Find the maximum total value that can be put in the knapsack without exceeding weight W.

⚠️ Each item can be chosen at most once (0/1 choice).

💡 DP Idea

At every item, you have two choices:

Take the item

Do not take the item

Dynamic Programming is used because:

Subproblems repeat

Optimal solution depends on optimal solutions of smaller subproblems

🧱 DP State Definition
dp[i][w] = maximum value using first i items with weight limit w

🔁 DP Transition (MOST IMPORTANT PART)
🔹 Option 1: Do NOT take item i
dp[i][w] = dp[i-1][w]


✔ Meaning:

Skip the current item

Best value remains what we already computed using previous items

🔹 Option 2: Take item i (only if wt[i] ≤ w)
dp[i][w] = val[i] + dp[i-1][w - wt[i]]


✔ Meaning:

Add value of current item

Reduce remaining weight

Use previous items only (0/1 constraint)

🔹 Final Recurrence
dp[i][w] = max(
    dp[i-1][w], 
    val[i] + dp[i-1][w - wt[i]]
)

🟢 Base Cases

dp[0][w] = 0 → no items → no value

dp[i][0] = 0 → no capacity → no value

🧩 Python Code (2D DP)
def knapsack(wt, val, W):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):

            # Case 1: Do not take item i
            dp[i][w] = dp[i - 1][w]

            # Case 2: Take item i (if possible)
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    val[i - 1] + dp[i - 1][w - wt[i - 1]]
                )

    return dp[n][W]

🔍 SPECIAL Explanation of Key Code Lines
🔹 Why dp[i-1][w]?
dp[i][w] = dp[i - 1][w]


➡️ If we skip the current item, we reuse the best solution from previous items for the same weight.

🔹 Why val[i-1] + dp[i-1][w - wt[i-1]]?
val[i - 1] + dp[i - 1][w - wt[i - 1]]


➡️ If we take the item:

Add its value

Reduce remaining weight

Use only previous items (0/1 rule)

🔹 Why max(...)?
dp[i][w] = max(not_take, take)


➡️ We always choose the best of the two choices

⏱ Complexity
Metric	Value
Time	O(n * W)
Space	O(n * W)
🎯 One-Line Exam Explanation

“At each item, choose to take or skip it. DP stores the maximum value for each weight limit using previous items.”

⏱ Time Complexity of 0/1 Knapsack
Standard DP Solution
for i in range(n):
    for w in range(W):
        ...

✅ Time Complexity
𝑂
(
𝑛
×
𝑊
)
O(n×W)
	​


Where:

n = number of items

W = knapsack capacity (max weight)

📦 Space Complexity

2D DP: O(n × W)

Optimized 1D DP: O(W)


❗ Why Knapsack Is “Pseudo-Polynomial”

0/1 Knapsack is NP-Hard, and DP works only because:

W is small enough

Inputs are bounded

This is why:

Knapsack DP is pseudo-polynomial, not truly polynomial.
❗ What Does Pseudo-Polynomial Mean?

Pseudo-polynomial does NOT mean “works for lower bounds only.”
That’s a very common confusion.

✅ Correct Meaning

An algorithm is pseudo-polynomial if:

Its running time is polynomial in the numeric value of the input,
not in the size of the input (number of bits).

🔹 True Polynomial vs Pseudo-Polynomial
Input example:
W = 1,000,000

Input size (bits):
log₂(1,000,000) ≈ 20 bits

1️⃣ True Polynomial Algorithm

Runs in:

O(n³) or O(n²)


Depends only on number of inputs — not their numeric values.

2️⃣ Knapsack DP Algorithm

Runs in:

O(n × W)


Here’s the problem:

W is a value, not input size

Input size of W is log(W), not W

So:

O(n × W) ≠ O(n × log W)


❌ That makes it not truly polynomial

🔹 Why 0/1 Knapsack Is NP-Hard

The general 0/1 Knapsack problem is NP-Hard

No known algorithm solves it in true polynomial time

DP works only when:

W is small

Values are bounded

What Do We Do in Real Systems?
✅ 1. Use 1D DP
dp = [0] * (W + 1)


✔ Saves memory
❌ Time still O(n × W)

✅ 2. Approximation / Greedy (when allowed)

Fractional knapsack (not 0/1)

Heuristics

✅ 3. Meet-in-the-Middle

Split items into two halves

Used when n ≈ 40–50

✅ 4. Constraints Matter (INTERVIEW GOLD)

Interviewers expect you to say this:

“This DP works only when W is reasonably small. If n or W is very large, we need approximations or different strategies.”

🎯 Interview-Perfect Answer (Memorize This)

“The time complexity is O(n×W). If the number of items is very large, this approach becomes infeasible. The algorithm is pseudo-polynomial and works only when W is small. For large inputs, approximation or heuristic methods are required


