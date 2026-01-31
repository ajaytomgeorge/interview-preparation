# Dynamic Programming Problems

---

## Practical Limits: When Each Approach Becomes Infeasible

Before implementing any knapsack solution, understand the real-world limits. Below are **order-of-magnitude thresholds** assuming:
- Single modern CPU
- Seconds to minutes of runtime
- Reasonably optimized code
- Exact solution (unless noted)

### 1️⃣ Brute Force (Try All Subsets)

**Complexity:** O(2ⁿ)

**Practical Limits:**

| Items (n) | Feasible? | Time Estimate | Why |
|-----------|-----------|---------------|-----|
| ≤ 20 | ✅ | < 1 second | ~1 million subsets |
| 25 | ✅ | ~1 second | ~33 million subsets |
| 30 | ⚠️ | ~30 seconds | ~1 billion subsets (borderline) |
| 35 | ❌ | ~18 minutes | 34 billion subsets |
| 40 | ❌ | ~18 hours | 1 trillion subsets |

**Rule of Thumb:** Brute force dies hard around **30 items**

**When to Use:**
- ✅ Interview proof-of-concept
- ✅ Educational purposes
- ❌ Production (except very small inputs)

---

### 2️⃣ Dynamic Programming (Capacity-Based)

**Complexity:** O(n × capacity)

**Limiting Factor:** Capacity size matters MORE than items

**Practical Limits:**

| Items | Capacity | Total Ops | Feasible? |
|-------|----------|-----------|-----------|
| 100 | 10⁴ | 10⁶ | ✅ Fast |
| 1,000 | 10⁵ | 10⁸ | ✅ Acceptable |
| 10,000 | 10⁵ | 10⁹ | ⚠️ Slow but works |
| Any | 10⁶ | ~10⁹ | ⚠️ Slow |
| Any | 10⁷ | ~10¹⁰ | ❌ Too slow |
| Any | ≥ 10⁸ | Massive | ❌ Out of memory |

**Memory Constraints:**

```
Memory = n × capacity × 8 bytes (for 64-bit integers)

1,000 items, capacity 10⁵: 800 MB ✅
10,000 items, capacity 10⁵: 8 GB ⚠️
1,000 items, capacity 10⁶: 8 GB ⚠️
10,000 items, capacity 10⁶: 80 GB ❌
```

**Rule of Thumb:** DP works well when **capacity ≤ 10⁶** (ideally ≤ 10⁵)

**Why it's called "Pseudo-Polynomial":**
- Polynomial in n and W separately
- But W can be exponentially large compared to n
- So overall not truly polynomial

**When to Use:**
- ✅ Small to medium capacity (≤ 10⁶)
- ✅ Large number of items (n up to 10⁴)
- ❌ Huge capacities (W ≥ 10⁷)

---

### 3️⃣ Greedy (Ratio-Based)

**Complexity:** O(n log n)

**Practical Limits:**

| Items | Feasible? | Time |
|-------|-----------|------|
| 10⁶ | ✅ | < 1 second |
| 10⁷ | ✅ | ~10 seconds |
| 10⁸ | ✅ | ~100 seconds |
| 10⁹ | ⚠️ | Memory bound |

**Rule of Thumb:** Greedy scales **almost infinitely** (limited mainly by memory and sorting)

**Critical Caveat:**
- ❌ **NOT exact for 0/1 Knapsack** (can be 50% off)
- ✅ **EXACT for Fractional Knapsack** (can take partial items)
- ✅ Good for **approximation** when optimality not required

**When to Use:**
- ✅ Fractional knapsack (exact)
- ✅ 0/1 knapsack when approx is ok (and it must be quick)
- ❌ 0/1 knapsack when exact answer required

---

### 4️⃣ Branch and Bound

**Complexity:** Worst-case exponential, but often much faster in practice

**Very input-dependent** (depends on data and bounds tightness)

**Practical Limits:**

| Items | Best Case | Worst Case | Typical |
|-------|-----------|-----------|---------|
| 30 | ✅ Fast | ✅ OK | ✅ Good |
| 40 | ✅ Good | ⚠️ Slow | ✅ Reasonable |
| 50 | ⚠️ Slow | ❌ Very slow | ⚠️ Borderline |
| 60 | ❌ Very slow | ❌ Impossible | ❌ Don't try |

**Works Best When:**
- Items are sorted by value/weight ratio
- Bounds are tight
- Data has structure you can exploit
- You can prune many branches early

