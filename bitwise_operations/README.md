# Bitwise Operations & Bit Manipulation

Bit manipulation problems that use XOR, AND, OR operations to solve classic coding challenges efficiently.

## 1. Single Number Problem (Classic XOR)

### Problem Statement

Given an array where every element appears **twice except one**, find the single number that appears only once.

**Constraint:** O(1) extra space, O(n) time

### Examples

```
Input:  [2, 2, 1]
Output: 1

Input:  [4, 1, 2, 1, 2]
Output: 4

Input:  [1]
Output: 1
```

### Key Insight: XOR Properties

XOR has magical properties for this problem:
- `a ^ a = 0` (any number XORed with itself = 0)
- `a ^ 0 = a` (any number XORed with 0 = itself)
- `a ^ b = b ^ a` (commutative)
- `(a ^ b) ^ c = a ^ (b ^ c)` (associative)

**The trick:** If we XOR all numbers, pairs cancel out to 0, leaving only the single number!

### Algorithm

```
result = 0
For each number in array:
    result ^= number
Return result
```

### Implementation

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example
print(singleNumber([2, 2, 1]))  # Output: 1
print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(n) - single pass |
| **Space** | O(1) - only one variable |

### Why XOR Works - Dry Run

```
Array: [4, 1, 2, 1, 2]

result = 0
result ^= 4  → result = 4 (binary: 100)
result ^= 1  → result = 5 (binary: 101)
result ^= 2  → result = 7 (binary: 111)
result ^= 1  → result = 6 (binary: 110) [1 appears twice, cancels]
result ^= 2  → result = 4 (binary: 100) [2 appears twice, cancels]

Final: 4 ✓
```

---

## 2. Every Element Appears 3 Times Except One

### Problem Statement

Every element appears **3 times except one** that appears once. Find the single number using O(1) space.

### Approach: Bit Counting

Since every bit position in the array appears multiple times (3x), count bits at each position:
- If bit count % 3 != 0 → this bit belongs to the single number

### Implementation

```python
def singleNumber3(nums):
    result = 0
    
    # Check each bit position (0 to 31)
    for i in range(32):
        bit_count = 0
        
        # Count how many numbers have bit i set
        for num in nums:
            if num & (1 << i):
                bit_count += 1
        
        # If bit_count % 3 != 0, set this bit in result
        if bit_count % 3 != 0:
            result |= (1 << i)
    
    # Handle negative numbers (two's complement)
    return result if result < (1 << 31) else ~(result ^ ((1 << 32) - 1))

# Example
print(singleNumber3([2, 2, 2, 1]))  # Output: 1
print(singleNumber3([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(32 × n) = O(n) |
| **Space** | O(1) |

### Why Bit Counting Works

```
Example: [2, 2, 2, 1]
Binary: [10, 10, 10, 01]

Bit 0 (ones place):
  Count = 1 (only from 1)
  1 % 3 = 1 → bit 0 is set in result

Bit 1 (twos place):
  Count = 3 (from all three 2s)
  3 % 3 = 0 → bit 1 is not set

Result = 01 = 1 ✓
```

---

## 3. Power of 2 Check

### Problem Statement

Check if a number **n is a power of 2** (2^k for some k ≥ 0).

### Examples

```
Input:  16
Output: True (2^4)

Input:  3
Output: False

Input:  1
Output: True (2^0)

Input:  0
Output: False
```

### Binary Insight

Powers of 2 have **exactly ONE bit set**:
- 1 = 0001
- 2 = 0010
- 4 = 0100
- 8 = 1000
- 16 = 10000

### Clever Trick: n & (n-1) == 0

If n is a power of 2, then `n & (n-1) == 0` because:

```
n =   8 = 1000
n-1 = 7 = 0111

8 & 7 = 1000 & 0111 = 0000 ✓
```

Why? Subtracting 1 from a power of 2 flips all bits to the right of the single 1-bit.

### Implementation

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Examples
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(3))   # False
print(isPowerOfTwo(1))   # True
print(isPowerOfTwo(0))   # False
```

### Complexity Analysis

| Metric | Value |
|--------|-------|
| **Time** | O(1) - constant bit operations |
| **Space** | O(1) |

### Verification

