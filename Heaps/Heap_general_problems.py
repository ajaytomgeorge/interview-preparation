Great 👍
Below are clean Python implementations + clear explanations for each heap interview question, written in an interview-ready style.

I’ll use Python’s heapq (which is a min-heap).
For max-heap, we negate values.

1️⃣ K Largest Elements
🔹 Problem

Find the K largest elements in an array.

✅ Approach

Maintain a min-heap of size K

If heap size exceeds K → pop the smallest

Heap always stores K largest seen so far

🧠 Why it works

Smallest among K largest stays at the top and gets removed when a larger element appears.

🧩 Code
import heapq

def k_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap

⏱ Complexity

Time: O(N log K)

Space: O(K)

2️⃣ K Smallest Elements
🔹 Problem

Find the K smallest elements.

✅ Approach

Use a max-heap of size K

Python has only min-heap → store negative values

🧠 Why it works

The largest among the K smallest gets removed when a smaller number appears.

🧩 Code
import heapq

def k_smallest(nums, k):
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [-x for x in max_heap]

⏱ Complexity

Time: O(N log K)

Space: O(K)

3️⃣ Top K Frequent Elements
🔹 Problem

Return the K most frequent elements.

✅ Approach

Count frequency using a dictionary

Use a min-heap ordered by frequency

Keep heap size ≤ K

🧩 Code
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]

🧠 Heap stores
(frequency, number)

⏱ Complexity

Time: O(N log K)

Space: O(K)

4️⃣ Find Median from Data Stream
🔹 Problem

Support:

addNum(num)

findMedian()

✅ Approach (Classic)

Max-heap → left half

Min-heap → right half

Balance sizes so difference ≤ 1

🧩 Code
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max heap (negative values)
        self.right = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.left, -num)

        # Ensure ordering property
        if self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance sizes
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2

⏱ Complexity

Insert: O(log N)

Median: O(1)

5️⃣ Priority Queue (Task Scheduling)
🔹 Problem

Execute highest priority task first.

✅ Approach

Use a max-heap

Store (−priority, task)

🧩 Code
import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []

    def add_task(self, task, priority):
        heapq.heappush(self.heap, (-priority, task))

    def execute_task(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]

🧠 Use cases

OS scheduling

Job queues

Network packet prioritization

6️⃣ K Closest Points to Origin
🔹 Problem

Find K closest points to (0,0).

✅ Approach

Use a max-heap of size K

Store (−distance, point)

🧩 Code
import heapq

def k_closest(points, k):
    max_heap = []

    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(max_heap, (-dist, (x, y)))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for dist, point in max_heap]

⏱ Complexity

Time: O(N log K)

Space: O(K)