**Rule of Thumb:** Exact, but **fragile** — reliable up to ~**50 items**, dies around **60**

**When to Use:**
- ✅ Interview when optimality matters
- ✅ When you can tighten bounds
- ⚠️ Production (risky for large inputs)

---

### 5️⃣ Meet-in-the-Middle

**Complexity:** O(2^(n/2)) — splits problem into two halves

**Practical Limits:**

| Items | Space | Time | Feasible? |
|-------|-------|------|-----------|
| 30 | 32 MB | < 1 sec | ✅ |
| 40 | 512 MB | ~5 sec | ✅ |
| 45 | ~4 GB | ~30 sec | ⚠️ |
| 50 | ~32 GB | ~5 min | ⚠️ |
| 55 | ~256 GB | ~1 hour | ❌ |

**Rule of Thumb:** Hard ceiling around **~50 items** (dominated by space, not time)

**When to Use:**
- ✅ Interview: impressive and exact for ~40 items
- ✅ When you need exact answer for medium-sized input
- ❌ Large inputs (memory explosion)

---

### 6️⃣ Approximation (FPTAS - Fully Polynomial Time Approximation)

**Complexity:** O(n² / ε) where ε = allowed error

**Practical Limits:**

| Items | Error | Time | Feasible? |
|-------|-------|------|-----------|
| 10⁴ | 1% | < 1 sec | ✅ |
| 10⁵ | 1% | ~10 sec | ✅ |
| 10⁶ | 1% | ~100 sec | ✅ |
| 10⁷ | 1% | ~1000 sec | ⚠️ |
| 10⁵ | 0.01% | ~100 sec | ⚠️ |
| 10⁶ | 0.01% | ~1000 sec | ⚠️ |

**Accuracy Trade-off:**
```
1% error → very fast
0.1% error → slower
0.01% error → slow
0.001% error → very slow
```

**Rule of Thumb:** Scales **extremely well** if you allow small error (1-5%)

**When to Use:**
- ✅ When exact is overkill
- ✅ When you have millions of items
- ✅ When 1-5% error is acceptable
- ❌ When you absolutely need optimal

---

### 7️⃣ Heuristics / Metaheuristics

**Examples:** Genetic algorithms, simulated annealing, ant colony optimization

**Complexity:** Depends on iterations, not n

**Practical Limits:**

| Items | Feasible? | Notes |
|-------|-----------|-------|
| 10⁴ | ✅ | Fast, good solutions |
| 10⁵ | ✅ | Industry standard |
| 10⁶ | ✅ | Takes time but works |
| 10⁷ | ⚠️ | Memory/iteration overhead |
| 10⁸+ | ❌ | Rarely justifiable |

**Rule of Thumb:** **No optimality guarantee**, but often very good solutions in reasonable time

**When to Use:**
- ✅ **Industry standard** for real knapsack problems
- ✅ When large inputs and fast approximation needed
- ✅ When you have time budget not accuracy budget
- ❌ When optimal is absolutely required

---

### 8️⃣ Integer Linear Programming (ILP)

**Using solvers:** CPLEX, Gurobi, CBC, SCIP

**Complexity:** NP-hard, but solvers are insanely optimized

**Practical Limits:**

| Binary Variables | Feasible? | Notes |
|------------------|-----------|-------|
| ≤ 1,000 | ✅ | Fast, < 1 second |
| ≤ 5,000 | ⚠️ | 1-10 seconds |
| ≤ 10,000 | ⚠️ | 10-60 seconds |
| ≥ 20,000 | ❌ | Exact is hard |

**Approximations/Relaxations:**
```
Linear Programming (relaxed): 100,000+ variables ✅
Cutting planes: 10,000-50,000 ✅
Exact (branch & cut): 5,000-10,000 ⚠️
```

**Rule of Thumb:** Solvers are incredibly smart, but still NP-hard. Expect **1-5k variables** for reasonable solve time

**When to Use:**
- ✅ When you have a solver available
- ✅ Production systems with $ budget
- ✅ Complex constraints (not just capacity)
- ❌ Interviews (too heavy-weight)

---

## 🎯 Big Comparison Table (Bookmark This!)

