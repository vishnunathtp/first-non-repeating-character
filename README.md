# First Non-Repeating Character

An optimal and clean implementation to find the first non-repeating character in a string.

## Problem Description
Given a string `s`, find the first non-repeating character and return its index. If it does not exist, return `-1`.

### Example
- Input: `s = "loveleetcode"`
- Output: `2` (Character `'v'`)

## Approach & Complexity
1. Count frequencies of all characters in a single pass using a hash table / frequency map.
2. Iterate through the string a second time and return the index of the first character with a count of 1.

- **Time Complexity:** $O(N)$ where $N$ is the length of the string.
- **Space Complexity:** $O(1)$ auxiliary space (at most 26 lowercase English letters or $O(K)$ distinct characters).

## How to Run & Test
```bash
python solution.py
python -m unittest discover tests
```
