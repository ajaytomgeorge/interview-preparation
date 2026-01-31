# Minimum Operations with Powers of 2 (NAF - Non-Adjacent Form)

## Problem Statement

Given a positive integer $n$ (up to $2^{60}$), you need to reduce it to 0 using the minimum number of operations.

**In one operation, you can either:**
- Add $2^i$ (any power of 2, where $i \geq 0$)
- Subtract $2^i$

**Goal:** Find that minimum count of additions and subtractions.

---

## What is NAF (Non-Adjacent Form)?

You mentioned "NCF"—you likely mean **NAF (Non-Adjacent Form)**. This is a specific way of representing numbers that is incredibly popular in cryptography (like Elliptic Curve Cryptography) because it minimizes the "weight" of a number.

### Standard Binary vs NAF

**Standard Binary:** Uses digits $\{0, 1\}$  
**NAF:** Uses digits $\{0, 1, -1\}$

### The Rule

No two non-zero digits can be next to each other (i.e., you'll never see 1, 1 or 1, -1).

### Why It Matters Here

Every non-zero digit in a NAF representation corresponds to one addition or subtraction. Since NAF is guaranteed to have the minimum number of non-zero digits for any integer, finding the NAF weight is exactly the same as finding your "minimum operations."

---

## Approach: "Greedy Bitwise Strategy"

Since we want to eliminate as many $1$s as possible in the fewest moves, we look at the binary bits from right to left (least significant to most significant).

### If $n$ is even
- The last bit is 0
- No operation needed
- Shift right to look at the next bit

### If $n$ is odd
- Bit is 1, an operation is required
- Look at the last two bits using `(n & 3)`
- **3 in binary is '11'**

#### Case ...01 (Ends in 1)
- Subtracting $1$ is best
- It clears the bit and leaves a 0 behind

#### Case ...11 (Ends in 3)
- Adding $1$ is better
- It turns 11 into 100 (via a carry)
- You've turned two $1$s into a single $1$ further down the line
- Potentially saves many operations if there was a long string of $1$s

---

## Python Implementation

```python
def getMinOperations(n):
    operations = 0
    
    while n > 0:
        if n % 2 == 0:
            # Bit is 0, no operation needed. 
            # Shift right to look at the next bit.
            n //= 2
        else:
            # Bit is 1, an operation is required.
            # Look at the last two bits using (n & 3).
            # 3 in binary is '11'.
            if (n & 3) == 3:
                # If it ends in '11', adding 1 is more efficient 
                # because it triggers a carry.
                n += 1
            else:
                # If it ends in '01', just subtract the 1.
                n -= 1
            
            operations += 1
            
    return operations
```

---

## Example Testing

```python
print(f"Ops for 5: {getMinOperations(5)}")   # Output: 2
print(f"Ops for 21: {getMinOperations(21)}") # Output: 3
```

### Walkthrough: n = 5

```
Binary of 5: 101

Step 1: n = 5 (101), n & 3 = 01 → subtract 1
        operations = 1, n = 4

Step 2: n = 4 (100), n % 2 == 0 → shift right
        n = 2

Step 3: n = 2 (10), n % 2 == 0 → shift right
        n = 1

Step 4: n = 1 (1), n & 3 = 01 → subtract 1
        operations = 2, n = 0

Result: 2 operations ✅
```

### Walkthrough: n = 21

```
Binary of 21: 10101

Step 1: n = 21 (10101), n & 3 = 01 → subtract 1
        operations = 1, n = 20

Step 2: n = 20 (10100), n % 2 == 0 → shift right
        n = 10

Step 3: n = 10 (1010), n % 2 == 0 → shift right
        n = 5

Step 4: n = 5 (101), n & 3 = 01 → subtract 1
        operations = 2, n = 4

Step 5: n = 4 (100), n % 2 == 0 → shift right
        n = 2

Step 6: n = 2 (10), n % 2 == 0 → shift right
        n = 1

Step 7: n = 1 (1), n & 3 = 01 → subtract 1
        operations = 3, n = 0

Result: 3 operations ✅
```

---

## Why This Handles the $2^{60}$ Constraint

### Memory
- It only stores a few integers
- Uses almost no RAM

### Speed
- Even at $2^{60}$, the while loop runs a maximum of ~62 times
- On a modern CPU, this completes in microseconds

---

## Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(log n) |
| **Space** | O(1) |

This is optimal for the $2^{60}$ constraint.

---

## Key Intuition

The algorithm converts a number to its **Non-Adjacent Form (NAF)**:
- Each bit flip (operation) represents one addition or subtraction
- By greedily choosing to add when we see two consecutive 1s (to create a carry), we minimize the total number of non-zero bits
- This is provably optimal

---

## Related Question

Would you like me to show you how to adapt this logic if the problem restricted you to **only subtractions**?