| Method | Exact? | Dies At | Best For |
|--------|--------|---------|----------|
| **Brute Force** | ✅ | ~30 items | Proof of concept, tiny inputs |
| **DP (Capacity)** | ✅ | W ≈ 10⁶ | Classic interview, medium capacity |
| **Greedy** | ❌ | Never (wrong) | Fractional knapsack, approximation |
| **Branch & Bound** | ✅ | ~50-60 items | Interview + tightable bounds |
| **Meet-in-Middle** | ✅ | ~50 items | Interview (impresses people) |
| **FPTAS** | ❌ | 10⁶+ items | When 1% error OK, huge inputs |
| **Heuristics** | ❌ | 10⁸+ items | **Industry standard for real problems** |
| **ILP Solver** | ✅ | 1k-5k vars | Production + complex constraints |

---

## 💡 Quick Decision Guide

```
Input Size: n = 30?
├─ YES → Use DP or Branch & Bound (exact, reasonable time)
└─ NO
    │
    Input Size: n = 50?
    ├─ YES → Use Meet-in-Middle or ILP solver
    └─ NO
        │
        Input Size: n = 1000?
        ├─ YES → Use DP (if capacity ≤ 10⁶)
        └─ NO
            │
            Input Size: n = 100,000?
            ├─ YES → Use FPTAS or Heuristics
            └─ NO
                └─ Use Heuristics/Metaheuristics + ILP relaxation
```

---

## Traveling Salesman Problem (TSP) — Practical Limits

### Why TSP is Harsher Than Knapsack

**Key Difference:**

- **Knapsack** → Combinations (2ⁿ)
- **TSP** → Permutations ((n−1)!)

**Factorial growth is FAR worse than exponential.** That's why TSP collapses much earlier.

**Comparison:**
```
n = 20:
  2ⁿ = 1,048,576 (millions)
  n! = 2.4 × 10¹⁸ (quintillions) ← 1 TRILLION TIMES WORSE
```

---

### 1️⃣ Brute Force TSP (Try All Tours)

**Complexity:** O((n−1)! / 2) with symmetry removed

**Practical Limits:**

| Cities (n) | Tours | Feasible? | Time Estimate |
|-----------|-------|-----------|---------------|
| 10 | ~180k | ✅ | < 1 ms |
| 12 | ~20M | ⚠️ | ~1 second |
| 14 | ~3.1B | ⚠️ | ~30 seconds |
| 15 | ~43B | ❌ | ~10 minutes |
| 20 | ~60 quadrillion | ☠️ | Never |

**Rule of Thumb:** Brute-force TSP **dies hard at ~12-14 cities**

**Comparison to Knapsack:**
- Knapsack brute force: ~30 items
- TSP brute force: ~12 cities
- **TSP dies 2.5x earlier**

---

### 2️⃣ DFS / Backtracking (Still Brute Force)

Just brute force with recursion.

**Improvement?** Slight pruning, but hits the same factorial wall

**Practical Limit:** ~15 cities max

**Why?** Without a good upper bound, can't prune effectively

---

### 3️⃣ Branch and Bound (Exact, Smarter)

**Idea:** DFS + prune paths that already exceed best known cost

**Practical Limits (highly input-dependent):**

| Cities | Feasible? | Notes |
|--------|-----------|-------|
| ≤ 20 | ✅ | Good pruning possible |
| 25 | ⚠️ | Borderline, depends on data |
| 30 | ❌ | Bad distance distributions defeat pruning |
| ≥ 35 | ☠️ | Worst case is still factorial |

**Rule of Thumb:** Exact B&B dies around **25-30 cities**

**Why it fails:**
- Worst-case still factorial
- Bad pruning when cities are scattered randomly
- Real-world TSP often has structure that helps; random data is worst-case

---

### 4️⃣ Dynamic Programming (Held–Karp Algorithm)

**Complexity:** O(n² × 2ⁿ)

**Memory:** O(n × 2ⁿ) - the killer constraint

**Practical Limits:**

| Cities | Memory | Time | Feasible? |
|--------|--------|------|-----------|
| 16 | 16 KB | < 1 sec | ✅ |
| 18 | 64 KB | ~1 sec | ✅ |
| 20 | 256 KB | ~5 sec | ✅ |
| 22 | 1 MB | ~20 sec | ⚠️ |
| 24 | 4 MB | ~2 min | ⚠️ |
| 25 | 8 MB | ~5 min | ⚠️ |
| 26 | 16 MB | ~10 min | ⚠️ |
| 28 | 64 MB | ~1 hour | ❌ |