```
Powers of 2:
1  (0001) & 0  (0000) = 0 ✓
2  (0010) & 1  (0001) = 0 ✓
4  (0100) & 3  (0011) = 0 ✓
8  (1000) & 7  (0111) = 0 ✓
16 (10000) & 15 (01111) = 0 ✓

Non-powers:
3  (0011) & 2  (0010) = 2 ✗
6  (0110) & 5  (0101) = 4 ✗
7  (0111) & 6  (0110) = 6 ✗
```

---

## 4. Maximum XOR of Two Numbers (Bitwise Trie)

### Problem Statement

Given an array of numbers, find the **maximum XOR** of any two numbers in the array.

### Examples

```
Input:  [3, 10, 5, 25, 2, 8]
Output: 28 (25 ^ 5 = 11001 ^ 00101 = 11100 = 28)

Input:  [1, 2, 3, 4, 5]
Output: 7 (4 ^ 3 = 100 ^ 011 = 111 = 7)
```

### Key Insight

XOR is maximized when bits differ. To maximize:
- Build a Trie of all numbers' bits
- For each number, greedily choose opposite bits when possible

### Approach: Bitwise Trie

1. **Build Trie:** Store each number as a binary path (bit by bit)
2. **Traverse:** For each number, find a path with opposite bits

### Implementation

```python
class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None

def maxXorTrie(nums):
    # Build trie
    root = TrieNode()
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero
            else:
                if not node.one:
                    node.one = TrieNode()
                node = node.one
    
    # Find max XOR
    max_xor = 0
    for num in nums:
        current_xor = 0
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Greedily choose opposite bit
            opposite_bit = 1 - bit
            if opposite_bit == 0:
                if node.zero:
                    node = node.zero
                    current_xor |= (0 << i)
                else:
                    node = node.one
                    current_xor |= (1 << i)
            else:
                if node.one:
                    node = node.one
                    current_xor |= (1 << i)
                else:
                    node = node.zero
                    current_xor |= (0 << i)
        max_xor = max(max_xor, current_xor)
    
    return max_xor

# Example
print(maxXorTrie([3, 10, 5, 25, 2, 8]))  # Output: 28
```

### Simpler Brute Force (for understanding)

```python
def maxXor_brute(nums):
    max_xor = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            max_xor = max(max_xor, nums[i] ^ nums[j])
    return max_xor

# Time: O(n²), Space: O(1)
```

### Complexity Analysis

| Method | Time | Space |
|--------|------|-------|
| **Trie** | O(n × 32) = O(n) | O(n × 32) |
| **Brute** | O(n²) | O(1) |

---

## Bitwise Operators Quick Reference

| Operator | Name | Example |
|----------|------|---------|
| `&` | AND | `5 & 3 = 1` (0101 & 0011 = 0001) |
| `\|` | OR | `5 \| 3 = 7` (0101 \| 0011 = 0111) |
| `^` | XOR | `5 ^ 3 = 6` (0101 ^ 0011 = 0110) |
| `~` | NOT | `~5 = -6` (bitwise complement) |
| `<<` | Left shift | `5 << 1 = 10` (0101 << 1 = 1010) |
| `>>` | Right shift | `5 >> 1 = 2` (0101 >> 1 = 0010) |

---

## Common Bit Tricks

| Problem | Solution | Insight |
|---------|----------|---------|
| **Check power of 2** | `n & (n-1) == 0` | Only one bit set |
| **Count set bits** | `n & 1` repeatedly | Check each bit |
| **Set i-th bit** | `n \| (1 << i)` | OR with 1 at position |
| **Clear i-th bit** | `n & ~(1 << i)` | AND with 0 at position |
| **Toggle i-th bit** | `n ^ (1 << i)` | XOR to flip |
| **Get i-th bit** | `(n >> i) & 1` | Shift and check |
| **Clear rightmost bit** | `n & (n-1)` | Removes LSB |
| **Get rightmost bit** | `n & -n` | Isolates LSB |

---

## Related Problems

1. **Single Number** ✓ (covered)
2. **Single Number II** (3 times) ✓ (covered)
3. **Single Number III** (two singles, rest twice)
4. **Power of 2** ✓ (covered)
5. **Maximum XOR** ✓ (covered)
6. **Hamming Distance** - Count differing bits
7. **Number of 1 Bits** - Count set bits
8. **Reverse Bits** - Mirror binary representation
9. **Missing Number** - XOR all with indices
