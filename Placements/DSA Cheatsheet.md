---
title: DSA Cheatsheet for Technical Interviews
tags: [DSA, interviews, python, algorithms, datastructures]
created: 2024-01-17
---

# 📚 Data Structures and Algorithms Cheatsheet

> [!info] About This Guide
> A comprehensive guide for DSA interview preparation with Python implementations, common patterns, and interview tips.

## 📋 Quick Reference

> [!tip] Big-O Cheatsheet
> - O(1) - Constant
> - O(log n) - Logarithmic
> - O(n) - Linear
> - O(n log n) - Linearithmic
> - O(n²) - Quadratic
> - O(2ⁿ) - Exponential
> - O(n!) - Factorial

## 🔄 Common Coding Patterns
1. Two Pointers
2. Sliding Window
3. Fast and Slow Pointers
4. Binary Search
5. DFS/BFS
6. Dynamic Programming
7. Backtracking

## 📈 Arrays and Strings

> [!note] Overview
> Arrays are fundamental data structures that store elements in contiguous memory locations.

### Implementation and Basic Operations
```python
# Basic array operations
def array_operations():
    # Initialize
    arr = []
    
    # Append - O(1)
    arr.append(5)
    
    # Insert at index - O(n)
    arr.insert(0, 3)
    
    # Delete - O(n)
    arr.pop()  # removes last element
    
    # Search - O(n)
    element = arr[0]  # O(1) for known index
    
    # Slice - O(k) where k is slice size
    sub_arr = arr[1:4]
```

### Common Interview Questions
1. Two Sum
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 🔗 Linked Lists

> [!note] Overview
> A linked list is a linear data structure where elements are stored in nodes, each pointing to the next node.

### Implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
```

## 📚 Stacks and Queues

> [!note] Overview
> Stack: LIFO (Last In First Out)
> Queue: FIFO (First In First Out)

### Stack Implementation
```python
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if self.items else None
        
    def peek(self):
        return self.items[-1] if self.items else None
        
    def is_empty(self):
        return len(self.items) == 0
```

### Queue Implementation
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.popleft() if self.items else None
        
    def is_empty(self):
        return len(self.items) == 0
```

## 🌳 Trees

> [!note] Overview
> Trees are hierarchical data structures with a root node and child nodes.

### Binary Tree Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# DFS Traversals
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## 🕸️ Graphs

> [!note] Overview
> Graphs consist of vertices connected by edges. They can be directed or undirected.

### Implementation
```python
# Adjacency List representation
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
```

## 🎯 Dynamic Programming

> [!note] Overview
> Solving complex problems by breaking them down into simpler subproblems.

### Example: Fibonacci with Memoization
```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

## 🔍 Searching and Sorting

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Quick Sort
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

## 📝 Interview Preparation Tips

> [!tip] Interview Success Strategies
> 1. Always think aloud while solving problems
> 2. Start with brute force, then optimize
> 3. Consider edge cases
> 4. Test your solution with examples
> 5. Analyze time and space complexity
> 6. Practice writing clean, readable code

## 🔗 Practice Resources
- [[LeetCode]] - Platform for coding practice
- [[HackerRank]] - Coding challenges and contests
- [[GeeksforGeeks]] - DSA articles and problems
- [[InterviewBit]] - Interview preparation platform

> [!warning] Remember
> - Focus on understanding concepts rather than memorizing solutions
> - Regular practice is key
> - Learn common patterns and techniques
> - Always optimize your solutions


## 🛠️ Python Power Tools

> [!note] Overview
> Python provides powerful built-in tools and modules that can significantly simplify coding tasks and improve efficiency.

### Collections Module
```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter - count occurrences
nums = [1, 2, 2, 3, 3, 3]
counts = Counter(nums)  # Counter({3: 3, 2: 2, 1: 1})

# defaultdict - dictionary with default values
graph = defaultdict(list)
graph[1].append(2)  # No KeyError if key doesn't exist

# deque - efficient double-ended queue
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)

# namedtuple - create simple classes
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# OrderedDict - dictionary that remembers insertion order
od = OrderedDict()
od['a'] = 1
od['b'] = 2
```

### Itertools Module
```python
from itertools import combinations, permutations, product, cycle

# combinations
list(combinations('ABC', 2))  # [('A','B'), ('A','C'), ('B','C')]

# permutations
list(permutations('ABC', 2))  # [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

# product - cartesian product
list(product('AB', '12'))  # [('A','1'), ('A','2'), ('B','1'), ('B','2')]

# cycle - infinite iterator
counter = cycle(['A', 'B', 'C'])
[next(counter) for _ in range(5)]  # ['A', 'B', 'C', 'A', 'B']
```

### Functools Module
```python
from functools import reduce, partial, lru_cache

# reduce - apply function to sequence
reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24

# partial - fix function arguments
base_two = partial(int, base=2)
base_two('1010')  # 10

# lru_cache - memoization decorator
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Heapq Module
```python
import heapq

# heapify and operations
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)
heapq.heappush(nums, 2)
smallest = heapq.heappop(nums)
k_smallest = heapq.nsmallest(3, nums)
```

### Bisect Module
```python
import bisect

# binary search and insertion
sorted_nums = [1, 3, 5, 7, 9]
insert_pos = bisect.bisect_left(sorted_nums, 4)  # 2
bisect.insort_left(sorted_nums, 4)  # [1, 3, 4, 5, 7, 9]
```

### List/Dict/Set Comprehensions
```python
# List comprehension
squares = [x*x for x in range(10) if x % 2 == 0]

# Dict comprehension
square_map = {x: x*x for x in range(5)}

# Set comprehension
unique_squares = {x*x for x in range(-5, 5)}
```

### Lambda Functions and Map/Filter/Reduce
```python
# Lambda with map
squares = list(map(lambda x: x**2, range(5)))

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# Reduce with lambda
from functools import reduce
factorial = reduce(lambda x, y: x*y, range(1, 6))  # 120
```

### Advanced String Methods
```python
# String operations
text = "  Hello, World!  "
text.strip()                     # Remove whitespace
text.lower()                     # Convert to lowercase
"123".zfill(5)                  # '00123'
",".join(['a', 'b', 'c'])       # 'a,b,c'
"hello,world".split(',')        # ['hello', 'world']
```

### Advanced Slicing
```python
# Advanced slicing operations
arr = list(range(10))
reversed_arr = arr[::-1]         # Reverse
every_second = arr[::2]          # Every 2nd element
last_three = arr[-3:]           # Last three elements
except_ends = arr[1:-1]         # All but first and last
```

> [!tip] Interview Tips for Python Tools
> - Use Counter for frequency counting problems
> - defaultdict for graph and tree problems
> - heapq for k-largest/smallest element problems
> - bisect for binary search in sorted arrays
> - List comprehensions for cleaner, more readable code
> - lru_cache for dynamic programming problems