**Rule of Thumb:** Exact DP dies around **22-24 cities** (memory wall hits hard)

**Why it's famous:** Best general exact algorithm for small TSP, but still fundamentally exponential

---

### 5️⃣ Meet-in-the-Middle (Rarely Used for TSP)

Hard to apply cleanly to TSP structure.

Slight gains only.

**Practical Limit:** ~25 cities (theoretical, hard to implement well)

---

### 6️⃣ Approximation Algorithms (Guaranteed Bounds)

**Example:** Christofides Algorithm (for metric TSP)

- Always ≤ 1.5 × optimal
- Polynomial time
- Only works for metric TSP (triangle inequality holds)

**Practical Limits:**

| Cities | Feasible? |
|--------|-----------|
| 10⁵ | ✅ |
| 10⁶ | ✅ |
| 10⁷ | ✅ |

**Rule of Thumb:** **Scales perfectly** if you accept 1.5× non-optimality

**Catch:** Only works for metric TSP, not arbitrary distances

---

### 7️⃣ Heuristics (Industry Standard)

**Examples:**
- Nearest Neighbor
- 2-opt / 3-opt local search
- Lin–Kernighan heuristic
- Simulated Annealing
- Genetic Algorithms
- Ant Colony Optimization

**Practical Limits:**

| Cities | Feasible? | Solution Quality |
|--------|-----------|------------------|
| 1,000 | ✅ | Within 0.5-2% of optimal |
| 10,000 | ✅ | Within 1-3% of optimal |
| 100,000 | ✅ | Within 2-5% of optimal |
| 1,000,000 | ⚠️ | Time/memory intensive |

**Rule of Thumb:** **This is how logistics actually solves TSP**

**Why heuristics work:**
- Real-world TSP has structure (geographic clusters, highways)
- Random starting points → hill climbing → local optima → often very good
- Can run multiple times and pick best

**Accuracy:** Often within 0.1-2% of optimal (no guarantee, but empirically excellent)

---

### 8️⃣ Integer Linear Programming (with Cutting Planes)

**Reality:** This is how world-record TSP instances are solved

**Achievements:**
- Exact solution for **85,900+ cities** (Concorde TSP Solver)
- But... months of computation
- Massive cutting plane generation
- Geometric structure exploited (Euclidean metric)

**Why this works:**
- Real maps ≠ worst-case TSP
- Euclidean geometry saves you (most permutations eliminated by geometry)
- Cutting planes destroy infeasible regions
- Massive computational resources

**Practical Limits:**
- Without special structure: 1k-5k cities
- With Euclidean geometry: 10k-100k cities
- Record holders: 80k+ cities (special cases only)

---

## 🎯 Big Comparison Table (TSP)

| Method | Exact? | Dies At | Best For |
|--------|--------|---------|----------|
| **Brute Force** | ✅ | ~12-14 cities | Tiny inputs only |
| **DFS / Backtracking** | ✅ | ~15 cities | Interview naive approach |
| **Branch & Bound** | ✅ | ~25-30 cities | Interview + good pruning |
| **DP (Held–Karp)** | ✅ | ~22-24 cities | Exact for small TSP |
| **Meet-in-Middle** | ✅ | ~25 cities | Theoretical (hard to implement) |
| **Approximation** | ❌ | ~10⁶ cities | Guaranteed 1.5× optimal |
| **Heuristics** | ❌ | ~10⁵-10⁶ cities | **Industry standard** |
| **ILP + Cuts** | ✅ | ~85k cities | Real-world with structure |

---

## 🔥 TSP vs Knapsack: The Key Contrast

| Aspect | Knapsack | TSP |
|--------|----------|-----|
| **Growth** | 2ⁿ | (n−1)! |
| **Exact Limit** | ~50 items | ~25 cities |
| **Why** | Combinations | Permutations |
| **Approx scales to** | Very well (10⁶+) | Very well (10⁶+) |
| **Industry use** | Approx / ILP | **Heuristics / ILP** |
| **Worst-case** | Hopeless | Impossibly hopeless |
| **Real-world** | Structured → approx works | Structured → heuristics work |

---

## 💡 One-Sentence Takeaway (Remember This)

**"Exact TSP dies around 25 cities; practical TSP scales to hundreds of thousands by giving up perfection."**

---

## Why Quantum Computers Don't Save TSP

This is important: there's a lot of hype around quantum computing and NP-hard problems. Let me explain what's real and what's myth.

### The Short Answer (No Hype)

**Quantum computers do not:**
- ❌ Magically try all TSP routes at once
- ❌ Read out exponentially many answers
- ❌ Turn factorial-time problems into polynomial-time ones

**Therefore:** Quantum doesn't save TSP.

---

### Myth to Kill First: "Quantum Tries All Possibilities in Parallel"

**The claim:** Quantum superposition lets us check all routes simultaneously.

**The reality:** A quantum system can represent many states at once, but **when you measure, you get ONE answer**. The other states vanish.

**Real-world analogy 🎭**

Imagine:
1. **1 trillion people silently try different routes**
2. **You're allowed to ask ONE of them for their answer**
3. **The rest vanish instantly**

That's quantum measurement.

**Parallelism without readable output is useless** unless you can amplify the right answer through interference.

---

### Why Quantum Helps SOME Problems (But Not TSP)

Quantum gives genuine speedups when:

✅ **You can interfere paths** → wrong answers cancel out, right answers amplify
✅ **Strong mathematical structure** → global properties you can exploit
✅ **Specific goal states** → interference naturally amplifies them

**Examples where quantum helps:**
- Factoring large numbers (Shor's algorithm)
- Searching unsorted databases (Grover's algorithm)
- Problems with clear symmetry

**TSP does NOT have this structure:**
- ❌ No interference pattern among routes
- ❌ No global property to amplify
- ❌ No mathematical shortcut

---

### What Quantum CAN Do: Grover's Algorithm

Grover's algorithm gives a **quadratic speedup**.

**Classic search:** N possibilities take N time (try them all)

**Quantum search:** N possibilities take √N time

**For TSP with brute force:**

| Approach | Time |
|----------|------|
| Classical brute force | (50−1)! ≈ 10³² |
| Quantum brute force | √((50−1)!) ≈ 10¹⁶ |

**Result:** Still hopeless. You can't compute 10¹⁶ operations in reasonable time.

**Key insight:** Quadratic speedup ≠ salvation when dealing with factorials.

---

### Why You Can't "Encode Shortest Route" Cleverly

**The idea:** Use quantum interference to amplify only the shortest route.

**The problem:** To do that, you'd need to:

1. Compare all route lengths somehow
2. Without measuring them (which collapses superposition)
3. Amplify only the optimal one

**But here's the catch:**

Comparing route lengths **already requires evaluating them**, which is the hard part.

You can't get quantum interference "for free" — you'd still have to do the exponential work.

**No free lunch:** Quantum doesn't bypass the fundamental hard work.

---

### The Measurement Wall 🚧

**The hard limit:**

Quantum computers **cannot:**
- ❌ Output exponential amounts of information
- ❌ Reveal which of exponentially many states was best
- ❌ Collapse to the optimal solution deterministically

**Why?** Information theory forbids it.

**Intuition:** If you could extract exponentially many bits of information from a polynomial-sized system, you could solve any NP problem easily. But that's believed false.

---

### What Theorists Actually Know

**Proven facts:**

- Grover's algorithm is optimal for unstructured search
- No quantum algorithm is known to solve NP-complete problems efficiently
- Most complexity theorists believe:

```
NP ⊈ BQP

(NP problems cannot all be solved efficiently by quantum computers)
```

**In plain English:**
Even with quantum computers, we don't know how to efficiently solve NP-complete problems like TSP.

---

### Real-World Quantum Optimization (What Actually Happens)

**How quantum is used in practice:**

Quantum is treated as **another heuristic**, like simulated annealing:

#### Quantum Annealing (D-Wave)
- Finds good (not optimal) routes
- Sometimes helps, sometimes doesn't
- No guarantees
- Scales poorly

#### QAOA (Quantum Approximate Optimization Algorithm)
- Designed for combinatorial problems
- Empirically mixed results
- Often no better than classical heuristics

**Critical point:** These do **not break NP-completeness**. They're just another hill-climbing technique.

---

### Why Geometry Beats Quantum

**Here's a key insight that many miss:**

```
Classical heuristics exploit Euclidean geometry.
Quantum algorithms do not get extra leverage from geometry.
Geometry helps classical methods MORE than quantum helps.
```

**Real-world TSP has:**
- Cities in space (Euclidean metric)
- Triangle inequality (distances are consistent)
- Geographic clustering (cities group together)

**Classical algorithms exploit all of this:**
- Nearest neighbor works ~1% off optimal because clusters exist
- 2-opt local search finds great routes by respecting geography
- Lin–Kernighan uses spatial structure brilliantly

**Quantum doesn't get any of these advantages.** A quantum computer can't "see" that cities form clusters.

---

### The Core Reason (This is Inevitable)

**TSP is hard because:**

There are too many distinct answers, and **quantum mechanics cannot let you read exponentially many answers**.

**That's the brick wall.**

You cannot:
1. Create a superposition of all solutions
2. Extract which one is best
3. Without this step being the exponential work

Superposition without readout is a magic trick, not computation.

---

### Why Quantum Won't Save You in 10 Years Either

Even if quantum computers get much better:

**Scaling problems:**
- Quantum systems are extremely fragile
- Error rates scale with problem size
- Creating/maintaining superposition gets harder
- Temperature requirements keep dropping

**Complexity barriers:**
- Even with perfect quantum hardware, the algorithm limits remain
- You still can't extract exponential information
- You still can't bypass combinatorial explosion

**The honest truth:**
Quantum might be useful for some problems, but TSP is not one of them.

---

## 🎯 Quantum vs Classical for NP-Hard Problems

| Aspect | Classical | Quantum |
|--------|-----------|---------|
| **Brute Force Speedup** | Baseline | √(2ⁿ) quadratic |
| **Heuristics** | **Very effective** | Marginal |
| **Exploits Geometry** | **Yes** | No |
| **Solves TSP Exactly** | Up to ~25 cities | Up to ~25 cities |
| **Practical Use** | Industry standard | Research only |
| **Promise vs Reality** | Matches | Hype > Reality |

---

## 💡 One-Liner You Can Use

**"Quantum computers give quadratic speedup on brute force, but that's not enough when you're dealing with factorials. For TSP, classical heuristics actually outperform quantum approaches."**

Or even shorter:

**"Quantum doesn't turn exponential into polynomial. For TSP, geometry beats physics."**

---

## 0/1 Knapsack Problem

### Problem Statement

You are given:
- **n** items
- Each item has:
  - `wt[i]` → weight
  - `val[i]` → value
- A knapsack with maximum capacity **W**

**Goal:** Find the maximum total value that can be put in the knapsack without exceeding weight W.

**Constraint:** Each item can be chosen at most once (0/1 choice).

### Why Dynamic Programming?

DP is used because:
- Subproblems repeat
- Optimal solution depends on optimal solutions of smaller subproblems
- Overlapping subproblems exist

### DP State Definition

```
dp[i][w] = maximum value using first i items with weight limit w
```

### DP Transition (MOST IMPORTANT)

For each item `i` and weight `w`, we have two choices:

#### Option 1: Do NOT take item i
```
dp[i][w] = dp[i-1][w]
```

**Meaning:**
- Skip the current item
- Best value remains what we already computed using previous items

#### Option 2: Take item i (only if wt[i] ≤ w)
```
dp[i][w] = val[i] + dp[i-1][w - wt[i]]
```

**Meaning:**
- Add value of current item
- Reduce remaining weight
- Use previous items only (0/1 constraint)

#### Final Recurrence
```
dp[i][w] = max(
    dp[i-1][w],                              # do not take
    val[i] + dp[i-1][w - wt[i]]            # take item
)
```

### Base Cases

```
dp[0][w] = 0    # no items → no value
dp[i][0] = 0    # no capacity → no value
```

### Python Code (2D DP)

```python
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
```

### Special Explanations

#### Why dp[i-1][w]?
```python
dp[i][w] = dp[i - 1][w]
```

If we skip the current item, we reuse the best solution from previous items for the same weight.

#### Why val[i-1] + dp[i-1][w - wt[i-1]]?
```python
val[i - 1] + dp[i - 1][w - wt[i - 1]]
```

If we take the item:
- Add its value
- Reduce remaining weight
- Use only previous items (0/1 rule)

#### Why max(...)?
```python
dp[i][w] = max(not_take, take)
```

We always choose the best of the two choices.

### Example Walkthrough

```
Items:    wt = [2, 3, 4, 5]
          val = [3, 4, 5, 6]
Capacity: W = 5

dp[0][w] = 0 (base case)

For item 1 (wt=2, val=3):
  dp[1][0] = 0
  dp[1][1] = 0 (can't fit)
  dp[1][2] = max(dp[0][2], 3 + dp[0][0]) = max(0, 3) = 3
  dp[1][3] = max(dp[0][3], 3 + dp[0][1]) = max(0, 3) = 3
  dp[1][4] = 3, dp[1][5] = 3

For item 2 (wt=3, val=4):
  dp[2][5] = max(dp[1][5], 4 + dp[1][2]) = max(3, 4+3) = 7
  ...

Final: dp[4][5] = maximum value with capacity 5
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n × W) |
| **Space Complexity** | O(n × W) for 2D DP, O(W) for 1D DP |

Where:
- n = number of items
- W = knapsack capacity

### Space-Optimized Version (1D DP)

```python
def knapsack_1d(wt, val, W):
    dp = [0] * (W + 1)

    for i in range(len(wt)):
        # Traverse from right to left to avoid using updated values
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]
```

**Why reverse iteration?** We must process weights from right to left to avoid using the same item twice.

### Pseudo-Polynomial Time Complexity

❗ **Important:** 0/1 Knapsack is **pseudo-polynomial**, not truly polynomial.

**What does this mean?**

An algorithm is pseudo-polynomial if its running time is polynomial in the numeric value of the input, not in the size of the input (number of bits).

#### Example
```
W = 1,000,000
Input size (bits) = log₂(1,000,000) ≈ 20 bits

Algorithm time = O(n × W) = O(n × 1,000,000)
This is NOT polynomial in input size (bits)
```

**Conclusion:** This DP solution works only when W is reasonably small.

### Key Insights

1. **State Representation:** `dp[i][w]` captures all necessary information
2. **Optimal Substructure:** Solution uses optimal solutions of subproblems
3. **Non-overlapping Choice:** We explicitly choose to take or not take each item
4. **Bottom-up Approach:** We build from smaller problems to larger ones

---

## Minimum Coins Problem

### Problem Statement

Given:
- An array of coin denominations
- A target amount

**Goal:** Find the minimum number of coins needed to make the target amount.

### Examples

```python
coins = [1, 2, 5]
amount = 13

Possible combinations:
- 13 × 1 = 13 coins
- 6 × 2 + 1 × 1 = 7 coins
- 2 × 5 + 3 × 1 = 5 coins (but using 2 and 5 better)
- 2 × 5 + 1 × 2 + 1 × 1 = 4 coins
- 1 × 5 + 4 × 2 = 5 coins

Minimum: 4 coins (5 + 5 + 2 + 1)
```

### DP Approach

**State:** `dp[i]` = minimum coins needed to make amount i

**Transition:** For each coin, update all amounts that can be formed:
```
dp[amount] = min(dp[amount], dp[amount - coin] + 1)
```

### Python Solution

```python
def find_minimum_coins(coins, amount):
    # dp[i] = minimum coins to make amount i
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # base case: 0 coins for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1

# Example
result = find_minimum_coins([1, 2, 5], 13)
print(result)  # Output: 4
```

### With Path Reconstruction

```python
def find_minimum_coins_with_path(coins, amount):
    dp = [float("inf")] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    # Reconstruct path
    path = []
    current = amount
    while current > 0:
        coin = parent[current]
        path.append(coin)
        current -= coin

    return dp[amount], path
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(amount × n) where n = number of coins |
| **Space** | O(amount) |

### Key Differences from 0/1 Knapsack

| Feature | 0/1 Knapsack | Coin Change |
|---------|--------------|-------------|
| **Items** | Limited (each once) | Unlimited (each multiple times) |
| **DP Loop** | Iterate items then weights | Iterate amounts then coins |
| **Weight Constraint** | Maximum weight W | Exact amount |
| **Iteration Order** | Can be forward | Must be forward (allowing reuse) |

### Interview Tips

1. **Unbounded vs 0/1:** Coin change is unbounded (can use coins multiple times)
2. **Greedy Won't Work:** Greedy approach (always pick largest coin) fails for some coin sets
3. **Base Case:** Always initialize `dp[0] = 0`
4. **Impossible Cases:** Check if result is still infinity (impossible amount)

---

## Summary Comparison

| Problem | Constraint | Approach | Use Case |
|---------|-----------|----------|----------|
| **0/1 Knapsack** | Each item once | 2D DP with careful transition | Item selection, project selection |
| **Coin Change** | Coins unlimited | 1D DP, forward iteration | Making change, combinations |
| **DP Key** | Identify state | Subproblems overlap | Optimization problems |
